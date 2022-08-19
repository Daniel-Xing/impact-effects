
from impactEffects.instances.Impactor_population import ImpactorPopulation
from impactEffects.instances.TargetClass import Target
from impactEffects.core.core_collins import *


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
        ) = collins_cal_themal(impactor=instance, target=target)

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
