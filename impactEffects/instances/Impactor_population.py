# -*- encoding: utf-8 -*-
"""
Filename         :Impactor_population.py
Description      :
Time             :2022/07/10 09:38:36
Author           :daniel
Version          :1.0
"""

from impactEffects.instances.ImpactorClass import Impactor
from impactEffects.instances.distribution import *
from numpy import Inf
from impactEffects.core.config import *
from impactEffects.instances.checker import numeric_checker


MIN_SAMPLE_NUM = 1
MAX_SAMPLE_NUM = 1e8


class ImpactorPopulation:
    """Example for supporting impactor population,
    only type of diameter is ProbabilityDistribution

    Parameters
    ---------
    diameter : ProbabilityDistribution
        diameter of impactor
    density: int
    """

    def __init__(
        self,
        diameter: ProbabilityDistribution,
        density: int,
        velocity: int,
        theta: int,
        velocity_upper: int = 3e5,
        velocity_lower: int = 0,
        theta_upper: int = 90,
        theta_lower: int = 0,
        density_upper: int = Inf,
        density_lower: int = 0,
        diameterNumber: int = 100,
    ):
        # set velocity upper and lower bounds
        self.velocity_upper = velocity_upper
        self.velocity_lower = velocity_lower
        # set theta upper and lower bounds
        self.theta_upper = theta_upper
        self.theta_lower = theta_lower
        # set pdiameter upper and lower bounds
        # set density upper and lower bounds
        self.density_upper = density_upper
        self.density_lower = density_lower

        # using setter function to set the values
        self.set_pdiameter(diameter, diameterNumber)
        self.set_density(density)
        self.set_theta(theta)
        self.set_velocity(velocity)

        self.mass = None
        self.energy0 = None
        self.energy0_megatons = None
        self.rec_time = None

        self.altitudeBurst = 0

        self.instances = []
        for diamter in self.pdiameter:
            # print("aaa", diamter, "type: ", type(diamter))
            self.instances.append(
                Impactor(
                    diameter=diamter,
                    density=self.density,
                    velocity=self.velocity,
                    theta=self.theta,
                )
            )

        return

    # define setter function for pdiameter
    def set_pdiameter(self, pdiameter, pdiameterNumber):
        """set after check

        Args:
            pdiameter (_type_): _description_
        """
        if type(pdiameterNumber) != int:
            raise TypeError("pdiameterNumber must be a numeric value, int.")

        if (
            pdiameterNumber < MIN_SAMPLE_NUM
            or pdiameterNumber > MAX_SAMPLE_NUM
        ):
            raise ValueError(
                "pdiameterNumber must be\
                    within the bounds: {} < density < {}".format(
                    MIN_SAMPLE_NUM, MAX_SAMPLE_NUM
                )
            )

        try:
            pdiameter.sample(pdiameterNumber)
        except Exception:
            raise NotImplementedError("no sample function found in pdiameter")

        self.pdiameter = pdiameter.sample(pdiameterNumber)

    # define setter function for density
    def set_density(self, density):
        # check if the value is numeric
        if not numeric_checker(density):
            raise TypeError("density must be a numeric value, float or int.")
        # check if density is within the bounds
        if density > self.density_upper or density < self.density_lower:
            raise ValueError(
                "density must be within the bounds: {} < density < {}".format(
                    self.density_lower, self.density_upper
                )
            )
        self.density = density

    # define setter function for velocity
    def set_velocity(self, velocity):
        # check if the value is numeric
        if not numeric_checker(velocity):
            raise TypeError("velocity must be a numeric value, float or int.")
        # check if velocity is within the bounds
        if velocity > self.velocity_upper or velocity < self.velocity_lower:
            raise ValueError(
                "velocity must be\
                    within the bounds: {} < velocity < {}".format(
                    self.velocity_lower, self.velocity_upper
                )
            )
        self.velocity = velocity

    # define setter function for theta
    def set_theta(self, theta):
        # check if the value is numeric
        if not numeric_checker(theta):
            raise TypeError("theta must be a numeric value, float or int.")
        # check if theta is within the bounds
        if theta > self.theta_upper or theta < self.theta_lower:
            raise ValueError(
                "theta must be within the bounds: {} < theta < {}".format(
                    self.theta_lower, self.theta_upper
                )
            )
        self.theta = theta

    def get_energy0(self) -> float:
        if self.energy0 is None:
            self.calculate_energy0()
        return self.energy0

    def get_energy0_megatons(self) -> float:
        if self.energy0_megatons is None:
            self.calcualte_energy0_megatons()

        return self.energy0_megatons

    def get_rec_time(self):
        if self.rec_time is None:
            self.calculate_recTime()
        return self.rec_time

    def get_pdiameter(self) -> float:
        return self.pdiameter

    def get_density(self) -> float:
        return self.density

    def get_velocity(self) -> float:
        return self.velocity

    def get_mass(self) -> float:
        if self.mass is None:
            self.calculate_mass()

        return self.mass

    def get_theta(self):
        return self.theta

    # calculate the mass of the impactor
    def calculate_mass(self):
        self.mass = ((PI * self.pdiameter ** 3) / 6) * self.density

    # calculate the time of the impact
    def calculate_energy0(self):
        if self.mass is None:
            self.calculate_mass()

        self.energy0 = 0.5 * self.mass * (self.velocity * 1000) ** 2

    # calculate the time of the impact
    def calcualte_energy0_megatons(self):
        if self.energy0 is None:
            self.calculate_energy0()

        self.energy0_megatons = self.energy0 * joules2megatones

    # calculate the time of the impact
    def calculate_recTime(self):
        mass = self.get_mass()

        # Compute the recurrence interval for this energy impact
        # New model (after Bland and Artemieva (2006) MAPS 41 (607-621).
        if mass < 3:
            self.rec_time = 10 ** (-4.568) * mass ** 0.480
        elif mass < 1.7e10:
            self.rec_time = 10 ** (-4.739) * mass ** 0.926
        elif mass < 3.3e12:
            self.rec_time = 10 ** (0.922) * mass ** 0.373
        elif mass < 8.4e14:
            self.rec_time = 10 ** (-0.086) * mass ** 0.454
        else:
            self.rec_time = 10 ** (-3.352) * mass ** 0.672

        energy0_megatons = self.get_energy0_megatons()
        self.rec_time = max(self.rec_time, 110 * energy0_megatons ** 0.77)

    def Instances(self):
        """Now, only support diamater
        """
        return self.instances


if __name__ == "__main__":
    uniformDistribution = UniformDistribution(10, 1000, int(time.time()))

    # print(uniformDistribution.sample(10))

    impactor = ImpactorPopulation(
        diameter=uniformDistribution, density=1000, velocity=1000, theta=45
    )
    print(impactor.get_pdiameter())
    print(impactor.Instances())
