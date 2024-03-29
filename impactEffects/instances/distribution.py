import os
import datetime
import time
import numpy as np


class ProbabilityDistribution:
    """Abstract base class for all probability distributions

    Parameters
    ---------
    seed : int
        seed for the numpy.random.Generator instance
    """

    def __init__(self, seed):
        self.rng_ = np.random.default_rng(seed)

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

    def log_likelihood(self, samples):
        """Calculate log likelihood of samples; log is the natural logarithm

        Parameters
        ----------
        samples : Union[int, float, array-like]
            samples for which the log likelihood shall be calculated

        Returns
        -------
        likelihoods : Union[float, numpy.ndarray]
            If :param: samples is a single number
            or a size-1 array-like object,
            a single float with the log-likelihood is returned.
            Otherwise, a numpy.ndarray of
            log-likelihoods with the same shape as
                :param: samples is returned.
            For distributions with compact support,
            if likelihood = 0 => log-likelihood = -numpy.inf
        """
        raise NotImplementedError(
            "log_likelihood function must be implemented"
        )


class UniformDistribution(ProbabilityDistribution):
    """Uniform distribution
[https://en.wikipedia.org/wiki/Uniform_distribution_(continuous)]

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

    def sample(self, n_samples=1):
        samples = self.rng_.uniform(self.min, self.max, n_samples)
        if isinstance(n_samples, int) and n_samples == 1:
            samples = samples[0]
        return samples
