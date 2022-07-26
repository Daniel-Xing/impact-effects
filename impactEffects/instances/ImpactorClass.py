# -*- encoding: utf-8 -*-
"""
Filename         :Impactor.py
Description      :
Time             :2022/07/10 09:38:24
Author           :daniel
Version          :1.0
"""

from numpy import Inf
from impactEffects.core.config import *
from impactEffects.instances.checker import numeric_checker


class Impactor:
    """
    __init__
    """

    def __init__(
        self,
        diameter,
        density,
        velocity,
        theta,
        velocity_upper=3e5,
        velocity_lower=0,
        theta_upper=90,
        theta_lower=0,
        diameter_upper=Inf,
        diameter_lower=0,
        density_upper=Inf,
        density_lower=0,
    ):
        # set velocity upper and lower bounds
        self.velocity_upper = velocity_upper
        self.velocity_lower = velocity_lower
        # set theta upper and lower bounds
        self.theta_upper = theta_upper
        self.theta_lower = theta_lower
        # set pdiameter upper and lower bounds
        self.diameter_upper = diameter_upper
        self.diameter_lower = diameter_lower
        # set density upper and lower bounds
        self.density_upper = density_upper
        self.density_lower = density_lower

        # self.pdiameter = diameter
        # self.density = density
        # self.velocity = velocity
        # self.theta = theta
        # self.ttype = ttype

        # using setter function to set the values
        self.set_pdiameter(diameter)
        self.set_density(density)
        self.set_theta(theta)
        self.set_velocity(velocity)

        self.mass = None
        self.energy0 = None
        self.energy0_megatons = None
        self.rec_time = None

        return

    # define setter function for pdiameter
    def set_pdiameter(self, pdiameter):
        # check if the value is numeric
        if not numeric_checker(pdiameter):
            raise TypeError(
                "pdiameter must be a numeric value, float or int."
            )
        # check if pdiameter is within the bounds
        if (
            pdiameter > self.diameter_upper
            or pdiameter < self.diameter_lower
        ):
            raise ValueError(
                "pdiameter must be within the bounds: {} < pdiameter < {}".
                format(
                    self.diameter_lower, self.diameter_upper
                )
            )
        self.pdiameter = pdiameter

    # define setter function for density
    def set_density(self, density):
        # check if the value is numeric
        if not numeric_checker(density):
            raise TypeError(
                "density must be a numeric value, float or int."
            )
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
            raise TypeError(
                "velocity must be a numeric value, float or int."
            )
        # check if velocity is within the bounds
        if velocity > self.velocity_upper or velocity < self.velocity_lower:
            raise ValueError(
                "velocity must be within the bounds: {} < velocity < {}".
                format(self.velocity_lower, self.velocity_upper
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


if __name__ == "__main__":
    impactor = Impactor(diameter=111, density=111, velocity=111, theta=45)
    print(impactor.get_pdiameter())
