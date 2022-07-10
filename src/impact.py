# -*- encoding: utf-8 -*-
'''
Filename         :impact.py
Description      :
Time             :2022/07/10 10:39:57
Author           :daniel
Version          :1.0
'''
from src.config import *
from src.core import *

def atmospheric_entry(impactor: Impactor, target: Target):
    """
    
    Arguments
    ---------
    
    
    Returns
    -------
    
    """
    
    i_factor, _av, _rStrength = iFactor(impactor, target)
    
    if i_factor >= 1:
        velocity_at_surface = burst_velocity_at_zero(impactor, target)
    else:
        ## Compute the breakup altitude by combining above parameters to evaluate Eq. 11
        altitudeBU = altitude_of_breakup(target.scaleHeight, _rStrength, i_factor)

        ## Define velocity at breakup altitude using Eq. 8 (and Eq. 5)
        vBU = velocity_at_breakup(impactor.get_velocity(), _av, altitudeBU, target.get_schaleHeight())

        ## Define dispersion length-scale (Eq. 16)
        lDisper = dispersion_length_scale(impactor.get_pdiameter(), impactor.get_theta(), impactor.get_density(), \
            target.get_dragC(), target.get_rhoSurface(), altitudeBU, target.get_schaleHeight())

        ## Define the alpha parameters used to evaluate Eq. 18 and Eq. 19
        alpha2 = (target.get_fp()**2 - 1)**(1/2)

        ## Define the burst altitude using Eq. 18
        altitudeBurst = airburst_altitude(impactor, target, alpha2, lDisper, altitudeBU)
        
        velocity_at_surface = brust_velocity(impactor, target, altitudeBurst, altitudeBU, vBU, lDisper)
        dispersion = dispersion_of_impactor(impactor, target, lDisper, altitudeBU, altitudeBurst)
    
    return velocity_at_surface, i_factor, altitudeBU, altitudeBurst, dispersion


def calc_energy(impactor: Impactor, target: Target):
    """
    Implement equation (1)
    """
    mass, energy0, energy0_megatons, theta, R_earth = \
        impactor.get_mass(), impactor.get_energy0(), impactor.get_energy0_megatons()

    ### If the impactor is less than a kilogram, the impactor burns up in the atmosphere
    if mass < 1:
        logging.warning("Impactor is less than a kilogram. Impactor will burn up in the atmosphere.")

    ### Calculate the effects of atmospheric entry
    velocity, iFactor, altitudeBU, altitudeBurst, dispersion = atmospheric_entry(impactor, target)
    
    ### Compute linear and angular momentum as a fraction of Earth's
    linmom, angmom, energy0 = fraction_of_momentum(impactor, target, velocity)
    
    trot_change = cal_trot_change(impactor, target, velocity) 
	
    ### Compute energy of airburst, or energy after deceleration by atmosphere
    energy_atmosphere = cal_energy_atmosphere(impactor, target, velocity)
    energy_blast, energy_surface = cal_energy_blast_surface(impactor, target, velocity, altitudeBurst, energy_atmosphere)
    energy_megatons = energy_surface / (4.186 * 10**15) ### joules to megatons conversion

    ### Account for the decelerating effect of the water layer
    mwater = cal_mass_of_water(impactor, target, velocity)
    vseafloor = cal_velocity_projectile(impactor, target, velocity)
    energy_seafloor = cal_energy_at_seafloor(impactor, target, vseafloor)
	
    # ### Compute the epicentral angle for use in several subsequent calculations.
    delta = cal_energy_at_seafloor(target)
    
    return velocity, altitudeBU, altitudeBurst, dispersion, linmom, angmom, energy0, trot_change, \
      energy_atmosphere, energy_blast, energy_surface, energy_megatons, mwater, vseafloor, energy_seafloor, delta
    
    