import numpy as np
from sympy import re
import impactEffects.instances.ImpactorClass
from impactEffects.functions import *
from impactEffects.functions.function import *
from impactEffects.instances import ImpactorClass, TargetClass


def impact(impartor: Impactor, targets: Target):
    impactor = impactEffects.instances.ImpactorClass.Impactor(
        diameter=111, density=111, velocity=111, theta=45, depth=0, ttype=3
    )
    targets = TargetClass.Target(depth=0, distance=75, density=2500)

    res = kinetic_energy(impactor)
    print(res, energy0)

    impactor = impactEffects.instances.ImpactorClass.Impactor(
        diameter=111, density=111, velocity=111, theta=45, depth=0, ttype=3
    )
    targets = TargetClass.Target(depth=0, distance=75, density=2500)

    res = kinetic_energy_megatons(impactor)
    print(res, energy0_megatons)

    impactor = impactEffects.instances.ImpactorClass.Impactor(
        diameter=111, density=111, velocity=111, theta=45, depth=0, ttype=3
    )
    targets = TargetClass.Target(depth=0, distance=75, density=2500)

    res = rec_time(impactor)
    print(res, rec_time_)

    impactor = impactEffects.instances.ImpactorClass.Impactor(
        diameter=111, density=111, velocity=111, theta=45, depth=0, ttype=3
    )
    targets = TargetClass.Target(depth=0, distance=75, density=2500)

    collins_iFactor, _av, _rStrength = iFactor(impactor, targets)
    print(collins_iFactor, i_Factor)

    impactor = impactEffects.instances.ImpactorClass.Impactor(
        diameter=111, density=111, velocity=111, theta=45, depth=0, ttype=3
    )
    targets = TargetClass.Target(depth=0, distance=75, density=2500)

    res = altitude_of_breakup(impactor, targets)

    print(res, altitudeBurst)

    impactor = impactEffects.instances.ImpactorClass.Impactor(
        diameter=111, density=111, velocity=111, theta=45, depth=0, ttype=3
    )
    targets = TargetClass.Target(depth=0, distance=75, density=2500)

    res = velocity_at_breakup(impactor, targets)

    print(res, vBU)

    impactor = impactEffects.instances.ImpactorClass.Impactor(
        diameter=111, density=111, velocity=111, theta=45, depth=0, ttype=3
    )
    targets = TargetClass.Target(depth=0, distance=75, density=2500)

    res = dispersion_length_scale(impactor, targets)

    print(res, lDisper)

    impactor = impactEffects.instances.ImpactorClass.Impactor(
        diameter=111, density=111, velocity=111, theta=45, depth=0, ttype=3
    )
    targets = TargetClass.Target(depth=0, distance=75, density=2500)

    res = airburst_altitude(impactor, targets)

    print(res, altitudeBurst)

    impactor = impactEffects.instances.ImpactorClass.Impactor(
        diameter=111, density=111, velocity=111, theta=45, depth=0, ttype=3
    )
    targets = TargetClass.Target(depth=0, distance=75, density=2500)

    res = brust_velocity(impactor, targets)
    print(res, velocity)

    impactor = impactEffects.instances.ImpactorClass.Impactor(
        diameter=111, density=111, velocity=111, theta=45, depth=0, ttype=3
    )
    targets = TargetClass.Target(depth=0, distance=75, density=2500)

    res = dispersion_of_impactor(impactor, targets)

    impactor = impactEffects.instances.ImpactorClass.Impactor(
        diameter=111, density=111, velocity=111, theta=45, depth=0, ttype=3
    )
    targets = TargetClass.Target(depth=0, distance=75, density=2500)

    res = fraction_of_momentum(impactor, targets)

    print(res, lratio, pratio)

    impactor = impactEffects.instances.ImpactorClass.Impactor(
        diameter=111, density=111, velocity=111, theta=45, depth=0, ttype=3
    )
    targets = TargetClass.Target(depth=0, distance=75, density=2500)

    res = cal_trot_change(impactor, targets)

    impactor = impactEffects.instances.ImpactorClass.Impactor(
        diameter=111, density=111, velocity=111, theta=45, depth=0, ttype=3
    )
    targets = TargetClass.Target(depth=0, distance=75, density=2500)

    res = cal_energy_atmosphere(impactor, targets)

    impactor = impactEffects.instances.ImpactorClass.Impactor(
        diameter=111, density=111, velocity=111, theta=45, depth=0, ttype=3
    )
    targets = TargetClass.Target(depth=0, distance=75, density=2500)

    res = cal_energy_blast_surface(impactor, targets)

    impactor = impactEffects.instances.ImpactorClass.Impactor(
        diameter=111, density=111, velocity=111, theta=45, depth=0, ttype=3
    )
    targets = TargetClass.Target(depth=0, distance=75, density=2500)

    res = cal_mass_of_water(impactor, targets)

    impactor = impactEffects.instances.ImpactorClass.Impactor(
        diameter=111, density=111, velocity=111, theta=45, depth=0, ttype=3
    )
    targets = TargetClass.Target(depth=0, distance=75, density=2500)

    res = cal_velocity_projectile(impactor, targets)
    print(res, vseafloor)

    impactor = impactEffects.instances.ImpactorClass.Impactor(
        diameter=111, density=111, velocity=111, theta=45, depth=0, ttype=3
    )
    targets = TargetClass.Target(depth=0, distance=75, density=2500)

    res = cal_energy_at_seafloor(impactor, targets)
    print(res, energy_seafloor)

    impactor = impactEffects.instances.ImpactorClass.Impactor(
        diameter=111, density=111, velocity=111, theta=45, depth=0, ttype=3
    )
    targets = TargetClass.Target(depth=0, distance=75, density=2500)

    res = cal_ePIcentral_angle(targets)
    print(res, delta)

    impactor = impactEffects.instances.ImpactorClass.Impactor(
        diameter=111, density=111, velocity=111, theta=45, depth=0, ttype=3
    )
    targets = TargetClass.Target(depth=0, distance=75, density=2500)

    res = cal_scaling_diameter_constant(impactor)
    print(res, Cd, beta)

    impactor = impactEffects.instances.ImpactorClass.Impactor(
        diameter=111, density=111, velocity=111, theta=45, depth=0, ttype=3
    )
    targets = TargetClass.Target(depth=0, distance=75, density=2500)

    res = cal_anglefac(impactor)
    print(res, anglefac)

    impactor = impactEffects.instances.ImpactorClass.Impactor(
        diameter=111, density=111, velocity=111, theta=45, depth=0, ttype=3
    )
    targets = TargetClass.Target(depth=1111, distance=75, density=1000)

    res = cal_wdiameter(impactor, targets)
    wdiameter = 873.96211031212
    print(res, wdiameter)

    impactor = impactEffects.instances.ImpactorClass.Impactor(
        diameter=111, density=111, velocity=111, theta=45, depth=0, ttype=3
    )
    targets = TargetClass.Target(depth=0, distance=75, density=2500)

    res = cal_transient_crater_diameter(impactor, targets)
    print(res, Dtr)

    impactor = impactEffects.instances.ImpactorClass.Impactor(
        diameter=111, density=111, velocity=111, theta=45, depth=0, ttype=3
    )
    targets = TargetClass.Target(depth=0, distance=75, density=2500)

    res = cal_depthr(impactor, targets)
    print(res, depthtr)

    impactor = impactEffects.instances.ImpactorClass.Impactor(
        diameter=111, density=111, velocity=111, theta=45, depth=0, ttype=3
    )
    targets = TargetClass.Target(depth=0, distance=75, density=2500)

    res = cal_cdiamater(impactor, targets)
    print(res, cdiameter)

    impactor = impactEffects.instances.ImpactorClass.Impactor(
        diameter=111, density=111, velocity=111, theta=45, depth=0, ttype=3
    )
    targets = TargetClass.Target(depth=0, distance=75, density=2500)

    res = cal_depthfr(impactor, targets)
    print(res, depthfr)

    impactor = impactEffects.instances.ImpactorClass.Impactor(
        diameter=111, density=111, velocity=111, theta=45, depth=0, ttype=3
    )
    targets = TargetClass.Target(depth=0, distance=75, density=2500)

    res = cal_vCrater_vRation(impactor, targets)
    print(res, vCrater, vratio)

    impactor = impactEffects.instances.ImpactorClass.Impactor(
        diameter=111, density=111, velocity=111, theta=45, depth=0, ttype=3
    )
    targets = TargetClass.Target(depth=0, distance=75, density=2500)

    res = cal_vMelt(impactor, targets)
    print(res, vMelt)

    impactor = impactEffects.instances.ImpactorClass.Impactor(
        diameter=111, density=111, velocity=111, theta=45, depth=0, ttype=3
    )
    targets = TargetClass.Target(depth=0, distance=75, density=2500)

    res = cal_mratio_and_mcratio(impactor, targets)
    print(res, mratio, mcratio)

    impactor = impactEffects.instances.ImpactorClass.Impactor(
        diameter=111000, density=111, velocity=111, theta=45, depth=0, ttype=3
    )
    targets = TargetClass.Target(depth=1111, distance=75, density=1000)

    res = cal_eject_arrival(impactor, targets)
    ejecta_arrival = 124.569530217127
    print(res, ejecta_arrival)

    impactor = impactEffects.instances.ImpactorClass.Impactor(
        diameter=111000, density=111, velocity=111, theta=45, depth=0, ttype=3
    )
    targets = TargetClass.Target(depth=1111, distance=75, density=1000)

    res = cal_ejecta_thickness(impactor, targets)
    ejecta_thickness = 143311.274150426

    print(res, ejecta_thickness)

    impactor = impactEffects.instances.ImpactorClass.Impactor(
        diameter=111000, density=111, velocity=111, theta=45, depth=0, ttype=3
    )
    targets = TargetClass.Target(depth=1111, distance=75, density=1000)

    (
        thermal_exposure_,
        no_radiation_,
        max_rad_time_,
        irradiation_time_,
        megaton_factor_,
        thermal_power_,
    ) = cal_themal(impactor, targets)
    (
        thermal_exposure,
        no_radiation,
        max_rad_time,
        irradiation_time,
        megaton_factor,
        thermal_power,
    ) = (
        4.14356223682368,
        0,
        14.208291667122,
        20466.8083549098,
        69.9012618159051,
        13,
    )

    impactor = impactEffects.instances.ImpactorClass.Impactor(
        diameter=111000, density=111, velocity=111, theta=45, depth=0, ttype=3
    )
    targets = TargetClass.Target(depth=1111, distance=75, density=1000)

    res = cal_magnitude(impactor, targets)
    magnitude = 11.9138097245741

    impactor = impactEffects.instances.ImpactorClass.Impactor(
        diameter=111000, density=111, velocity=111, theta=45, depth=0, ttype=3
    )
    targets = TargetClass.Target(depth=1111, distance=75, density=1000)

    eff_mag = 10.3894097245741
    seismic_arrival = 15
    res = cal_magnitude2(impactor, targets)

    print(res)

    impactor = impactEffects.instances.ImpactorClass.Impactor(
        diameter=111, density=111, velocity=111, theta=45, depth=0, ttype=3
    )
    targets = TargetClass.Target(depth=0, distance=75, density=2500)

    res = cal_shock_arrival(impactor, targets)
    print(res, shock_arrival)

    impactor = impactEffects.instances.ImpactorClass.Impactor(
        diameter=111, density=111, velocity=111, theta=45, depth=0, ttype=3
    )
    targets = TargetClass.Target(depth=0, distance=75, density=2500)

    res = cal_vmax(impactor, targets)

    impactor = impactEffects.instances.ImpactorClass.Impactor(
        diameter=111, density=111, velocity=111, theta=45, depth=0, ttype=3
    )
    targets = TargetClass.Target(depth=0, distance=75, density=2500)

    res = cal_dec_level(impactor, targets)

    impactor = impactEffects.instances.ImpactorClass.Impactor(
        diameter=111, density=111, velocity=111, theta=45, depth=0, ttype=3
    )
    targets = TargetClass.Target(depth=1111, distance=75, density=1000)

    res = cal_TsunamiArrivalTime(impactor, targets)
    TsunamiArrivalTime = 1436.89232538551

    print(res, TsunamiArrivalTime)

    impactor = impactEffects.instances.ImpactorClass.Impactor(
        diameter=111, density=111, velocity=111, theta=45, depth=0, ttype=3
    )
    targets = TargetClass.Target(depth=1111, distance=75, density=1000)

    res = cal_WaveAmplitudeUpperLimit(impactor, targets)
    WaveAmplitudeUpperLimit = 0.712889118910467

    print(res, WaveAmplitudeUpperLimit)

    impactor = impactEffects.instances.ImpactorClass.Impactor(
        diameter=111, density=111, velocity=111, theta=45, depth=0, ttype=3
    )
    targets = TargetClass.Target(depth=1111, distance=75, density=1000)

    res = cal_WaveAmplitudeLowerLimit(impactor, targets)
    WaveAmplitudeLowerLimit = 0.00103553906729725

    print(res, WaveAmplitudeLowerLimit)
