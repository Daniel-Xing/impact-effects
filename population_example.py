import time
import numpy as np
from impactEffects.functions.function_population import *
from impactEffects.instances import TargetClass
from impactEffects.instances.Impactor_population import ImpactorPopulation
from impactEffects.instances.distribution import UniformDistribution
from impactEffects.core.core_population import *
from impactEffects.utils.print_population import *


def case1():
    uniformDistribution = UniformDistribution(
        10, 100, int(time.time()))

    impactor = ImpactorPopulation(diameter=uniformDistribution,
                                  density=1000,
                                  velocity=1000,
                                  theta=45)
    targets = TargetClass.Target(depth=0, distance=75, density=2500)

    trot_change = cal_trot_change_population(impactor=impactor, target=targets)
    lratio = cal_lratio_population(impactor=impactor, target=targets)
    pratio = cal_pratio_population(impactor=impactor, target=targets)
    mratio = cal_mratio_population(impactor=impactor, target=targets)
    vratio = cal_vration_population(impactor=impactor, target=targets)

    print(Global_change(vratio, mratio, lratio, trot_change, pratio))


if __name__ == "__main__":
    case1()
