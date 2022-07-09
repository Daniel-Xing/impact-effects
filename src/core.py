import math
import logging

from src.Impactor import *
from src.Targets import *


def atmospheric_entry(impactor: Impactor, target: Target):
    pdensity, dragC, rhoSurface, scaleHeight, pdiameter, velocity, theta, fp = \
        impactor.get_density(), target.get_dragC(), target.get_rhoSurface(), target.get_schaleHeight(), \
            impactor.get_pdiameter(), impactor.get_velocity(), impactor.get_theta(), target.get_fp()
    ## Approximate the strength of the impactor using the density function in
    ## Eq. 9 of Collins et al. (2005)
    _yield = 10 ** (2.107 + 0.0624 * pdensity ** (1 / 2))
    ## Define a relative strength of the impactor compared to the
    ## maximum possible stagnation pressure on entry
    _rStrength = _yield / (rhoSurface * (velocity * 1000) ** 2)
    ## Define the exponent of Eq. 8 for the case of impat at the surface
    _av = 3 * rhoSurface * dragC * scaleHeight / \
        (4 * pdensity * pdiameter * math.sin(theta * PI / 180))
        
    iFactor = 2.7185 * _av * _rStrength
    
    if iFactor >= 1:
        ## Burst altitude is zero
        altitudeBurst = 0

        ## Define the terminal velocity
        # Assuming drag coefficient of 2
        _vTerminal = min(impactor.get_velocity(), \
                         (4 * impactor.density * impactor.pdiameter * target.g / (3 * target.rhoSurface * target.dragC) )**(1/2)) 

        ## Define the surface velocity assuming continual spreading using Eq. 8
        _vSurface = impactor.vInput * 1000 * math.exp(-_av)
            
        ## Take the maximum of the extrapolated surface velocity and the terminal velocity
        if _vTerminal > _vSurface:
            velocity_at_surface = _vTerminal
        else:
            velocity_at_surface = _vSurface
    else:
        ## Compute the first term in Eq. 11
        altitude1 = - target.scaleHeight * math.log(_rStrength)

        ## Define the second, third and fourth terms (inside the brackets) in Eq. 11
        omega = 1.308 - 0.314 * iFactor - 1.303 * (1 - iFactor)**0.5

        ## Compute the breakup altitude by combining above parameters to evaluate Eq. 11
        altitudeBU = altitude1 - omega * target.scaleHeight

        ## Define velocity at breakup altitude using Eq. 8 (and Eq. 5)
        vBU = impactor.get_velocity() * 1000 * math.exp(- _av * math.exp(- altitudeBU/target.scaleHeight)) # m/s

        ## Define factor for evaluating Eq. 17
        vFac = 0.75 * (target.get_dragC() * target.get_rhoSurface() / impactor.get_density())**0.5 * \
                    math.exp(- altitudeBU / (2 * target.get_schaleHeight())) # Assuming drag coefficient of 2

        ## Define dispersion length-scale (Eq. 16)
        lDisper = impactor.get_pdiameter() * math.sin(impactor.get_theta() * PI / 180) * \
            (pdensity / (dragC * rhoSurface) )**(1/2) * exp(altitudeBU / (2 * scaleHeight)) # Assuming drag coefficient of 2

        ## Define the alpha parameters used to evaluate Eq. 18 and Eq. 19
        alpha2 = (fp**2 - 1)**(1/2)

        ## Define the burst altitude using Eq. 18
        altitudePen = 2 * scaleHeight * log(1 + alpha2 * lDisper /(2 * scaleHeight))
        altitudeBurst = altitudeBU - altitudePen
        
        if altitudeBurst > 0:
            ## Evaluate Eq. 19 (without factor lL_0^2; $lDisper * $pdiameter**2)
            expfac = 1/24 * alpha2 *(24 + 8 * alpha2**2 + 6 * alpha2 * lDisper / scaleHeight + 3 * alpha2**3 * lDisper / scaleHeight)

            ## Evaluate velocity at burst using Eq. 17 
            ## (note that factor $lDisper * $pdiameter**2 in $expfac cancels with same factor in $vFac)
            velocity_at_surface = vBU * exp(- expfac * vFac)
        else:
            ## Define (l/H) for use in Eq. 20
            altitudeScale = scaleHeight / lDisper

            ## Evaluate Eq. 20 (without factor lL_0^2; $lDisper * $pdiameter**2)
            ## (note that this Eq. is not correct in the paper)
            integral = altitudeScale**3 / 3 * (3 * (4 + 1/altitudeScale**2) * exp(altitudeBU / scaleHeight) + \
                6 * exp(2 * altitudeBU / scaleHeight) - 16 * exp(1.5 * altitudeBU / scaleHeight ) - 3 / altitudeScale**2 - 2)

            ## Evaluate velocity at the surface using Eq. 17
            velocity_at_surface = vBU * exp(- vFac * integral)

            ## Evaluate dispersion of impactor at impact using Eq. 15
            dispersion = pdiameter * (1 + 4 * altitudeScale**2 * (exp(altitudeBU / (2 * scaleHeight)) - 1)**2)**(1/2)

    velocity_at_surface /= 1000
    
    return velocity_at_surface, iFactor, altitudeBU, altitudeBurst, dispersion


def calc_energy(impactor: Impactor, target: Target):
    """
    Implement equation (1)
    """
    mass = impactor.get_mass()
    # 单位坐标转换
    energy0 = impactor.get_energy0()
    # 焦耳到兆吨的转换
    energy0_megatons = impactor.get_energy0_megatons()

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
