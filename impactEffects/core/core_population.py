from impactEffects.instances.Impactor_population import ImpactorPopulation
from impactEffects.instances.TargetClass import Target
from impactEffects.core.core_collins import *


def collins_cal_lratio_population(
    impactors: ImpactorPopulation, target: Target, velocity: float = 0,
):
    """

    Arguments
    ---------


    Returns
    -------

    """
    lratio = []

    for instance in impactors.Instances():
        lratio.append(
            collins_fraction_of_momentum(
                impactor=instance, target=target, velocity=velocity,
            )[0]
        )

    return lratio


def collins_cal_pratio_population(
    impactors: ImpactorPopulation, target: Target, velocity: float = 0,
):
    """

    Arguments
    ---------


    Returns
    -------

    """
    pratio = []

    for instance in impactors.Instances():
        pratio.append(
            collins_fraction_of_momentum(
                impactor=instance, target=target, velocity=velocity,
            )[1]
        )

    return pratio


def collins_cal_trot_change_population(
    impactors: ImpactorPopulation, target: Target, velocity: float = 0
):
    """

    Arguments
    ---------


    Returns
    -------

    """

    trot_change = []

    for instance in impactors.Instances():
        trot_change.append(
            collins_cal_trot_change(
                impactor=instance, target=target, velocity=velocity,
            )
        )

    return trot_change


def collins_cal_vRation_population(
    impactors: ImpactorPopulation, target: Target, Dtr: float = 0,
) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """
    vratio = []

    for instance in impactors.Instances():
        vratio.append(
            collins_cal_vCrater_vRation(
                impactor=instance, target=target, Dtr=Dtr
            )[1]
        )

    return vratio


def collins_cal_mratio_population(
    impactors: ImpactorPopulation,
    target: Target,
    velocity: float = 0,
    vMelt: float = 0,
    vCrater: float = 0,
    Dtr: float = 0,
) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """

    mratio = []

    for instance in impactors.Instances():
        mratio.append(
            collins_cal_mratio_and_mcratio(
                impactor=instance,
                target=target,
                velocity=velocity,
                vMelt=vMelt,
                vCrater=vCrater,
                Dtr=Dtr,
            )[0]
        )

    return mratio


def collins_cal_themal_population(
    impactors: ImpactorPopulation,
    target: Target,
    energy_surface: float = 0,
    altitudeBurst: float = 0,
    delta: float = 0,
    velocity: float = 0,
):
    """

    Arguments
    ---------


    Returns
    -------

    """

    res = {
        "h": [],
        "Rf": [],
        "thermal_exposure": [],
        "no_radiation": [],
        "max_rad_time": [],
        "irradiation_time": [],
        "megaton_factor": [],
        "thermal_power": [],
    }

    for instance in impactors.Instances():
        (
            h,
            Rf,
            thermal_exposure,
            no_radiation,
            max_rad_time,
            irradiation_time,
            megaton_factor,
            thermal_power,
        ) = collins_cal_themal(
            impactor=instance,
            target=target,
            energy_surface=energy_surface,
            altitudeBurst=altitudeBurst,
            delta=delta,
            velocity=velocity,
        )

        # Append res in list
        res["h"].append(h)
        res["Rf"].append(Rf)
        res["thermal_exposure"].append(thermal_exposure)
        res["no_radiation"].append(no_radiation)
        res["max_rad_time"].append(max_rad_time)
        res["irradiation_time"].append(irradiation_time)
        res["megaton_factor"].append(megaton_factor)
        res["thermal_power"].append(thermal_power)

    return res
