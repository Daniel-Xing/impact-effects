from src.Targets import *


class Impactor:

    """
    __init__
    """

    def __init__(self, diameter, density, velocity, theta, type):
        self.pdiameter = diameter
        self.density = density
        self.velocity = velocity
        self.theta = theta
        self.type = type

        self.mass = -1
        self.energy0 = -1
        self.energy0_megatons = -1

        return

    # TODO: add Checker

    def calculate_mass(self):
        self.mass = ((PI * self.pdiameter ** 3) / 6) * self.density

    def calculate_energy0(self):
        if self.mass < 0:
            self.calculate_mass()

        self.energy0 = 0.5 * self.mass * (self.velocity * 1000) ** 2

    def calcualte_energy0_megatons(self):
        if self.energy0 < 0:
            self.calculate_energy0()

        self.energy0_megatons = self.energy0 * joules2megatones

    def get_energy0(self) -> float:
        if self.energy0 < 0:
            self.calculate_energy0()
        return self.energy0

    def get_energy0_megatons(self) -> float:
        if self.energy0_megatons < 0:
            self.calcualte_energy0_megatons()

        return self.calcualte_energy0_megatons

    def get_pdiameter(self) -> float:
        return self.pdiameter

    def get_density(self) -> float:
        return self.density

    def get_velocity(self) -> float:
        return self.velocity

    def get_type(self) -> int:
        return self.type

    def get_mass(self) -> float:
        if self.mass < 0:
            self.calculate_mass()

        return self.mass
