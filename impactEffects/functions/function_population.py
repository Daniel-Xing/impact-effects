from impactEffects.instances.Impactor_population import ImpactorPopulation
from impactEffects.instances.TargetClass import Target
from impactEffects.core.core_population import *


def cal_lratio_population(
    impactor: ImpactorPopulation,
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
        return collins_cal_lratio_population(impactor, target, velocity)

    return 0


def cal_pratio_population(
    impactor: ImpactorPopulation,
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
        return collins_cal_pratio_population(impactor, target, velocity)

    return 0


def cal_trot_change_population(
    impactor: ImpactorPopulation,
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
        return collins_cal_trot_change_population(impactor, target, velocity)

    return 0


def cal_vration_population(
    impactor: ImpactorPopulation,
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
        return collins_cal_vRation_population(impactor, target, Dtr)

    return [0]


def cal_mratio_population(
    impactor: ImpactorPopulation,
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
        return collins_cal_mratio_population(
            impactor, target, velocity, vMelt, vCrater, Dtr
        )

    return 0


def cal_themal_population(
    impactor: ImpactorPopulation,
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
        return collins_cal_themal_population(
            impactor, target, energy_surface, altitudeBurst, delta, velocity,
        )

    return [0]
