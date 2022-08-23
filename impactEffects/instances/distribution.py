import os
import datetime
import time
import numpy as np
import pandas as pd


###################################################
class ProbabilityDistribution:
    """Abstract base class for all probability distributions

    Parameters
    ---------
    seed : int
        seed for the numpy.random.Generator instance
    """

    def __init__(self, seed):
        self.rng_ = np.random.default_rng(seed)

    ### ##################################
    def sample(self, n_samples=1):
        """Generate samples from the underlying distribution

        Parameters
        ----------
        n_samples : Union[int, array-like], optional
            number of samples or shape of array with random samples
            default : 1

        Returns
        -------
        samples : Union[float, numpy.ndarray]
            by default, a single sample is returned as a float
            if :param: n_samples > 1 or is array-like with size > 1,
                a numpy.ndarray of samples with the specified shape is returned
        """
        raise NotImplementedError("sample function must be implemented")

    ### ##################################
    def log_likelihood(self, samples):
        """Calculate log likelihood of samples; log is the natural logarithm

        Parameters
        ----------
        samples : Union[int, float, array-like]
            samples for which the log likelihood shall be calculated

        Returns
        -------
        likelihoods : Union[float, numpy.ndarray]
            If :param: samples is a single number or a size-1 array-like object,
                a single float with the log-likelihood is returned.
            Otherwise, a numpy.ndarray of log-likelihoods with the same shape as
                :param: samples is returned.
            For distributions with compact support, if likelihood = 0 => log-likelihood = -numpy.inf
        """
        raise NotImplementedError(
            "log_likelihood function must be implemented")


###################################################
class TableDistribution(ProbabilityDistribution):
    """Abstract base class for probability distributions defined by an interpolated CDF and PDF.
    Implements common sample() and log_likelihood() functions.

    Derived classes will have to implement a __init__ function that fills
    * self.cdf : numpy.ndarray
        latice points of cumulative distribution function, sorted in ascending order
    * self.log_cdf : numpy.ndarray
        latice points of log probability density function
    * self.values : numpy.ndarray
        x-values of self.cdf and self.log_pdf, sorted in ascending order

    Parameters
    ----------
    seed : int
        seed for the numpy.random.Generator instance

    TODO: implement linear interpolation between latice points for
          both sample() and log_likelihood()
    """

    def __init__(self, seed):
        super().__init__(seed)
        self.values = NotImplemented
        self.cdf = NotImplemented
        self.log_pdf = NotImplemented

    ### ##################################
    def sample(self, n_samples=1):
        uniform_samples = self.rng_.uniform(size=n_samples)
        indices = np.searchsorted(self.cdf, uniform_samples)

        if indices.size == 1:
            return self.values[indices.item()]
        else:
            return self.values[indices]

    ### ##################################
    def log_likelihood(self, samples):
        indices = np.searchsorted(self.values, samples)

        if indices.size > 1:
            assert indices.ndim == 1
            indices[np.isclose(samples, self.values[0])] = 1
            indices[np.isclose(samples, self.values[-1])
                    ] = self.values.size - 2

            likelihoods = np.empty_like(indices)
            if likelihoods.ndim == 0:
                likelihoods = np.array(-np.inf)
            else:
                likelihoods[:] = -np.inf

            likelihoods = pd.Series(likelihoods)
            mask = np.logical_and(indices > 0, indices < self.values.size)
            likelihoods[mask] = self.log_pdf[indices[mask] - 1]
            likelihoods = likelihoods.to_numpy()

        else:
            if indices > 0 and indices < self.values.size:
                likelihoods = self.log_pdf[indices - 1]
            elif np.isclose(samples, self.values[0]):
                likelihoods = self.log_pdf[0]
            elif np.isclose(samples, self.values[-1]):
                likelihoods = self.log_pdf[-1]
            else:
                likelihoods = -np.inf

        return likelihoods


###################################################
class FileTableDistribution(TableDistribution):
    """Probability distribution based on a CDF stored as a numpy array in an .npz file

    Parameters
    ----------
    npz_file : Union[str, Path-like]
        path to .npz file storing the numpy arrays

    values_key : str
        key for the values array in the .npz file

    cdf_key : str
        key for the CDF array in the .npz file

    seed : int
        seed for the numpy.random.Generator instance
    """

    def __init__(self, npz_file, values_key, cdf_key, seed):
        if not os.path.isfile(npz_file):
            raise FileNotFoundError("Could not find file {}".format(npz_file))
        super().__init__(seed)

        container = np.load(npz_file)
        self.values = container[values_key]
        self.cdf = container[cdf_key]
        container.close()

        if not (np.diff(self.values) > 0).all():
            raise ValueError("values array is not sorted in ascending order")

        pdf = np.diff(self.cdf) / np.diff(self.values)
        if not (pdf > 0).all():
            raise ValueError("CDF array is not sorted in ascending order")
        if not (self.cdf[0] > 0 and np.isclose(self.cdf[-1], 1)):
            raise ValueError("invalid CDF: min must be > 0, max = 1")

        self.log_pdf = np.log(pdf)


###################################################
class AngleDistribution(ProbabilityDistribution):
    """Probability distribution of prior for meteoroid impact angle (in radians).

    CDF(theta) = sin(theta)^2, PDF(theta) = sin(2*theta), 0 <= theta <= pi/2

    Source: Collins et al. (2017) [https://onlinelibrary.wiley.com/doi/abs/10.1111/maps.12873]

    Parameters
    ----------
    seed : int
        seed for the numpy.random.Generator instance
    """

    ### ##################################
    def sample(self, n_samples=1):
        """Generate samples from the angle distribution

        Parameters
        ----------
        n_samples : Union[int, array-like], optional
            number of samples or shape of array with random samples
            default : 1

        Returns
        -------
        samples : Union[float, numpy.ndarray]
            angles in radians

            By default, a single sample is returned as a float.
            If :param: n_samples > 1 or is array-like with size > 1,
                a numpy.ndarray of samples with the specified shape is returned.
        """
        uniform_samples = self.rng_.uniform(size=n_samples)
        if uniform_samples.size == 1:
            uniform_samples = uniform_samples.item()
        samples = np.arcsin(np.sqrt(uniform_samples))

        return samples

    ### ##################################
    def log_likelihood(self, samples):
        """Calculate log likelihood of samples; log is the natural logarithm

        Parameters
        ----------
        samples : Union[int, float, array-like]
            angles is radians for which the log likelihood shall be calculated

        Returns
        -------
        likelihoods : Union[float, numpy.ndarray]
            If :param: samples is a single angle or an array-like object of size 1,
                a single float with the log-likelihood is returned.
            Otherwise, a numpy.ndarray of log-likelihoods with the same shape as
                :param: samples is returned.
            If angle <= 0 or angle >= pi/2 => log-likelihood = -numpy.inf
        """
        samples_array = np.array(samples)
        mask = (samples_array > 0) & (samples_array < np.pi/2)

        likelihoods = np.empty_like(samples_array)
        if likelihoods.ndim == 0:
            likelihoods = np.array(-np.inf)
        else:
            likelihoods[:] = -np.inf
        likelihoods[mask] = np.log(np.sin(2*samples_array[mask]))

        if likelihoods.size == 1:
            likelihoods = likelihoods.item()

        return likelihoods


###################################################
class LogAngleDistribution(ProbabilityDistribution):
    """Probability distribution of prior for log(meteoroid impact angle) with angle in radians.

    Log is the natural logarithm.
    CDF(log(theta)) = sin(theta)^2, PDF(log(theta)) = theta * sin(2*theta), 0 <= theta <= pi/2

    Paremters
    ----------
    seed : int
        seed for the numpy.random.Generator instance
    """

    def __init__(self, seed):
        super().__init__(seed)
        self._log_pi_half = np.log(np.pi) - np.log(2)

    ### ##################################
    def sample(self, n_samples=1):
        """Generate samples from the log(angle) distribution

        Parameters
        ----------
        n_samples : Union[int, array-like], optional
            number of samples or shape of array with random samples
            default : 1

        Returns
        -------
        samples : Union[float, numpy.ndarray]
            long(angles); angles in radians

            By default, a single sample is returned as a float.
            If :param: n_samples > 1 or is array-like with size > 1,
                a numpy.ndarray of samples with the specified shape is returned.
        """
        uniform_samples = self.rng_.uniform(size=n_samples)
        if uniform_samples.size == 1:
            uniform_samples = uniform_samples.item()
        samples = np.log(np.arcsin(np.sqrt(uniform_samples)))

        return samples

    ### ##################################
    def log_likelihood(self, samples):
        """Calculate log likelihood of samples; log is the natural logarithm

        Parameters
        ----------
        samples : Union[int, float, array-like]
            log(angles) for which the log likelihood shall be calculated; angles in radians

        Returns
        -------
        likelihoods : Union[float, numpy.ndarray]
            If :param: samples is a single number or an array-like object of size 1,
                a single float with the log-likelihood is returned.
            Otherwise, a numpy.ndarray of log-likelihoods with the same shape as
                :param: samples is returned.
            For distributions with compact support, if likelihood = 0 => log-likelihood = -numpy.inf
        """
        samples_array = np.array(samples)
        mask = samples_array < self._log_pi_half

        likelihoods = np.empty_like(samples_array)
        if likelihoods.ndim == 0:
            likelihoods = np.array(-np.inf)
        else:
            likelihoods[:] = -np.inf
        likelihoods[mask] = np.log(
            np.sin(2*np.exp(samples_array[mask]))) + samples_array[mask]

        if likelihoods.size == 1:
            likelihoods = likelihoods.item()

        return likelihoods


###################################################
class ParetoDistribution(ProbabilityDistribution):
    """Pareto distribution [https://en.wikipedia.org/wiki/Pareto_distribution]

    If the histogram in log-space looks like an exponential (i.e. a straight line if the bin counts
    are also in log-space) with a negative slope, that's a Pareto distribution.

    Parameters
    ----------
    minimum : float
        min value for the distribution

    loglog_slope : float
        slope of the histogram as described above
        loglog_slope < 0

    seed : int
        seed for the numpy.random.Generator instance
    """

    def __init__(self, minimum, loglog_slope, seed):
        if not isinstance(minimum, (int, float)):
            raise TypeError("minimum must be a float")
        if minimum <= 0:
            raise ValueError("minimum must be positive")
        if not isinstance(loglog_slope, (int, float)):
            raise TypeError("loglog_slope must be a float")
        if loglog_slope >= 0:
            raise ValueError("loglog_slope must be negative")

        super().__init__(seed)
        self.a = -loglog_slope
        self.m = minimum
        self.log_y0 = np.log(self.a) + self.a*np.log(self.m)

    ### ##################################
    def sample(self, n_samples=1):
        samples = self.m * (self.rng_.pareto(self.a, n_samples) + 1)
        if samples.size == 1:
            samples = samples.item()

        return samples

    ### ##################################
    def log_likelihood(self, samples):
        log_samples_array = np.array(samples)
        mask = log_samples_array >= self.m
        log_samples_array[mask] = np.log(log_samples_array[mask])

        likelihoods = np.empty_like(log_samples_array)
        if likelihoods.ndim == 0:
            likelihoods = np.array(-np.inf)
        else:
            likelihoods[:] = -np.inf
        likelihoods[mask] = self.log_y0 - \
            (self.a + 1) * log_samples_array[mask]

        if likelihoods.size == 1:
            likelihoods = likelihoods.item()

        return likelihoods


###################################################
class LogParetoDistribution(ParetoDistribution):
    """Log(samples) where samples have a Pareto distribution; log is the natural logarithm.

    Pareto distribution: [https://en.wikipedia.org/wiki/Pareto_distribution]

    If the histogram in log-space looks like an exponential (i.e. a straight line if the bin counts
    are also in log-space) with a negative slope, that's a Pareto distribution.

    Parameters
    ----------
    minimum : float
        min value for the underlying Pareto distribution
        Minimum sample generated will be log(mininum)

    loglog_slope : float
        slope of the histogram as described above
        loglog_slope < 0

    seed : int
        seed for the numpy.random.Generator instance
    """

    def __init__(self, minimum, loglog_slope, seed):
        super().__init__(minimum, loglog_slope, seed)
        self.log_m = np.log(self.m)

    ### ##################################
    def sample(self, n_samples=1):
        samples = self.rng_.exponential(
            1 / self.a, size=n_samples) + self.log_m
        if samples.size == 1:
            samples = samples.item()

        return samples

    ### ##################################
    def log_likelihood(self, samples):
        samples_array = np.array(samples)
        mask = samples_array >= self.log_m

        likelihoods = np.empty_like(samples_array)
        if likelihoods.ndim == 0:
            likelihoods = np.array(-np.inf)
        else:
            likelihoods[:] = -np.inf
        likelihoods[mask] = self.log_y0 - self.a * samples_array[mask]

        if likelihoods.size == 1:
            likelihoods = likelihoods.item()

        return likelihoods


###################################################
class CompositeParetoDistribution(ProbabilityDistribution):
    """Pareto-like distribution with multiple sections where slope is different

    Pareto distribution: [https://en.wikipedia.org/wiki/Pareto_distribution]

    If the histogram in log-space with log bin counts looks like a piecewise linear function,
    that's the distribution for it.

    Parameters
    ----------
    minima : array-like
        latice points of the piecewise linear function described above
        len(minima) > 1; use ParetoDistribution instead if len(minima) = 1
        minima > 0

    loglog_slopes : array-like
        slopes of piecewise linear function described above
        slopes < 0

    seed : int
        seed for the numpy.random.Generator instance
    """

    def __init__(self, minima, loglog_slopes, seed):
        super().__init__(seed)

        self.minima = np.array(minima)
        if self.minima.size < 2:
            raise ValueError(
                "minima must have length >= 2. For lengh 1, use ParetoDistribution class")
        if self.minima.ndim != 1:
            raise ValueError("minima must be a one-dimensional array")
        if not (np.diff(self.minima) > 0).all():
            raise ValueError("minima must be sorted in ascending order")

        self.neg_slopes = -np.array(loglog_slopes)
        if self.neg_slopes.shape != self.minima.shape:
            raise ValueError(
                "minima and loglog_slopes must have the same shape")
        if not (self.neg_slopes > 0).all():
            raise ValueError("loglog_slopes must be negative")

        self.minima = np.hstack((self.minima, [np.inf]))
        self.log_yi = np.cumsum([0] + [(self.neg_slopes[i] - self.neg_slopes[i-1])
                                * np.log(self.minima[i]) for i in range(1, self.neg_slopes.size)])
        y = np.exp(self.log_yi)

        log_y0 = -np.log(sum(y[i] / self.neg_slopes[i] * (self.minima[i]**-self.neg_slopes[i] -
                         self.minima[i+1]**-self.neg_slopes[i]) for i in range(self.neg_slopes.size)))
        self.log_yi += log_y0

    ### ##################################
    def sample(self, n_samples=1):
        """TODO: This is incorrect (check histogram)"""
        samples = self.minima[0] * \
            (self.rng_.pareto(self.neg_slopes[0], n_samples) + 1)
        for i in range(1, self.minima.size - 1):
            mask = samples > self.minima[i]
            num_replace = mask.sum()
            if num_replace == 0:
                break
            samples[mask] = self.minima[i] * \
                (self.rng_.pareto(self.neg_slopes[i], num_replace) + 1)

        if samples.size == 1:
            samples = samples.item()

        return samples

    ### ##################################
    def log_likelihood(self, samples):
        samples_array = np.array(samples)
        likelihoods = np.empty_like(samples_array)
        if likelihoods.ndim == 0:
            likelihoods = np.array(-np.inf)
        else:
            likelihoods[:] = -np.inf

        for i in range(self.neg_slopes.size):
            mask = (self.minima[i] <= samples_array) & (
                samples_array < self.minima[i+1])
            likelihoods[mask] = self.log_yi[i] - \
                (self.neg_slopes[i] + 1) * np.log(samples_array[mask])

        if likelihoods.size == 1:
            likelihoods = likelihoods.item()

        return likelihoods


###################################################
class LogCompositeParetoDistribution(CompositeParetoDistribution):
    """Log(samples) where samples are distributed as described in CompositeParetoDistribution class

    Pareto distribution: [https://en.wikipedia.org/wiki/Pareto_distribution]

    If the histogram with log bin counts looks like a piecewise linear function,
    that's the distribution for it.

    Parameters
    ----------
    minima : array-like
        latice points of the piecewise linear function described above
        len(minima) > 1; use ParetoDistribution instead if len(minima) = 1
        minima > 0

    loglog_slopes : array-like
        slopes of piecewise linear function described above
        slopes < 0

    seed : int
        seed for the numpy.random.Generator instance
    """

    def __init__(self, minima, loglog_slopes, seed):
        super().__init__(minima, loglog_slopes, seed)
        self.log_minima = np.log(self.minima)

    ### ##################################
    def sample(self, n_samples=1):
        """TODO: This is incorrect (check histogram)"""
        samples = self.rng_.exponential(
            1 / self.neg_slopes[0], n_samples) + self.log_minima[0]
        for i in range(1, self.log_minima.size - 1):
            mask = samples > self.log_minima[i]
            num_replace = mask.sum()
            if num_replace == 0:
                break
            samples[mask] = self.rng_.exponential(
                1 / self.neg_slopes[i], num_replace) + self.log_minima[i]

        if samples.size == 1:
            samples = samples.item()

        return samples

    ### ##################################
    def log_likelihood(self, samples):
        samples_array = np.array(samples)
        likelihoods = np.empty_like(samples_array)
        if likelihoods.ndim == 0:
            likelihoods = np.array(-np.inf)
        else:
            likelihoods[:] = -np.inf

        for i in range(self.neg_slopes.size):
            mask = (self.log_minima[i] <= samples_array) & (
                samples_array < self.log_minima[i+1])
            likelihoods[mask] = self.log_yi[i] - \
                self.neg_slopes[i] * samples_array[mask]

        if likelihoods.size == 1:
            likelihoods = likelihoods.item()

        return likelihoods


###################################################
class UniformDistribution(ProbabilityDistribution):
    """Uniform distribution [https://en.wikipedia.org/wiki/Uniform_distribution_(continuous)]

    Parameters
    ----------
    mimimum : float
        lower bound for the distribution

    maximum : float
        upper bound for the distribution
        maximum > minimum

    seed : int
        seed for the numpy.random.Generator instance
    """

    def __init__(self, minimum, maximum, seed):
        super().__init__(seed)
        if minimum >= maximum:
            raise ValueError("minimum must be smaller than maximum")

        self.min = minimum
        self.max = maximum
        self._log_likelihood = -np.log(self.max - self.min)

    ### ##################################
    def sample(self, n_samples=1):
        samples = self.rng_.uniform(self.min, self.max, n_samples)
        if isinstance(n_samples, int) and n_samples == 1:
            samples = samples[0]
        return samples

    ### ##################################
    def log_likelihood(self, samples):
        samples_array = np.array(samples)
        mask = (samples_array >= self.min) & (samples_array <= self.max)

        likelihoods = np.empty_like(samples_array)
        if likelihoods.ndim == 0:
            likelihoods = np.array(-np.inf)
        else:
            likelihoods[:] = -np.inf
        likelihoods[mask] = self._log_likelihood

        if likelihoods.size == 1:
            likelihoods = likelihoods.item()

        return likelihoods


###################################################
class NormalDistribution(ProbabilityDistribution):
    """Normal distribution [https://en.wikipedia.org/wiki/Normal_distribution]

    Parameters
    ----------
    mu : float
        mean of the distribution

    sigma : float
        standard deviation of the distribution

    seed : int
        seed for the numpy.random.Generator instance
    """

    def __init__(self, mu, sigma, seed):
        super().__init__(seed)
        assert sigma > 0

        self.mu = mu
        self.sigma = sigma
        self.log_y0 = -np.log(sigma) - np.log(2*np.pi) / 2

    ### ##################################
    def sample(self, n_samples=1):
        samples = self.rng_.normal(self.mu, self.sigma, n_samples)
        if isinstance(n_samples, int) and n_samples == 1:
            samples = samples[0]
        return samples

    ### ##################################
    def log_likelihood(self, samples):
        likelihood = -np.square((samples - self.mu) /
                                self.sigma) / 2 + self.log_y0
        if likelihood.size == 1:
            likelihood = likelihood.item()

        return likelihood


###################################################
class LogNormalDistribution(NormalDistribution):
    """Log-normal distribution [https://en.wikipedia.org/wiki/Log-normal_distribution]

    exp(samples) where samples are normally distributed

    Parameters
    ----------
    mu : float
        mean of the underlying normal distribution

    sigma : float
        standard deviation of the underlying normal distribution

    seed : int
        seed for the numpy.random.Generator instance
    """

    ### ##################################
    def sample(self, n_samples=1):
        samples = self.rng_.lognormal(self.mu, self.sigma, n_samples)
        if isinstance(n_samples, int) and n_samples == 1:
            samples = samples[0]
        return samples

    ### ##################################
    def log_likelihood(self, samples):
        log_samples_array = np.array(samples)
        mask = log_samples_array > 0
        log_samples_array[mask] = np.log(log_samples_array[mask])

        likelihoods = np.empty_like(log_samples_array)
        if likelihoods.ndim == 0:
            likelihoods = np.array(-np.inf)
        else:
            likelihoods[:] = -np.inf
        likelihoods[mask] = -np.square((log_samples_array[mask] - self.mu) / self.sigma) / 2 \
            + self.log_y0 - log_samples_array[mask]

        if likelihoods.size == 1:
            likelihoods = likelihoods.item()

        return likelihoods


###################################################
class MultivariateNormalDistribution(ProbabilityDistribution):
    """Multivariate normal distribution
    [https://en.wikipedia.org/wiki/Multivariate_normal_distribution]

    Parameters
    ----------
    mu : array-like
        mean of the distribution

    cov : array-like
        2D covariance matrix of the distribution
        must be strictly positive definite

    seed : int
        seed for the numpy.random.Generator instance
    """

    def __init__(self, mu, cov, seed):
        super().__init__(seed)

        self.mu = np.array(mu)
        self.cov = np.array(cov)

        if self.mu.ndim != 1:
            raise ValueError("mu must be a one-dimensional vector")
        if self.mu.size == 1:
            raise ValueError(
                "mu must have size >= 2; use NormalDistribution instead")
        if self.cov.ndim != 2:
            raise ValueError("cov must be a two-dimensional matrix")
        if self.cov.shape != (self.mu.size, self.mu.size):
            raise ValueError("cov must have shape (len(mu), len(mu))")

        eigvals = np.linalg.eigvals(self.cov)
        if not (eigvals > 0).all():
            raise ValueError("cov must be strictly positive definite")
        self.inv_cov = np.linalg.inv(self.cov)

        self.log_y0 = (-np.log(eigvals).sum() -
                       self.mu.size * np.log(2*np.pi)) / 2

    ### ##################################
    def sample(self, n_samples=1):
        samples = self.rng_.multivariate_normal(
            self.mu, self.cov, n_samples, check_valid='raise')
        if samples.size == self.mu.size:
            samples = samples.flatten()

        return samples

    ### ##################################
    def log_likelihood(self, samples):
        samples_array = np.array(samples)
        if samples_array.shape[-1] != self.mu.size:
            raise ValueError(
                "last dim of samples must have same size as self.mu")

        if samples.ndim == 1:
            x_minus_mu = samples_array - self.mu
        else:
            x_minus_mu = samples_array - \
                np.repeat([self.mu], np.prod(samples_array.shape[:-1]),
                          axis=0).reshape(samples_array.shape)

        likelihood = self.log_y0 - \
            np.diag(x_minus_mu.dot(self.inv_cov).dot(x_minus_mu)) / 2

        if likelihood.size == 1:
            likelihood = likelihood.item()

        return likelihood


###################################################
class FlatPrior(ProbabilityDistribution):
    def sample(self, n_samples=1):
        raise ValueError("FlatPrior distribution cannot generate samples")

    def log_likelihood(self, samples):
        samples_array = np.array(samples)
        if samples_array.size == 1:
            return 0
        return np.zeros_like(samples_array)


###################################################
class CombinedDistributions(ProbabilityDistribution):
    def __init__(self, *distributions, names):
        if len(distributions) < 2:
            raise ValueError("At least two distributions have to be provided.")
        if not all(isinstance(d, ProbabilityDistribution) for d in distributions):
            raise TypeError(
                "all distributions must be ProbabilityDistribution instances")

        super().__init__(0)
        self.distributions = distributions
        self.names = names

    def sample(self, n_samples=1):
        return [d.sample(n_samples) for d in self.distributions]

    def log_likelihood(self, samples):
        if len(samples) != len(self.distributions):
            raise ValueError("samples must be a list with the same length as the number of "
                             + "distributions inside this instance of CombinedDistributions")

        return sum(d.log_likelihood(samples[i]) for i, d in enumerate(self.distributions))


if __name__ == "__main__":
    uniformDistribution = UniformDistribution(
        10, 1000, int(time.time()))

    print(uniformDistribution.sample(10))
