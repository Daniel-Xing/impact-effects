
import time
from impactEffects.functions.function import cal_lratio, cal_mratio, cal_trot_change
from impactEffects.functions.function_population import cal_lratio_population, cal_mratio_population, cal_pratio_population, cal_themal_population, cal_trot_change_population, cal_vration_population
from impactEffects.instances import TargetClass
from impactEffects.instances.Impactor_population import ImpactorPopulation
from impactEffects.instances.distribution import UniformDistribution
from impactEffects.core.core_population import *


def test_cal_themal_population():
    uniformDistribution = UniformDistribution(
        10, 1000, int(time.time()))

    # print(uniformDistribution.sample(10))

    impactor = ImpactorPopulation(diameter=uniformDistribution,
                                  density=1000,
                                  velocity=1000,
                                  theta=45)
    targets = TargetClass.Target(depth=0, distance=75, density=2500)

    res = cal_themal_population(impactor, targets)
    for k in list(res.keys()):
        print(k, " ", res[k])


def test_cal_lratio_population():
    uniformDistribution = UniformDistribution(
        10, 1000, int(time.time()))

    # print(uniformDistribution.sample(10))

    impactor = ImpactorPopulation(diameter=uniformDistribution,
                                  density=1000,
                                  velocity=1000,
                                  theta=45)
    targets = TargetClass.Target(depth=0, distance=75, density=2500)

    res = cal_lratio_population(impactor, targets)
    print(res)


def test_cal_pratio_population():
    uniformDistribution = UniformDistribution(
        10, 1000, int(time.time()))

    # print(uniformDistribution.sample(10))

    impactor = ImpactorPopulation(diameter=uniformDistribution,
                                  density=1000,
                                  velocity=1000,
                                  theta=45)
    targets = TargetClass.Target(depth=0, distance=75, density=2500)

    res = cal_pratio_population(impactor, targets)
    print(res)


def test_cal_trot_change_population():
    uniformDistribution = UniformDistribution(
        10, 1000, int(time.time()))

    # print(uniformDistribution.sample(10))

    impactor = ImpactorPopulation(diameter=uniformDistribution,
                                  density=1000,
                                  velocity=1000,
                                  theta=45)
    targets = TargetClass.Target(depth=0, distance=75, density=2500)

    res = cal_trot_change_population(impactor, targets)
    print(res)


def test_cal_vRation_population():
    uniformDistribution = UniformDistribution(
        10, 1000, int(time.time()))

    # print(uniformDistribution.sample(10))

    impactor = ImpactorPopulation(diameter=uniformDistribution,
                                  density=1000,
                                  velocity=1000,
                                  theta=45)
    targets = TargetClass.Target(depth=0, distance=75, density=2500)

    res = cal_vration_population(impactor, targets)
    print(res)


def test_cal_mratio_population():
    uniformDistribution = UniformDistribution(
        10, 1000, int(time.time()))

    # print(uniformDistribution.sample(10))

    impactor = ImpactorPopulation(diameter=uniformDistribution,
                                  density=1000,
                                  velocity=1000,
                                  theta=45)
    targets = TargetClass.Target(depth=0, distance=75, density=2500)

    res = cal_mratio_population(impactor, targets)
    print(res)
