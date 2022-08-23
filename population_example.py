import time
import numpy as np
from impactEffects.functions.function_population import *
from impactEffects.instances import TargetClass
from impactEffects.instances.Impactor_population import ImpactorPopulation
from impactEffects.instances.distribution import UniformDistribution
from impactEffects.core.core_population import *
from impactEffects.utils.print_population import *
from impact_example import get_input


def INPUT():
    while True:
        min_pdiameter = float(
            input("please input min value of diameter of impactor: "))
        max_pdiameter = float(
            input("please input max value of diameter of impactor: "))
        diameterUnit = int(
            input("please input the unit of diameter: 1 for km, 2 for m "))
        # pdiameter = 1000

        pdensity = float(input("please input density(kg/m^3) of impactor: "))
        # pdensity = 3000

        v_input = float(input("please input the velocity of impactor: "))
        velocityUnits = int(
            input("please input the unit of velocity: 1 for km/s, 2 for mile/s ")
        )
        # v_input = 20

        theta = float(input("please input the theta(degrees) of impactor: "))
        # theta = 45

        tdensity = float(input("please input the density(kg/m^3) of target: "))
        # tdensity = 2500

        depth = float(input("please input the depth(meters): "))
        # depth = 0

        distance = float(input("please input the distance: "))
        distanceUnit = int(
            input("please input the unit of distance: 1 for km, 2 for m "))
        # distance = 100

        try:
            if diameterUnit == 1:
                min_pdiameter *= 1000
                max_pdiameter *= 1000
            elif diameterUnit == 2:
                pass
            else:
                raise Exception("diameter unit error")

            if velocityUnits == 1:
                pass
            elif velocityUnits == 2:
                v_input *= 1.61
            else:
                raise Exception("velocity unit error")

            if distanceUnit == 1:
                pass
            elif diameterUnit == 2:
                distance = distance * 1000
            else:
                raise Exception("distance unit error")

            uniformDistribution = UniformDistribution(
                min_pdiameter, max_pdiameter, int(time.time()))

            impactor = ImpactorPopulation(diameter=uniformDistribution,
                                          density=pdensity,
                                          velocity=v_input,
                                          theta=theta)
            targets = TargetClass.Target(
                depth=depth, distance=distance, density=tdensity)
            break
        except:
            print("Input error, please retry or exit.")
            retry = input("Do you want to retry?(0:false, 1:true)")
            if retry == "0":
                exit(0)
            elif retry == "1":
                continue
            else:
                print("error: input is not 0/1 .")
                exit(1)

    return impactor, targets


def simulator_population(impactor, targets):

    trot_change = cal_trot_change_population(impactor=impactor, target=targets)
    lratio = cal_lratio_population(impactor=impactor, target=targets)
    pratio = cal_pratio_population(impactor=impactor, target=targets)
    mratio = cal_mratio_population(impactor=impactor, target=targets)
    vratio = cal_vration_population(impactor=impactor, target=targets)

    print(Global_change(vratio, mratio, lratio, trot_change, pratio))


if __name__ == "__main__":
    impactor, targets = INPUT()
    simulator_population(impactor, targets)
