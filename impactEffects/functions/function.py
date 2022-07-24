# -*- encoding: utf-8 -*-
"""
Filename         :core.py
Description      :
Time             :2022/07/10 09:37:51
Author           :daniel
Version          :1.0
"""

from impactEffects.instances.ImpactorClass import *
from impactEffects.instances.TargetClass import *
from impactEffects.core.config import *
from impactEffects.core.core_collins import *


def kinetic_energy(
    impactor: Impactor, type: Choices = Choices.Collins
) -> float:
    """

    Arguments
    ---------
    impactor: Instance of Impactor, containning

    Returns
    -------

    """
    if type is Choices.Collins:
        return collins_kinetic_energy(impactor)

    return 0


def kinetic_energy_megatons(
    impactor: Impactor, type: Choices = Choices.Collins
) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """
    if type is Choices.Collins:
        return collins_kinetic_energy_megatons(impactor)

    return 0


def rec_time(impactor: Impactor, type: Choices = Choices.Collins) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """

    if type is Choices.Collins:
        return collins_rec_time(impactor)

    return 0


def iFactor(
    impactor: Impactor, target: Target, type: Choices = Choices.Collins
) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """

    if type is Choices.Collins:
        return collins_cal_iFactor(impactor, target)

    return 0


def burst_velocity_at_zero(
    impactor: Impactor, target: Target, type: Choices = Choices.Collins
) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """
    if type is Choices.Collins:
        return collins_burst_velocity_at_zero(impactor, target)

    return 0


def altitude_of_breakup(
    impactor: Impactor,
    target: Target,
    collins_iFactor: float = 0,
    type: Choices = Choices.Collins,
) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """

    if type is Choices.Collins:
        return collins_altitude_of_breakup(
            impactor, target, collins_iFactor
        )

    return 0


def velocity_at_breakup(
    impactor: Impactor,
    target: Target,
    av: float = 0,
    altitudeBU: float = 0,
    type: Choices = Choices.Collins,
) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """

    if type is Choices.Collins:
        return collins_velocity_at_breakup(impactor, target, av, altitudeBU)

    return 0


def dispersion_length_scale(
    impactor: Impactor,
    target: Target,
    altitudeBU: float = 0,
    type: Choices = Choices.Collins,
) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """
    if type is Choices.Collins:
        return collins_dispersion_length_scale(impactor, target, altitudeBU)

    return 0


def airburst_altitude(
    impactor: Impactor,
    target: Target,
    alpha2: float = 0,
    lDisper: float = 0,
    altitudeBU: float = 0,
    type: Choices = Choices.Collins,
) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """
    if type is Choices.Collins:
        return collins_airburst_altitude(
            impactor, target, alpha2, lDisper, altitudeBU
        )

    return 0


def brust_velocity(
    impactor: Impactor,
    target: Target,
    altitudeBurst: float = 0,
    altitudeBU: float = 0,
    vBu: float = 0,
    lDisper: float = 0,
    type: Choices = Choices.Collins,
) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """

    if type is Choices.Collins:
        return collins_brust_velocity(
            impactor, target, altitudeBurst, altitudeBU, vBu, lDisper
        )

    return 0


def dispersion_of_impactor(
    impactor: Impactor,
    target: Target,
    l_disper: float = 0,
    altitude_bu: float = 0,
    altitude_burst: float = 0,
    type: Choices = Choices.Collins,
) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """

    if type is Choices.Collins:
        return collins_dispersion_of_impactor(
            impactor, target, l_disper, altitude_bu, altitude_burst
        )

    return 0


def fraction_of_momentum(
    impactor: Impactor,
    target: Target,
    velocity: float = 0,
    type: Choices = Choices.Collins,
) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """

    if type is Choices.Collins:
        return collins_fraction_of_momentum(impactor, target, velocity)

    return 0


def cal_trot_change(
    impactor: Impactor,
    target: Target,
    velocity: float = 0,
    type: Choices = Choices.Collins,
) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """

    if type is Choices.Collins:
        return collins_cal_trot_change(impactor, target, velocity)

    return 0


def cal_energy_atmosphere(
    impactor: Impactor,
    target: Target,
    velocity: float = 0,
    type: Choices = Choices.Collins,
) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """

    if type is Choices.Collins:
        return collins_cal_energy_atmosphere(impactor, target, velocity)

    return 0


def cal_energy_blast_surface(
    impactor: Impactor,
    target: Target,
    velocity: float = 0,
    altitudeBurst: float = 0,
    energy_atmosphere: float = 0,
    type: Choices = Choices.Collins,
) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """
    if type is Choices.Collins:
        return collins_cal_energy_blast_surface(
            impactor, target, velocity, altitudeBurst, energy_atmosphere
        )

    return 0


def cal_mass_of_water(
    impactor: Impactor, target: Target, type: Choices = Choices.Collins
) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """

    if type is Choices.Collins:
        return collins_cal_mass_of_water(impactor, target)

    return 0


def cal_velocity_projectile(
    impactor: Impactor,
    target: Target,
    velocity: float = 0,
    type: Choices = Choices.Collins,
) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """

    if type is Choices.Collins:
        return collins_cal_velocity_projectile(impactor, target, velocity)

    return 0


def cal_energy_at_seafloor(
    impactor: Impactor,
    target: Target,
    vseafloor: float = 0,
    type: Choices = Choices.Collins,
) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """
    if type is Choices.Collins:
        return collins_cal_energy_at_seafloor(impactor, target, vseafloor)

    return 0


def cal_ePIcentral_angle(
    target: Target, type: Choices = Choices.Collins
) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """

    if type is Choices.Collins:
        return collins_cal_ePIcentral_angle(target)

    return 0


def cal_scaling_diameter_constant(
    target: Target, type: Choices = Choices.Collins
) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """

    if type is Choices.Collins:
        return collins_cal_scaling_diameter_constant(target=target)

    return 0


def cal_anglefac(
    impactor: Impactor, type: Choices = Choices.Collins
) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """

    if type is Choices.Collins:
        return collins_cal_anglefac(impactor)

    return 0


def cal_wdiameter(
    impactor: Impactor,
    target: Target,
    anglefac: float = 0,
    velocity: float = 0,
    type: Choices = Choices.Collins,
) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """
    if type is Choices.Collins:
        return collins_cal_wdiameter(impactor, target, anglefac, velocity)

    return 0


def cal_transient_crater_diameter(
    impactor: Impactor,
    target: Target,
    Cd: float = 0,
    beta: float = 0,
    anglefac: float = 0,
    vseafloor: float = 0,
    type: Choices = Choices.Collins,
) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """
    if type is Choices.Collins:
        return collins_cal_transient_crater_diameter(
            impactor, target, Cd, beta, anglefac, vseafloor
        )

    return 0


def cal_depthr(
    impactor: Impactor,
    target: Target,
    Dtr: float = 0,
    type: Choices = Choices.Collins,
) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """
    if type is Choices.Collins:
        return collins_cal_depthr(impactor, target, Dtr)

    return 0


def cal_cdiamater(
    impactor: Impactor,
    target: Target,
    Dtr: float = 0,
    type: Choices = Choices.Collins,
) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """
    if type is Choices.Collins:
        return collins_cal_cdiamater(impactor, target, Dtr)

    return 0


def cal_depthfr(
    impactor: Impactor,
    target: Target,
    Dtr: float = 0,
    depthtr: float = 0,
    cdiameter: float = 0,
    type: Choices = Choices.Collins,
) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """
    if type is Choices.Collins:
        return collins_cal_depthfr(
            impactor, target, Dtr, depthtr, cdiameter
        )

    return 0


def cal_vCrater(
    impactor: Impactor,
    target: Target,
    Dtr: float = 0,
    type: Choices = Choices.Collins,
) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """
    if type is Choices.Collins:
        return collins_cal_vCrater(impactor, target, Dtr)

    return 0


def cal_vratio(
    impactor: Impactor,
    target: Target,
    vCrater: float = 0,
    Dtr: float = 0,
    type: Choices = Choices.Collins,
) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """
    if type is Choices.Collins:
        return collins_cal_vratio(impactor, target, vCrater, Dtr)

    return 0


def cal_vCrater_vRation(
    impactor: Impactor,
    target: Target,
    Dtr: float = 0,
    type: Choices = Choices.Collins,
) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """
    if type is Choices.Collins:
        return collins_cal_vCrater_vRation(impactor, target, Dtr)

    return 0


def cal_vMelt(
    impactor: Impactor,
    target: Target,
    velocity: float = 0,
    energy_seafloor: float = 0,
    type: Choices = Choices.Collins,
) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """
    if type is Choices.Collins:
        return collins_cal_vMelt(
            impactor, target, velocity, energy_seafloor
        )

    return 0


def cal_mratio_and_mcratio(
    impactor: Impactor,
    target: Target,
    velocity: float = 0,
    vMelt: float = 0,
    vCrater: float = 0,
    Dtr: float = 0,
    type: Choices = Choices.Collins,
) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """
    if type is Choices.Collins:
        return collins_cal_mratio_and_mcratio(
            impactor, target, velocity, vMelt, vCrater, Dtr
        )

    return 0


def cal_eject_arrival(
    impactor: Impactor,
    target: Target,
    altitudeBurst: float = 0,
    type: Choices = Choices.Collins,
) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """
    if type is Choices.Collins:
        return collins_cal_eject_arrival(impactor, target, altitudeBurst)

    return 0


def cal_ejecta_thickness(
    impactor: Impactor,
    target: Target,
    altitudeBurst: float = 0,
    Dtr: float = 0,
    type: Choices = Choices.Collins,
) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """
    if type is Choices.Collins:
        return collins_cal_ejecta_thickness(
            impactor, target, altitudeBurst, Dtr
        )

    return 0


def cal_d_frag(
    impactor: Impactor,
    target: Target,
    cdiameter: float = 0,
    altitudeBurst: float = 0,
    Dtr: float = 0,
    type: Choices = Choices.Collins,
) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """
    if type is Choices.Collins:
        return collins_cal_d_frag(
            impactor, target, cdiameter, altitudeBurst, Dtr
        )

    return 0


def cal_themal(
    impactor: Impactor,
    target: Target,
    energy_surface: float = 0,
    altitudeBurst: float = 0,
    delta: float = 0,
    velocity: float = 0,
    type: Choices = Choices.Collins,
) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """
    if type is Choices.Collins:
        return collins_cal_themal(
            impactor,
            target,
            energy_surface,
            altitudeBurst,
            delta,
            velocity,
        )

    return 0


def cal_magnitude(
    impactor: Impactor,
    target: Target,
    altitudeBurst: float = 0,
    energy_seafloor: float = 0,
    type: Choices = Choices.Collins,
) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """
    if type is Choices.Collins:
        return collins_cal_magnitude(
            impactor, target, altitudeBurst, energy_seafloor
        )

    return 0


def cal_magnitude2(
    impactor: Impactor,
    target: Target,
    energy_seafloor: float = 0,
    altitudeBurst: float = 0,
    distance: float = 0,
    surface_wave_v: float = 0,
    delta: float = 0,
    type: Choices = Choices.Collins,
) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """
    if type is Choices.Collins:
        return collins_cal_magnitude2(
            impactor, target, altitudeBurst, energy_seafloor, delta
        )

    return 0


def cal_shock_arrival(
    impactor: Impactor,
    target: Target,
    altitudeBurst: float = 0,
    type: Choices = Choices.Collins,
) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """
    if type is Choices.Collins:
        return collins_cal_shock_arrival(impactor, target, altitudeBurst)

    return 0


def cal_vmax(
    impactor: Impactor,
    target: Target,
    energy_blast: float = 0,
    altitudeBurst: float = 0,
    type: Choices = Choices.Collins,
) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """
    if type is Choices.Collins:
        return collins_cal_vmax(
            impactor, target, energy_blast, altitudeBurst
        )

    return 0


def cal_shock_damage(
    impactor: Impactor,
    target: Target,
    opressure: float = 0,
    vmax: float = 0,
    type: Choices = Choices.Collins,
) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """
    if type is Choices.Collins:
        return collins_cal_shock_damage(impactor, target, opressure, vmax)

    return 0


def cal_dec_level(
    impactor: Impactor,
    target: Target,
    energy_blast: float = 0,
    altitudeBurst: float = 0,
    type: Choices = Choices.Collins,
) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """
    if type is Choices.Collins:
        return collins_cal_dec_level(
            impactor, target, energy_blast, altitudeBurst
        )

    return 0


def cal_TsunamiArrivalTime(
    impactor: Impactor,
    target: Target,
    wdiameter: float = 0,
    type: Choices = Choices.Collins,
) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """
    if type is Choices.Collins:
        return collins_cal_TsunamiArrivalTime(impactor, target, wdiameter)
    elif type is Choices.Example:
        return NotImplementedError("Error")

    return 0


def cal_WaveAmplitudeUpperLimit(
    impactor: Impactor,
    target: Target,
    wdiameter: float = 0,
    type: Choices = Choices.Collins,
) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """
    if type is Choices.Collins:
        return collins_cal_WaveAmplitudeUpperLimit(
            impactor, target, wdiameter
        )

    return 0


def cal_WaveAmplitudeLowerLimit(
    impactor: Impactor,
    target: Target,
    wdiameter: float = 0,
    type: Choices = Choices.Collins,
) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """
    if type is Choices.Collins:
        return collins_cal_WaveAmplitudeLowerLimit(
            impactor, target, wdiameter
        )

    return 0
