from tkinter.tix import InputOnly
import numpy as np
from sqlalchemy import false
from sympy import re
import impactEffects.instances.ImpactorClass
from impactEffects.functions import *
from impactEffects.functions.function import *
from impactEffects.instances import ImpactorClass, TargetClass
from impactEffects.utils.print import print_airblast, print_change, print_crater, print_ejecta, print_energy, print_recurrencetime, print_atmospheric_entry, print_seismic, print_thermal, print_tsunami


def get_input():
    while True:
        # pdiameter = float(input("please input diameter of impactor: "))
        # diameterUnit = int(
        #     input("please input the unit of diameter: 1 for km, 2 for m "))
        pdiameter = 18
        diameterUnit = 1

        # pdensity = float(input("please input density(kg/m^3) of impactor: "))
        pdensity = 2700

        # v_input = float(input("please input the velocity of impactor: "))
        # velocityUnits = int(
        #     input("please input the unit of velocity: 1 for km/s, 2 for mile/s ")
        # )
        v_input = 20
        velocityUnits = 1

        # theta = float(input("please input the theta(degrees) of impactor: "))
        theta = 60

        # tdensity = float(input("please input the density(kg/m^3) of target: "))
        tdensity = 1000

        # depth = float(input("please input the depth(meters): "))
        depth = 500

        # distance = float(input("please input the distance: "))
        # distanceUnit = int(
        #     input("please input the unit of distance: 1 for km, 2 for m "))
        distance = 200
        distanceUnit = 1

        try:
            if diameterUnit == 1:
                pdiameter *= 1000
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

            impactor = impactEffects.instances.ImpactorClass.Impactor(
                diameter=pdiameter, density=pdensity, velocity=v_input, theta=theta
            )
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


def simulateImpactor(impartor: Impactor, targets: Target):

    # cal_energy
    energy_disc, rec_disc, change_disc, atmos_disc, crater_disc, eject_disc, themal_disc, seismic_disc, ejecta_disc, airblast_disc, tsunami_disc = \
        "", "", "", "", "", "", "", "", "", "", ""
    _kinetic_energy = kinetic_energy(impactor)
    _kinetic_energy_megatons = kinetic_energy_megatons(impactor)
    energy_disc = print_energy(_kinetic_energy, _kinetic_energy_megatons)

    _rec_time = rec_time(impactor)
    # print(_rec_time)
    rec_disc = print_recurrencetime(_rec_time)

    # atmospheric_entry
    collins_iFactor, _av, _rStrength = iFactor(impactor, targets)
    # print(collins_iFactor)

    altitudeBU, altitudeBurst, dispersion, energy_surface, energy_megatons = 0, 0, 0, 0, 0
    if collins_iFactor >= 1:
        velocity = burst_velocity_at_zero(impactor, targets)
    else:
        altitudeBU = altitude_of_breakup(impactor, targets)
        # vBU = velocity_at_breakup(impactor, targets)

        # lDisper = dispersion_length_scale(impactor, targets)

        altitudeBurst = airburst_altitude(impactor, targets)

        velocity = brust_velocity(impactor, targets)

        dispersion = dispersion_of_impactor(impactor, targets)

    lratio, pratio = fraction_of_momentum(impactor, targets)

    trot_change = cal_trot_change(impactor, targets)
    # energy_atmosphere = cal_energy_atmosphere(impactor, targets)
    # energy_blast, energy_surface = cal_energy_blast_surface(impactor, targets)

    # mwater = cal_mass_of_water(impactor, targets)
    vseafloor = cal_velocity_projectile(impactor, targets)
    print("vseafloor", vseafloor)
    # energy_seafloor = cal_energy_at_seafloor(impactor, targets)
    # delta = cal_ePIcentral_angle(targets)
    # end_cal_energy

    # find_crater
    # Cd, beta = cal_scaling_diameter_constant(target=targets)
    # anglefac = cal_anglefac(impactor)

    wdiameter = 0
    if targets.depth != 0:
        wdiameter = cal_wdiameter(impactor, targets)

    Dtr = cal_transient_crater_diameter(impactor, targets)

    depthtr = cal_depthr(impactor, targets)

    cdiameter = cal_cdiamater(impactor, targets)
    # print("-----------------cal_cdiameter:", cdiameter)

    depthfr = cal_depthfr(impactor, targets)
    brecciaThickness = cal_brecciaThickness(impactor, targets)

    vCrater, vRatio = cal_vCrater_vRation(impactor, targets)

    vMelt = cal_vMelt(impactor, targets)

    mratio, mcratio = cal_mratio_and_mcratio(impactor, targets)
    # end find_crater

    change_disc = print_change(vRatio, mratio, lratio, trot_change, pratio)

    energy_megatons = energy_surface / (4.186 * 10**15)
    if impactor.get_mass() <= 1.5707963e12:
        atmos_disc = print_atmospheric_entry(impactor.get_mass(), impactor.velocity, velocity, collins_iFactor, altitudeBU,
                                             altitudeBurst, impactor.density, dispersion, impactor.theta, energy_surface, energy_megatons)

    if altitudeBurst <= 0:
        ejecta_arrival = cal_eject_arrival(impactor, targets)

        ejecta_thickness = cal_ejecta_thickness(impactor, targets)
        d_frag = cal_d_frag(impactor=impactor, target=targets,
                            cdiameter=cdiameter, altitudeBurst=altitudeBurst, Dtr=Dtr)

        if velocity >= 15:
            (
                h,
                Rf,
                thermal_exposure_,
                no_radiation_,
                max_rad_time_,
                irradiation_time_,
                megaton_factor_,
                thermal_power_,
            ) = cal_themal(impactor, targets)
        else:
            (
                h,
                Rf,
                thermal_exposure_,
                no_radiation_,
                max_rad_time_,
                irradiation_time_,
                megaton_factor_,
                thermal_power_,
            ) = 0, 0, 0, 0, 0, 0, 0, 0

        magnitude = cal_magnitude(impactor, targets)

        eff_mag, seismic_arrival = cal_magnitude2(impactor, targets)

        crater_disc = print_crater(vMelt, Dtr, targets.depth, wdiameter, impactor.pdiameter, dispersion,
                                   collins_iFactor, depthtr, mratio, mcratio, cdiameter, depthfr, brecciaThickness, velocity)

        try:
            enerm_pow = int(log(energy_megatons)/log(10))
        except:
            enerm_pow = -inf

        if targets.distance * 1000 <= Dtr/2:
            eject_disc = print_ejecta(energy_megatons, enerm_pow, targets.distance,
                                      Rf, Dtr, cdiameter, ejecta_arrival, ejecta_thickness, d_frag)
            return

        themal_disc = print_thermal(velocity, no_radiation_, max_rad_time_, targets.distance, Rf,
                                    h, thermal_power_, thermal_exposure_, irradiation_time_)
        seismic_disc = print_seismic(magnitude, seismic_arrival)
        ejecta_disc = print_ejecta(energy_megatons, enerm_pow, targets.distance,
                                   Rf, Dtr, cdiameter, ejecta_arrival, ejecta_thickness, d_frag)

    # Compute the effects of the airblast and print
    shock_arrival = cal_shock_arrival(impactor, targets)
    vmax, opressure = cal_vmax(impactor, targets)
    shock_damage = cal_shock_damage(
        impactor=impactor, target=targets, opressure=opressure, vmax=vmax)
    dec_level = cal_dec_level(impactor, targets)
    airblast_disc = print_airblast(opressure, vmax, shock_arrival,
                                   targets.distance, altitudeBurst, dec_level, shock_damage)

    # Compute the tsunami amplitude if water layer present
    if targets.depth > 0:
        TsunamiArrivalTime = cal_TsunamiArrivalTime(impactor, targets)
        WaveAmplitudeUpperLimit = cal_WaveAmplitudeUpperLimit(
            impactor, targets)
        WaveAmplitudeLowerLimit = cal_WaveAmplitudeLowerLimit(
            impactor, targets)
        tsunami_disc = print_tsunami(targets.distance, wdiameter, TsunamiArrivalTime,
                                     WaveAmplitudeLowerLimit, WaveAmplitudeUpperLimit)

    return energy_disc, rec_disc, change_disc, atmos_disc, crater_disc, eject_disc, themal_disc, seismic_disc, ejecta_disc, airblast_disc, tsunami_disc


if __name__ == "__main__":
    impactor, target = get_input()
    # impactor = impactEffects.instances.ImpactorClass.Impactor(
    #     diameter=111, density=111000, velocity=111, theta=45
    # )
    # target = TargetClass.Target(depth=0, distance=111, density=2750)
    simulateImpactor(impactor, target)
