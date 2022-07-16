import numpy as np
import impactEffects.instances.ImpactorClass
from impactEffects.functions import *
from impactEffects.functions.functions import *
from impactEffects.instances import ImpactorClass, TargetClass

mass = 79485913.655865
energy0 = 4.89672971076956e+17
energy0_megatons = 116.978731743181
rec_time_ = 4303.63077758262
i_Factor = 1.76668348132175e-07
altitudeBU = 134913.980633488
vBU = 110999.992750236
lDisper = 2685214.70569087
altitudeBurst = 21963.7818243691
velocity = 12175.8027204639
linmom = 967804803729.638
angmom = 4.35925722505549e+15
new_energy0 = 4.89672971076956e+17
lratio = 7.43900550350766e-19
pratio = 5.39467560607379e-21
trot_change = 5.3449948652072e-11
energy_atmosphere = 4.83781070895892e+17
energy_blast = 115571.206616314
energy_surface = 4.83781070895892e+17
mwater = 0
vseafloor = 12.1758027204639
energy_seafloor = 5.89190018106467e+15
delta = 0.674597659836708
anglefac = 0.890898521133585
Cd = 1.6
beta = 0.22
Dtr = 548.034713703502
depthtr = 193.788795510432
cdiameter = 685.043392129377
depthfr = 145.829281255601
vCrater = 0.0215457923352441
vratio = 1.9587083941131e-14
vMelt = 3.70791782934784e-05
mratio = 3.37083439031622e-17
mcratio = 0.00172094753892272
shock_arrival = 236.817895112731
vmax = 14.6105435123175
dec_level = 76.0763196239768


def test_Kinetic_energy():
    impactor = impactEffects.instances.ImpactorClass.Impactor(diameter=111, density=111, velocity=111,
                                                              theta=45, depth=0, ttype=3)
    targets = TargetClass.Target(depth=0, distance=75)

    res = kinetic_energy(impactor)

    assert np.allclose(res, energy0)


def test_kinetic_energy_megatons():
    impactor = impactEffects.instances.ImpactorClass.Impactor(diameter=111, density=111, velocity=111,
                             theta=45, depth=0, ttype=3)
    targets = TargetClass.Target(depth=0, distance=75)

    res = kinetic_energy_megatons(impactor)

    assert np.allclose(res, energy0_megatons)


def test_rec_time():
    impactor = impactEffects.instances.ImpactorClass.Impactor(diameter=111, density=111, velocity=111,
                             theta=45, depth=0, ttype=3)
    targets = TargetClass.Target(depth=0, distance=75)

    res = rec_time(impactor)

    assert np.allclose(res, rec_time_)


def test_iFactor():
    impactor = impactEffects.instances.ImpactorClass.Impactor(diameter=111, density=111, velocity=111,
                             theta=45, depth=0, ttype=3)
    targets = TargetClass.Target(depth=0, distance=75)

    collins_iFactor, _av, _rStrength = iFactor(impactor, targets)

    assert np.allclose(collins_iFactor, i_Factor)


def test_burst_velocity_at_zero():
    impactor = impactEffects.instances.ImpactorClass.Impactor(diameter=111, density=111, velocity=111,
                             theta=45, depth=0, ttype=3)
    targets = TargetClass.Target(depth=0, distance=75)

    res = burst_velocity_at_zero(impactor, targets)



def test_altitude_of_breakup():
    impactor = impactEffects.instances.ImpactorClass.Impactor(diameter=111, density=111, velocity=111,
                             theta=45, depth=0, ttype=3)
    targets = TargetClass.Target(depth=0, distance=75)

    res = altitude_of_breakup(impactor, targets)



def test_velocity_at_breakup():
    impactor = impactEffects.instances.ImpactorClass.Impactor(diameter=111, density=111, velocity=111,
                             theta=45, depth=0, ttype=3)
    targets = TargetClass.Target(depth=0, distance=75)

    res = velocity_at_breakup(impactor, targets)



def test_dispersion_length_scale():
    impactor = impactEffects.instances.ImpactorClass.Impactor(diameter=111, density=111, velocity=111,
                             theta=45, depth=0, ttype=3)
    targets = TargetClass.Target(depth=0, distance=75)

    res = dispersion_length_scale(impactor, targets)



def test_airburst_altitude():
    impactor = impactEffects.instances.ImpactorClass.Impactor(diameter=111, density=111, velocity=111,
                             theta=45, depth=0, ttype=3)
    targets = TargetClass.Target(depth=0, distance=75)

    res = airburst_altitude(impactor, targets)



def test_brust_velocity():
    impactor = impactEffects.instances.ImpactorClass.Impactor(diameter=111, density=111, velocity=111,
                             theta=45, depth=0, ttype=3)
    targets = TargetClass.Target(depth=0, distance=75)

    res = brust_velocity(impactor, targets)



def test_dispersion_of_impactor():
    impactor = impactEffects.instances.ImpactorClass.Impactor(diameter=111, density=111, velocity=111,
                             theta=45, depth=0, ttype=3)
    targets = TargetClass.Target(depth=0, distance=75)

    res = dispersion_of_impactor(impactor, targets)



def test_fraction_of_momentum():
    impactor = impactEffects.instances.ImpactorClass.Impactor(diameter=111, density=111, velocity=111,
                             theta=45, depth=0, ttype=3)
    targets = TargetClass.Target(depth=0, distance=75)

    res = fraction_of_momentum(impactor, targets)



def test_cal_trot_change():
    impactor = impactEffects.instances.ImpactorClass.Impactor(diameter=111, density=111, velocity=111,
                             theta=45, depth=0, ttype=3)
    targets = TargetClass.Target(depth=0, distance=75)

    res = cal_trot_change(impactor, targets)



def test_cal_energy_atmosphere():
    impactor = impactEffects.instances.ImpactorClass.Impactor(diameter=111, density=111, velocity=111,
                             theta=45, depth=0, ttype=3)
    targets = TargetClass.Target(depth=0, distance=75)

    res = cal_energy_atmosphere(impactor, targets)



def test_cal_energy_blast_surface():
    impactor = impactEffects.instances.ImpactorClass.Impactor(diameter=111, density=111, velocity=111,
                             theta=45, depth=0, ttype=3)
    targets = TargetClass.Target(depth=0, distance=75)

    res = cal_energy_blast_surface(impactor, targets)



def test_cal_mass_of_water():
    impactor = impactEffects.instances.ImpactorClass.Impactor(diameter=111, density=111, velocity=111,
                             theta=45, depth=0, ttype=3)
    targets = TargetClass.Target(depth=0, distance=75)

    res = cal_mass_of_water(impactor, targets)



def test_cal_velocity_projectile():
    impactor = impactEffects.instances.ImpactorClass.Impactor(diameter=111, density=111, velocity=111,
                             theta=45, depth=0, ttype=3)
    targets = TargetClass.Target(depth=0, distance=75)

    res = cal_velocity_projectile(impactor, targets)



def test_cal_energy_at_seafloor():
    impactor = impactEffects.instances.ImpactorClass.Impactor(diameter=111, density=111, velocity=111,
                             theta=45, depth=0, ttype=3)
    targets = TargetClass.Target(depth=0, distance=75)

    res = cal_energy_at_seafloor(impactor, targets)



def test_cal_ePIcentral_angle():
    impactor = impactEffects.instances.ImpactorClass.Impactor(diameter=111, density=111, velocity=111,
                             theta=45, depth=0, ttype=3)
    targets = TargetClass.Target(depth=0, distance=75)

    res = cal_ePIcentral_angle(impactor, targets)



def test_cal_scaling_diameter_constant():
    impactor = impactEffects.instances.ImpactorClass.Impactor(diameter=111, density=111, velocity=111,
                             theta=45, depth=0, ttype=3)
    targets = TargetClass.Target(depth=0, distance=75)

    res = cal_scaling_diameter_constant(impactor, targets)



def test_cal_anglefac():
    impactor = impactEffects.instances.ImpactorClass.Impactor(diameter=111, density=111, velocity=111,
                             theta=45, depth=0, ttype=3)
    targets = TargetClass.Target(depth=0, distance=75)

    res = cal_anglefac(impactor, targets)



def test_cal_wdiameter():
    impactor = impactEffects.instances.ImpactorClass.Impactor(diameter=111, density=111, velocity=111,
                             theta=45, depth=0, ttype=3)
    targets = TargetClass.Target(depth=0, distance=75)

    res = cal_wdiameter(impactor, targets)



def test_Kinetic_energy():
    impactor = impactEffects.instances.ImpactorClass.Impactor(diameter=111, density=111, velocity=111,
                             theta=45, depth=0, ttype=3)
    targets = TargetClass.Target(depth=0, distance=75)

    res = kinetic_energy(impactor, targets)



def test_cal_transient_crater_diameter():
    impactor = impactEffects.instances.ImpactorClass.Impactor(diameter=111, density=111, velocity=111,
                             theta=45, depth=0, ttype=3)
    targets = TargetClass.Target(depth=0, distance=75)

    res = cal_transient_crater_diameter(impactor, targets)



def test_cal_depthr():
    impactor = impactEffects.instances.ImpactorClass.Impactor(diameter=111, density=111, velocity=111,
                             theta=45, depth=0, ttype=3)
    targets = TargetClass.Target(depth=0, distance=75)

    res = cal_depthr(impactor, targets)



def test_cal_cdiamater():
    impactor = impactEffects.instances.ImpactorClass.Impactor(diameter=111, density=111, velocity=111,
                             theta=45, depth=0, ttype=3)
    targets = TargetClass.Target(depth=0, distance=75)

    res = cal_cdiamater(impactor, targets)



def test_cal_depthfr():
    impactor = impactEffects.instances.ImpactorClass.Impactor(diameter=111, density=111, velocity=111,
                             theta=45, depth=0, ttype=3)
    targets = TargetClass.Target(depth=0, distance=75)

    res = cal_depthfr(impactor, targets)



def test_cal_vCrater():
    impactor = impactEffects.instances.ImpactorClass.Impactor(diameter=111, density=111, velocity=111,
                             theta=45, depth=0, ttype=3)
    targets = TargetClass.Target(depth=0, distance=75)

    res = cal_vCrater(impactor, targets)



def test_cal_vratio():
    impactor = impactEffects.instances.ImpactorClass.Impactor(diameter=111, density=111, velocity=111,
                             theta=45, depth=0, ttype=3)
    targets = TargetClass.Target(depth=0, distance=75)

    res = cal_vratio(impactor, targets)



def test_cal_vCrater_vRation():
    impactor = impactEffects.instances.ImpactorClass.Impactor(diameter=111, density=111, velocity=111,
                             theta=45, depth=0, ttype=3)
    targets = TargetClass.Target(depth=0, distance=75)

    res = cal_vCrater_vRation(impactor, targets)



def test_cal_vMelt():
    impactor = impactEffects.instances.ImpactorClass.Impactor(diameter=111, density=111, velocity=111,
                             theta=45, depth=0, ttype=3)
    targets = TargetClass.Target(depth=0, distance=75)

    res = cal_vMelt(impactor, targets)



def test_cal_mratio_and_mcratio():
    impactor = impactEffects.instances.ImpactorClass.Impactor(diameter=111, density=111, velocity=111,
                             theta=45, depth=0, ttype=3)
    targets = TargetClass.Target(depth=0, distance=75)

    res = cal_mratio_and_mcratio(impactor, targets)



def test_cal_eject_arrival():
    impactor = impactEffects.instances.ImpactorClass.Impactor(diameter=111, density=111, velocity=111,
                             theta=45, depth=0, ttype=3)
    targets = TargetClass.Target(depth=0, distance=75)

    res = cal_eject_arrival(impactor, targets)



def test_cal_ejecta_thickness():
    impactor = impactEffects.instances.ImpactorClass.Impactor(diameter=111, density=111, velocity=111,
                             theta=45, depth=0, ttype=3)
    targets = TargetClass.Target(depth=0, distance=75)

    res = cal_ejecta_thickness(impactor, targets)



def test_cal_themal():
    impactor = impactEffects.instances.ImpactorClass.Impactor(diameter=111, density=111, velocity=111,
                             theta=45, depth=0, ttype=3)
    targets = TargetClass.Target(depth=0, distance=75)

    res = cal_themal(impactor, targets)



def test_cal_magnitude():
    impactor = impactEffects.instances.ImpactorClass.Impactor(diameter=111, density=111, velocity=111,
                             theta=45, depth=0, ttype=3)
    targets = TargetClass.Target(depth=0, distance=75)

    res = cal_magnitude(impactor, targets)



def test_cal_magnitude2():
    impactor = impactEffects.instances.ImpactorClass.Impactor(diameter=111, density=111, velocity=111,
                             theta=45, depth=0, ttype=3)
    targets = TargetClass.Target(depth=0, distance=75)

    res = cal_magnitude2(impactor, targets)



def test_cal_shock_arrival():
    impactor = impactEffects.instances.ImpactorClass.Impactor(diameter=111, density=111, velocity=111,
                             theta=45, depth=0, ttype=3)
    targets = TargetClass.Target(depth=0, distance=75)

    res = cal_shock_arrival(impactor, targets)



def test_cal_vmax():
    impactor = impactEffects.instances.ImpactorClass.Impactor(diameter=111, density=111, velocity=111,
                             theta=45, depth=0, ttype=3)
    targets = TargetClass.Target(depth=0, distance=75)

    res = cal_vmax(impactor, targets)
    assert np.allclose(res, vmax)



def test_cal_dec_level():
    impactor = impactEffects.instances.ImpactorClass.Impactor(diameter=111, density=111, velocity=111,
                             theta=45, depth=0, ttype=3)
    targets = TargetClass.Target(depth=0, distance=75)

    res = cal_dec_level(impactor, targets)
    
    assert np.allclose(res, dec_level)



def test_cal_TsunamiArrivalTime():
    impactor = impactEffects.instances.ImpactorClass.Impactor(diameter=111, density=111, velocity=111,
                             theta=45, depth=0, ttype=3)
    targets = TargetClass.Target(depth=0, distance=75)

    res = cal_TsunamiArrivalTime(impactor, targets)



def test_cal_WaveAmplitudeUpperLimit():
    impactor = impactEffects.instances.ImpactorClass.Impactor(diameter=111, density=111, velocity=111,
                             theta=45, depth=0, ttype=3)
    targets = TargetClass.Target(depth=0, distance=75)

    res = cal_WaveAmplitudeUpperLimit(impactor, targets)



def test_cal_WaveAmplitudeLowerLimit():
    impactor = impactEffects.instances.ImpactorClass.Impactor(diameter=111, density=111, velocity=111,
                             theta=45, depth=0, ttype=3)
    targets = TargetClass.Target(depth=0, distance=75)

    res = cal_WaveAmplitudeLowerLimit(impactor, targets)

