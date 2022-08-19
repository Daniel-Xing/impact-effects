from impactEffects.instances.Impactor_population import ImpactorPopulation
from impactEffects.instances.TargetClass import Target
from impactEffects.core.core_population import *


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
            impactor,
            target,
            energy_surface,
            altitudeBurst,
            delta,
            velocity,
        )

    return 0
    