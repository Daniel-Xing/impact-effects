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
from matplotlib.pyplot import flag

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
        exp(-altitudeBU / (2 * target.get_schaleHeight()))  # Assuming drag coefficient of 2

    if altitudeBurst > 0:
        # Evaluate Eq. 19 (without factor lL_0^2 lDisper * pdiameter**2)
        expfac = 1/24 * alpha2 * (24 + 8 * alpha2**2 + 6 * alpha2 * lDisper /
                                  target.get_schaleHeight() + 3 * alpha2**3 * lDisper / target.get_schaleHeight())

        # Evaluate velocity at burst using Eq. 17
        # (note that factor lDisper * pdiameter**2 in expfac cancels with same factor in vFac)
        velocity = vBU * exp(- expfac * vFac)
    else:
        # Define (l/H) for use in Eq. 20
        altitudeScale = target.get_schaleHeight() / lDisper

        # Evaluate Eq. 20 (without factor lL_0^2 lDisper * pdiameter**2)
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

def cal_ePIcentral_angle(target:Target) -> float:
    """
    
    Arguments
    ---------
    
    
    Returns
    -------
    
    """
    
    return (180 / PI) * (target.get_distance()/target.get_R_earth())

def cal_scaling_diameter_constant(impactor:Impactor) -> float:
    """
    
    Arguments
    ---------
    
    
    Returns
    -------
    
    """
    
    if impactor.type == 1:
        Cd = 1.88
        beta = 0.22
    elif impactor.type == 2:
        Cd = 1.54
        beta = 0.165
    else:
        Cd = 1.6
        beta = 0.22
    return Cd, beta


def cal_anglefac(impactor:Impactor) ->float:
    return (sin(impactor.get_theta() * PI / 180))**(1/3)


def cal_wdiameter(impactor:Impactor, target:Target, anglefac:float = None, velocity:float = None) -> float:
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
    
    if anglefac == None:
        anglefac = cal_anglefac(impactor)
    
    mass, tdensity, g, pdiameter = impactor.get_mass(), impactor.get_density(), target.get_g(), impactor.get_pdiameter()
    
    
    wdiameter = 1.88 * (( mass / tdensity)**(1/3)) * ( (1.61*g*pdiameter)/(velocity*1000)**2)**(- 0.22)
    wdiameter *= anglefac
    
    # update tdensity which should be return as value
    logging.log(logging.INFO, "update the impactor density for seafloor: {}".format(wdiameter))
    impactor.set_density(2700)
    
    return wdiameter

def cal_transient_crater_diameter(impactor:Impactor, target:Target, Cd:float = None, beta:float = None, anglefac:float = None, vseafloor:float = None) -> float:
    """
    
    Arguments
    ---------
    
    
    Returns
    -------
    
    """
    if Cd == None or beta ==None:
       Cd , beta =  cal_scaling_diameter_constant(impactor)
    
    if anglefac == None:
        anglefac = cal_anglefac(impactor)
        
    if vseafloor == None:
        vseafloor = cal_velocity_projectile(impactor, target)
        
    mass, tdensity, g, pdiameter = impactor.get_mass(), impactor.get_density(), target.get_g(), impactor.get_pdiameter()
    Dtr = Cd * ((mass / tdensity)**(1/3)) * ( (1.61*g*pdiameter)/(vseafloor*1000)**2)**(-beta)
    Dtr *= anglefac
    
    return Dtr
    

def cal_depthr(impactor:Impactor, target:Target, Dtr:float=None):
    if Dtr == None:
        Dtr = cal_transient_crater_diameter(impactor, target)
    
    return Dtr / 2.828

def cal_cdiamater(impactor:Impactor, target:Target, Dtr:float=None):
    if Dtr == None:
        Dtr = cal_transient_crater_diameter(impactor, target)
    
    if Dtr * 1.25  >= 3200:
        cdiameter = (1.17 * Dtr**1.13) / (3200**0.13)
    else:
        cdiameter = 1.25 * Dtr
    
    return cdiameter

def cal_depthfr(impactor:Impactor, target:Target, Dtr:float=None, depthtr:float = None, cdiameter:float=None):
    if Dtr == None:
        Dtr = cal_transient_crater_diameter(impactor, target)
    if depthtr == None:
        depthtr = cal_depthr(impactor, target, Dtr)
    if cdiameter == None:
        cdiameter = cal_cdiamater(impactor, target, Dtr)
    
    if Dtr * 1.25  >= 3200:
        depthfr = 37 * cdiameter**0.301
    else:
        #Breccia lens volume in m^3
        vbreccia = 0.032 * cdiameter**3		# in m^3
      
        #Rim height of final crater in m
        rimHeightf = 0.07 * Dtr**4 / cdiameter**3
      
        #Thickness of breccia lens in m
        brecciaThickness = 2.8 * vbreccia * ((depthtr + rimHeightf) / (depthtr * cdiameter**2))
      
        #Final crater depth (in m) = transient crater depth + final rim height - breccia thickness
        depthfr = depthtr + rimHeightf - brecciaThickness
    
    return depthfr


def cal_vCrater(impactor:Impactor, target:Target, Dtr:float = None) -> float:
    if Dtr == None:
        Dtr = cal_transient_crater_diameter(impactor, target)
    
    return (PI / 24) * (Dtr/1000)**3


def cal_vratio(impactor:Impactor, target:Target, vCrater:float = None, Dtr:float = None) -> float:
    if Dtr == None:
        Dtr = cal_transient_crater_diameter(impactor, target)
    if vCrater == None:
        vCrater = cal_vCrater(impactor, target, Dtr)
        

def cal_vCrater_vRation(impactor:Impactor, target:Target, Dtr:float = None) -> float:
    if Dtr == None:
        Dtr = cal_transient_crater_diameter(impactor, target)
    
    vCrater = (PI / 24) * (Dtr/1000)**3
    vRatio = vCrater / target.get_v_earth()
    return vCrater, vRatio

def cal_vMelt(impactor:Impactor, target:Target, velocity:float = None, energy_seafloor:float = None) -> float:
    if velocity == None:
        velocity = brust_velocity(impactor, target)
    
    if energy_seafloor == None:
        energy_seafloor = cal_energy_at_seafloor(impactor, target)
    
    if velocity < 12:
        raise ValueError("Velocity is less than 12 m/s")
    
    vMelt = target.get_melt_coeff() * (energy_seafloor) * sin(impactor.get_theta() * PI / 180)
    if vMelt > target.vEarth:
        vMelt = target.get_v_earth()
    
    return vMelt


def cal_mratio_and_mcratio(impactor:Impactor, target:Target, velocity:float = None, vMelt:float = None, vCrater:float = None, Dtr:float = None) -> float:
    if velocity == None:
        velocity = brust_velocity(impactor, target)
    
    if velocity < 12:
        raise ValueError("Velocity is less than 12 m/s")
    
    if Dtr == None:
        Dtr = cal_transient_crater_diameter(impactor, target)
    if vMelt == None:
        vMelt = cal_vMelt(impactor, target)
    if vCrater == None:
        vCrater = cal_vCrater(impactor, target, Dtr)
    
    mcratio = vMelt / vCrater
    mratio = vMelt / target.get_v_earth()
    return mratio, mcratio

def cal_eject_arrival(impactor:Impactor, target:Target, altitudeBurst:float = None):
    if altitudeBurst > 0:
        raise ValueError("Altitude of burst is greater than 0")
    
    phi = (target.get_distance()) / (2 * target.get_R_earth())
    X = (2 * tan(phi)) / (1 + tan(phi))
    e = -(0.5 * (X - 1)**2 + 0.5)**0.5 # eccentricity of eliptical path of the ejecta
    a = (X * target.get_R_earth() * 1000) / (2 * (1 - e**2))	# semi major axis of elliptical path
    
    part1 = a**1.5 / (g * (target.get_R_earth() * 1000)**2)**0.5
    term1 = 2* atan(((1 - e)/(1 + e))**0.5 * tan (phi / 2))
    term2 = e * (1 - e**2)**0.5 * sin (phi)/ (1 + e * cos(phi))
    ejecta_arrival = 2 * part1 * (term1 - term2)
    
    return ejecta_arrival

def cal_ejecta_thickness(impactor:Impactor, target:Target, altitudeBurst:float = None, Dtr:float = None):
    if altitudeBurst > 0:
        raise ValueError("Altitude of burst is greater than 0")
    
    ejecta_thickness = Dtr**4/(112 * (target.get_distance() * 1000)**3)
    return ejecta_thickness

def cal_themal(impactor:Impactor, target:Target, energy_surface:float =None, \
                    delta:float = None):
    eta = 3 * 10**-3	                ## factor for scaling thermal energy
    T_star = 3000		                ## temperature of fireball
    Rf = 2* 10**-6* (energy_surface)**(1/3)  ## Rf is in km
    sigma = 5.67 * 10**-8	                ## Stephan-Boltzmann constant
  
    thermal_exposure = (eta * energy_surface)/(2 * PI * (target.get_distance* 1000)**2)
  
    h = (1 - cos(delta * PI/180))* R_earth ## h is in km, R_earth is in km	
    Del = acos(h / Rf)
    f = (2/PI)*(Del - (h/Rf)*sin(Del))
  
    if h > Rf:
      no_radiation = 1
      return thermal_exposure, no_radiation
  
    no_radiation = 0
    thermal_exposure *= f
  
    max_rad_time = Rf / velocity           ## Rf in km / velocity in km/s
    irradiation_time = (eta * energy_surface)/(2 * PI * (Rf*1000)**2 * sigma * T_star**4)
  
    megaton_factor = (energy_megatons)**(1/6)

    thermal_power = log(thermal_exposure)/log(10)
    thermal_power = int(thermal_power)
    thermal_exposure /= 10**thermal_power