import math
import logging

from src.Impactor import *
from src.Targets import *


def atmospheric_entry(impactor: Impactor, target: Target):
    ## Approximate the strength of the impactor using the density function in
    ## Eq. 9 of Collins et al. (2005)
    _yield = 10 ** (2.107 + 0.0624 * impactor.pdensity ** (1 / 2))
    ## Define a relative strength of the impactor compared to the
    ## maximum possible stagnation pressure on entry
    _rStrength = _yield / (target.rhoSurface * (impactor.velocity * 1000) ** 2)
    ## Define the exponent of Eq. 8 for the case of impact at the surface
    _av = 3 * target.rhoSurface * target.dragC * target.schaleHeight / \
        (4 * impactor.density * impactor.pdiameter * math.sin())


def calc_energy(impactor: Impactor, target: Target):
    """
    Implement equation (1)
    """
    mass = impactor.get_mass()
    # 单位坐标转换
    energy0 = 0.5 * mass * (impactor.velocity * 1000) ** 2
    # 焦耳到兆吨的转换
    energy0_megatons = energy0 * joules2megatones

    # Compute the recurrence interval for this energy impact
    # New model (after Bland and Artemieva (2006) MAPS 41 (607-621).
    if mass < 3:
        rec_time = 10 ** (-4.568) * mass ** 0.480
    elif mass < 1.7E10:
        rec_time = 10 ** (-4.739) * mass ** 0.926
    elif mass < 3.3E12:
        rec_time = 10 ** (0.922) * mass ** 0.373
    elif mass < 8.4E14:
        rec_time = 10 ** (-0.086) * mass ** 0.454
    else:
        rec_time = 10 ** (-3.352) * mass ** 0.672

    ### Use our previous estimate at large sizes.
    rec_time = max(rec_time, 110 * (energy0_megatons) ** 0.77)

    ### If the impactor is less than a kilogram, the impactor burns up in the atmosphere
    if mass < 1:
        logging.warning("Impactor is less than a kilogram. Impactor will burn up in the atmosphere.")
