# -*- encoding: utf-8 -*-
'''
Filename         :core.py
Description      :
Time             :2022/07/10 09:37:51
Author           :daniel
Version          :1.0
'''
import math
import logging

from sympy import im

from src.Impactor import *
from src.Targets import *
from src.config import *

# implement equation 1


def kinetic_energy(impactor: Impactor) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """

    return impactor.get_energy0()


def kinetic_energy_megatons(impactor: Impactor) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """

    return impactor.get_energy0_megatons()


def rec_time(impactor: Impactor) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """

    return impactor.get_rec_time()


def iFactor(impactor: Impactor, target: Target) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """

    pdensity, dragC, rhoSurface, scaleHeight, pdiameter, velocity, theta, fp = \
        impactor.get_density(), target.get_dragC(), target.get_rhoSurface(), target.get_schaleHeight(), \
        impactor.get_pdiameter(), impactor.get_velocity(
        ), impactor.get_theta(), target.get_fp()

    # Approximate the strength of the impactor using the density function in
    # Eq. 9 of Collins et al. (2005)
    _yield = 10 ** (2.107 + 0.0624 * pdensity ** (1 / 2))
    # Define a relative strength of the impactor compared to the
    # maximum possible stagnation pressure on entry
    _rStrength = _yield / (rhoSurface * (velocity * 1000) ** 2)
    # Define the exponent of Eq. 8 for the case of impat at the surface
    _av = 3 * rhoSurface * dragC * scaleHeight / \
        (4 * pdensity * pdiameter * math.sin(theta * PI / 180))

    iFactor = 2.7185 * _av * _rStrength
    return iFactor, _av, _rStrength


def burst_velocity_at_zero(impactor: Impactor,  target: Target) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """
    i_factor, _av, _ = iFactor(impactor, target)

    # check
    if i_factor < 1:
        raise ValueError("I_factor should be greater than 1!")

    # Burst altitude is zero
    altitudeBurst = 0
    # Define the terminal velocity
    # Assuming drag coefficient of 2
    _vTerminal = min(impactor.get_velocity(),
                     (4 * impactor.density * impactor.pdiameter * target.g / (3 * target.rhoSurface * target.dragC))**(1/2))

    # Define the surface velocity assuming continual spreading using Eq. 8
    _vSurface = impactor.vInput * 1000 * math.exp(-_av)

    # Take the maximum of the extrapolated surface velocity and the terminal velocity
    if _vTerminal > _vSurface:
        velocity_at_surface = _vTerminal
    else:
        velocity_at_surface = _vSurface

    return velocity_at_surface


def altitude_of_breakup(scaleHeight: float, rStrength: float, iFactor: float) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """

    # Compute the first term in Eq. 11
    altitude1 = - scaleHeight * log(rStrength)

    # Define the second, third and fourth terms (inside the brackets) in Eq. 11
    omega = 1.308 - 0.314 * iFactor - 1.303 * (1 - iFactor)**0.5

    # Compute the breakup altitude by combining above parameters to evaluate Eq. 11
    altitudeBU = altitude1 - omega * scaleHeight

    return altitudeBU


def velocity_at_breakup(velocity: float, av: float, altitudeBU: float, scaleHeight: float) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """

    # m/s
    return velocity * 1000 * exp(- av * math.exp(- altitudeBU/scaleHeight))


def dispersion_length_scale(diameter: float, theta: float, density: float, dragC: float, rhoSurface: float, altitudeBU: float, scaleHeight: float) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """
    # Assuming drag coefficient of 2
    return diameter * sin(theta * PI / 180) * (density / (dragC * rhoSurface))**0.5 * exp(altitudeBU / (2 * scaleHeight))


def airburst_altitude(impactor: Impactor, target: Target, alpha2: float = None, lDisper: float = None, altitudeBU: float = None) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """
    if lDisper is None:
        lDisper = dispersion_length_scale(impactor.get_pdiameter(), impactor.get_theta(), impactor.get_density(),
                                          target.get_dragC(), target.get_rhoSurface(), altitudeBU, target.get_schaleHeight())

    if altitudeBU is None:
        i_factor, _, _rStrength = iFactor(impactor, target)
        altitudeBU = altitude_of_breakup(
            target.get_schaleHeight(), _rStrength, i_factor)

    if alpha2 is None:
        alpha2 = (target.get_fp()**2 - 1)**(1/2)

    # Define the burst altitude using Eq. 18
    altitudePen = 2 * target.get_schaleHeight() * log(1 + alpha2 * lDisper /
                                                      (2 * target.get_schaleHeight()))
    altitudeBurst = altitudeBU - altitudePen
    return altitudeBurst


def brust_velocity(impactor: Impactor, target: Target, altitudeBurst: float = None, altitudeBU: float = None, vBu: float = None, lDisper: float = None) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """

    if altitudeBU == None:
        i_factor, _av, _rStrength = iFactor(impactor, target)
        altitudeBU = altitude_of_breakup(
            target.get_schaleHeight(), _rStrength, i_factor)

    if vBU == None:
        i_factor, _av, _rStrength = iFactor(impactor, target)
        vBU = velocity_at_breakup(impactor.get_velocity(
        ), _av, altitudeBU, target.get_schaleHeight())

    if lDisper == None:
        lDisper = dispersion_length_scale(impactor.get_pdiameter(), impactor.get_theta(), impactor.get_density(),
                                          target.get_dragC(), target.get_rhoSurface(), altitudeBU, target.get_schaleHeight())

    if altitudeBurst == None:
        alpha2 = (target.get_fp()**2 - 1)**(1/2)
        altitudeBurst = airburst_altitude(
            impactor, target, alpha2, lDisper, altitudeBU)

    # Define factor for evaluating Eq. 17
    vFac = 0.75 * (target.get_dragC() * target.get_rhoSurface() / impactor.get_density())**0.5 * \
        exp(- altitudeBU / (2 * target.get_schaleHeight())
            )  # Assuming drag coefficient of 2

    if altitudeBurst > 0:
        # Evaluate Eq. 19 (without factor lL_0^2; $lDisper * $pdiameter**2)
        expfac = 1/24 * alpha2 * (24 + 8 * alpha2**2 + 6 * alpha2 * lDisper /
                                  target.get_schaleHeight() + 3 * alpha2**3 * lDisper / target.get_schaleHeight())

        # Evaluate velocity at burst using Eq. 17
        # (note that factor $lDisper * $pdiameter**2 in $expfac cancels with same factor in $vFac)
        velocity = vBU * exp(- expfac * vFac)
    else:
        # Define (l/H) for use in Eq. 20
        altitudeScale = target.get_schaleHeight() / lDisper

        # Evaluate Eq. 20 (without factor lL_0^2; $lDisper * $pdiameter**2)
        # (note that this Eq. is not correct in the paper)
        integral = altitudeScale**3 / 3 * (3 * (4 + 1/altitudeScale**2) * exp(altitudeBU / target.get_schaleHeight()) +
                                           6 * exp(2 * altitudeBU / target.get_schaleHeight()) - 16 * exp(1.5 * altitudeBU / target.get_schaleHeight()) - 3 / altitudeScale**2 - 2)

        # Evaluate velocity at the surface using Eq. 17
        velocity = vBU * exp(- vFac * integral)

    return velocity


def dispersion_of_impactor(impactor: Impactor, target: Target, lDisper: float = None, altitudeBU: float = None, altitudeBurst: float = None) -> float:
    """

    Arguments
    ---------


    Returns
    -------

    """

    if altitudeBU == None:
        i_factor, _av, _rStrength = iFactor(impactor, target)
        altitudeBU = altitude_of_breakup(
            target.get_schaleHeight(), _rStrength, i_factor)

    if lDisper == None:
        lDisper = dispersion_length_scale(impactor.get_pdiameter(), impactor.get_theta(), impactor.get_density(),
                                          target.get_dragC(), target.get_rhoSurface(), altitudeBU, target.get_schaleHeight())

    if altitudeBurst == None:
        alpha2 = (target.get_fp()**2 - 1)**(1/2)
        altitudeBurst = airburst_altitude(
            impactor, target, alpha2, lDisper, altitudeBU)

    if altitudeBurst > 0:
        raise ValueError("Impactor is not dispersionless at the surface")

    dispersion = impactor.get_pdiameter() * (1 + 4 * (target.get_schaleHeight() / lDisper)**2 *
                                             (exp(altitudeBU / (2 * target.get_schaleHeight())) - 1)**2)**(1/2)

    return dispersion


def fraction_of_momentum(impactor: Impactor, target: Target, velocity: float = None):
    """
    
    Arguments
    ---------
    
    
    Returns
    -------
    
    """
    
    
    if velocity == None:
        velocity = brust_velocity(impactor, target)

    linmom = impactor.get_mass() * (velocity * 1000)
    angmom = impactor.get_mass() * (velocity * 1000) * \
        cos(impactor.get_theta * PI / 180) * \
        target.get_R_earth()

    # relativistic effects, multiply energy by 1/sqrt(1 - v^2/c^2)
    if impactor.get_velocity() > (0.25 * 3 * 10**5):
        beta = 1 / (1 - impactor.get_velocity()**2 / 9 * 10**10)**0.5
        energy0 = impactor.energy0 * beta
        linmom *= beta
        angmom *= beta

    lratio = angmom / target.get_lEarth()
    pratio = linmom / target.get_pEarth()
    return lratio, pratio, energy0

def cal_trot_change(impactor:Impactor, target:Target, velocity:float=None):
    """
    
    Arguments
    ---------
    
    
    Returns
    -------
    
    """
    
    if velocity == None:
        velocity = brust_velocity(impactor, target)

    mass = impactor.get_mass()
    mEarth = target.get_mEarth()
    theta = impactor.get_theta()
    R_earth = target.get_R_earth()
    
    return (1.25/PI)*(mass/mEarth)*cos(theta * PI / 180) / \
        R_earth * velocity * (24.*60.*60.)**2

def cal_energy_atmosphere(impactor:Impactor, target:Target, velocity: float = None) -> float:
    """
    
    Arguments
    ---------
    
    
    Returns
    -------
    
    """
    
    if velocity == None:
        velocity = brust_velocity(impactor, target)
        
    energy_atmosphere = 0.5 * impactor.get_mass() * ((impactor.get_velocity() * 1000)**2 - (velocity * 1000)**2)
    return energy_atmosphere


def cal_energy_blast_surface(impactor:Impactor, target:Target, velocity: float = None, altitudeBurst:float = None, energy_atmosphere:float = None) -> float:
    """
    
    Arguments
    ---------
    
    
    Returns
    -------
    
    """
    if altitudeBurst == None:
        i_factor, _av, _rStrength = iFactor(impactor, target)
        altitudeBU = altitude_of_breakup(target.get_schaleHeight(), _rStrength, i_factor)
        lDisper = dispersion_length_scale(impactor.get_pdiameter(), impactor.get_theta(), impactor.get_density(),
                                          target.get_dragC(), target.get_rhoSurface(), altitudeBU, target.get_schaleHeight())
        
        alpha2 = (target.get_fp()**2 - 1)**(1/2)
        altitudeBurst = airburst_altitude(
            impactor, target, alpha2, lDisper, altitudeBU)
    
    if velocity == None:
        velocity = brust_velocity(impactor, target, altitudeBurst, altitudeBU, None, lDisper)
    
    
    if altitudeBurst > 0:
        # Blast energy is airburst energy (kTons)
        energy_blast = energy_atmosphere / (4.186 * 10**12)
        energy_surface = energy_atmosphere
    else:
        altitudeBurst = 0
        energy_surface = 0.5 * impactor.get_mass() * (velocity * 1000)**2
        # Blast energy is larger of airburt and impact energy (kTons)
        if energy_atmosphere > energy_surface:
            energy_blast = energy_atmosphere / (4.186 * 10**12)
        else:
            energy_blast = energy_surface / (4.186 * 10**12)
    
    return energy_blast, energy_surface

def cal_mass_of_water(impactor:Impactor, target:Target) -> float:
    """
    
    Arguments
    ---------
    
    
    Returns
    -------
    
    """
    
    mwater = (PI * impactor.get_pdiameter()**2 / 4) * (target.get_depth() / sin(impactor.get_theta() * PI / 180)) * 1000
    return mwater

def cal_velocity_projectile(impactor:Impactor, target:Target, velocity:float = None) -> float:
    """
    
    Arguments
    ---------
    
    
    Returns
    -------
    
    """
    
    if velocity == None:
        velocity = brust_velocity(impactor, target)
        
    vseafloor = velocity * exp(-(3 * 1000 * 0.877 * target.get_depth()) / (2 * impactor.get_density() * impactor.get_pdiameter() * sin(impactor.get_theta() * PI / 180)))
    return vseafloor

def cal_energy_at_seafloor(impactor:Impactor, target:Target, vseafloor: float = None) -> float:
    """
    
    Arguments
    ---------
    
    
    Returns
    -------
    
    """
    if vseafloor == None:
        vseafloor = cal_velocity_projectile(impactor, target)
    
    energy_seafloor = 0.5 * impactor.get_mass() * (vseafloor * 1000)**2
    return energy_seafloor

def cal_epicentral_angle(target:Target) -> float:
    """
    
    Arguments
    ---------
    
    
    Returns
    -------
    
    """
    
    return (180 / PI) * (target.get_distance()/target.get_R_earth())

def cal_wdiameter(impactor:Impactor, target:Target, velocity:float = None) -> float:
    """
    
    Arguments
    ---------
    
    
    Returns
    -------
    
    """
    if target.get_depth() == 0:
        raise ValueError("Target depth is 0")
    
    if velocity == None:
        velocity = brust_velocity(impactor, target)
    
    anglefac = (sin(impactor.get_theta() * PI / 180))**(1/3)
    if impactor.type == 1:
        Cd = 1.88
        beta = 0.22
    elif impactor.type == 2:
        Cd = 1.54
        beta = 0.165
    else:
        Cd = 1.6
        beta = 0.22
    
    mass, tdensity, g, pdiameter = impactor.get_mass(), impactor.get_density(), target.get_g(), impactor.get_pdiameter()
    
    
    wdiameter = 1.88 * (( mass / tdensity)**(1/3)) * ( (1.61*g*pdiameter)/(velocity*1000)**2)**(- 0.22)
    wdiameter *= anglefac
    
    # update tdensity which should be return as value
    logging.log(logging.INFO, "update the impactor density for seafloor: {}".format(wdiameter))
    impactor.set_density(2700)
    
    return wdiameter