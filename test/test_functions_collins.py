from turtle import distance
from impactEffects.functions import *
from impactEffects.functions.functions import *
from impactEffects.instances import *

## Case 1
# dist=75
# distanceUnits=1
# diam=111
# diameterUnits=1
# pdens=111
# pdens_select=0
# vel=111
# velocityUnits=1
# theta=45
# wdepth=
# wdepthUnits=1
# tdens=2500

def Test_Kinetic_energy():
    impactor = Impactor(diameter=111, density=111, velocity=111, 
                        theta=45, depth=0, type=3)
    targets = Targets(depth = 0, distance = 75)
    
    res = kinetic_energy(impactor, targets)
    
    assert res == None
    
def Test_kinetic_energy_megatons():
    impactor = Impactor(diameter=111, density=111, velocity=111, 
                        theta=45, depth=0, type=3)
    targets = Targets(depth = 0, distance = 75)
    
    res = kinetic_energy_megatons(impactor, targets)
    
    assert res == None
    
def Test_rec_time():
    impactor = Impactor(diameter=111, density=111, velocity=111, 
                        theta=45, depth=0, type=3)
    targets = Targets(depth = 0, distance = 75)
    
    res = rec_time(impactor, targets)
    
    assert res == None
    
def Test_iFactor():
    impactor = Impactor(diameter=111, density=111, velocity=111, 
                        theta=45, depth=0, type=3)
    targets = Targets(depth = 0, distance = 75)
    
    res = iFactor(impactor, targets)
    
    assert res == None
    
def Test_burst_velocity_at_zero():
    impactor = Impactor(diameter=111, density=111, velocity=111, 
                        theta=45, depth=0, type=3)
    targets = Targets(depth = 0, distance = 75)
    
    res = burst_velocity_at_zero(impactor, targets)
    
    assert res == None
    
def Test_altitude_of_breakup():
    impactor = Impactor(diameter=111, density=111, velocity=111, 
                        theta=45, depth=0, type=3)
    targets = Targets(depth = 0, distance = 75)
    
    res = altitude_of_breakup(impactor, targets)
    
    assert res == None
    
def Test_velocity_at_breakup():
    impactor = Impactor(diameter=111, density=111, velocity=111, 
                        theta=45, depth=0, type=3)
    targets = Targets(depth = 0, distance = 75)
    
    res = velocity_at_breakup(impactor, targets)
    
    assert res == None
    
def Test_dispersion_length_scale():
    impactor = Impactor(diameter=111, density=111, velocity=111, 
                        theta=45, depth=0, type=3)
    targets = Targets(depth = 0, distance = 75)
    
    res = dispersion_length_scale(impactor, targets)
    
    assert res == None
    
def Test_airburst_altitude():
    impactor = Impactor(diameter=111, density=111, velocity=111, 
                        theta=45, depth=0, type=3)
    targets = Targets(depth = 0, distance = 75)
    
    res = airburst_altitude(impactor, targets)
    
    assert res == None
    
def Test_brust_velocity():
    impactor = Impactor(diameter=111, density=111, velocity=111, 
                        theta=45, depth=0, type=3)
    targets = Targets(depth = 0, distance = 75)
    
    res = brust_velocity(impactor, targets)
    
    assert res == None
    
def Test_dispersion_of_impactor():
    impactor = Impactor(diameter=111, density=111, velocity=111, 
                        theta=45, depth=0, type=3)
    targets = Targets(depth = 0, distance = 75)
    
    res = dispersion_of_impactor(impactor, targets)
    
    assert res == None
    
def Test_fraction_of_momentum():
    impactor = Impactor(diameter=111, density=111, velocity=111, 
                        theta=45, depth=0, type=3)
    targets = Targets(depth = 0, distance = 75)
    
    res = fraction_of_momentum(impactor, targets)
    
    assert res == None
    
def Test_cal_trot_change():
    impactor = Impactor(diameter=111, density=111, velocity=111, 
                        theta=45, depth=0, type=3)
    targets = Targets(depth = 0, distance = 75)
    
    res = cal_trot_change(impactor, targets)
    
    assert res == None
    
def Test_cal_energy_atmosphere():
    impactor = Impactor(diameter=111, density=111, velocity=111, 
                        theta=45, depth=0, type=3)
    targets = Targets(depth = 0, distance = 75)
    
    res = cal_energy_atmosphere(impactor, targets)
    
    assert res == None
    
def Test_cal_energy_blast_surface():
    impactor = Impactor(diameter=111, density=111, velocity=111, 
                        theta=45, depth=0, type=3)
    targets = Targets(depth = 0, distance = 75)
    
    res = cal_energy_blast_surface(impactor, targets)
    
    assert res == None
    
def Test_cal_mass_of_water():
    impactor = Impactor(diameter=111, density=111, velocity=111, 
                        theta=45, depth=0, type=3)
    targets = Targets(depth = 0, distance = 75)
    
    res = cal_mass_of_water(impactor, targets)
    
    assert res == None
    
def Test_cal_velocity_projectile():
    impactor = Impactor(diameter=111, density=111, velocity=111, 
                        theta=45, depth=0, type=3)
    targets = Targets(depth = 0, distance = 75)
    
    res = cal_velocity_projectile(impactor, targets)
    
    assert res == None
    
def Test_cal_energy_at_seafloor():
    impactor = Impactor(diameter=111, density=111, velocity=111, 
                        theta=45, depth=0, type=3)
    targets = Targets(depth = 0, distance = 75)
    
    res = cal_energy_at_seafloor(impactor, targets)
    
    assert res == None
    
def Test_cal_ePIcentral_angle():
    impactor = Impactor(diameter=111, density=111, velocity=111, 
                        theta=45, depth=0, type=3)
    targets = Targets(depth = 0, distance = 75)
    
    res = cal_ePIcentral_angle(impactor, targets)
    
    assert res == None
    
def Test_cal_scaling_diameter_constant():
    impactor = Impactor(diameter=111, density=111, velocity=111, 
                        theta=45, depth=0, type=3)
    targets = Targets(depth = 0, distance = 75)
    
    res = cal_scaling_diameter_constant(impactor, targets)
    
    assert res == None
    
def Test_cal_anglefac():
    impactor = Impactor(diameter=111, density=111, velocity=111, 
                        theta=45, depth=0, type=3)
    targets = Targets(depth = 0, distance = 75)
    
    res = cal_anglefac(impactor, targets)
    
    assert res == None
    
def Test_cal_wdiameter():
    impactor = Impactor(diameter=111, density=111, velocity=111, 
                        theta=45, depth=0, type=3)
    targets = Targets(depth = 0, distance = 75)
    
    res = cal_wdiameter(impactor, targets)
    
    assert res == None
    
def Test_Kinetic_energy():
    impactor = Impactor(diameter=111, density=111, velocity=111, 
                        theta=45, depth=0, type=3)
    targets = Targets(depth = 0, distance = 75)
    
    res = kinetic_energy(impactor, targets)
    
    assert res == None
    
def Test_cal_transient_crater_diameter():
    impactor = Impactor(diameter=111, density=111, velocity=111, 
                        theta=45, depth=0, type=3)
    targets = Targets(depth = 0, distance = 75)
    
    res = cal_transient_crater_diameter(impactor, targets)
    
    assert res == None
    
def Test_cal_depthr():
    impactor = Impactor(diameter=111, density=111, velocity=111, 
                        theta=45, depth=0, type=3)
    targets = Targets(depth = 0, distance = 75)
    
    res = cal_depthr(impactor, targets)
    
    assert res == None
    
def Test_cal_cdiamater():
    impactor = Impactor(diameter=111, density=111, velocity=111, 
                        theta=45, depth=0, type=3)
    targets = Targets(depth = 0, distance = 75)
    
    res = cal_cdiamater(impactor, targets)
    
    assert res == None
    
def Test_cal_depthfr():
    impactor = Impactor(diameter=111, density=111, velocity=111, 
                        theta=45, depth=0, type=3)
    targets = Targets(depth = 0, distance = 75)
    
    res = cal_depthfr(impactor, targets)
    
    assert res == None
    
def Test_cal_vCrater():
    impactor = Impactor(diameter=111, density=111, velocity=111, 
                        theta=45, depth=0, type=3)
    targets = Targets(depth = 0, distance = 75)
    
    res = cal_vCrater(impactor, targets)
    
    assert res == None
    
def Test_cal_vratio():
    impactor = Impactor(diameter=111, density=111, velocity=111, 
                        theta=45, depth=0, type=3)
    targets = Targets(depth = 0, distance = 75)
    
    res = cal_vratio(impactor, targets)
    
    assert res == None
    
def Test_cal_vCrater_vRation():
    impactor = Impactor(diameter=111, density=111, velocity=111, 
                        theta=45, depth=0, type=3)
    targets = Targets(depth = 0, distance = 75)
    
    res = cal_vCrater_vRation(impactor, targets)
    
    assert res == None
    
def Test_cal_vMelt():
    impactor = Impactor(diameter=111, density=111, velocity=111, 
                        theta=45, depth=0, type=3)
    targets = Targets(depth = 0, distance = 75)
    
    res = cal_vMelt(impactor, targets)
    
    assert res == None
    
def Test_cal_mratio_and_mcratio():
    impactor = Impactor(diameter=111, density=111, velocity=111, 
                        theta=45, depth=0, type=3)
    targets = Targets(depth = 0, distance = 75)
    
    res = cal_mratio_and_mcratio(impactor, targets)
    
    assert res == None
    
def Test_cal_eject_arrival():
    impactor = Impactor(diameter=111, density=111, velocity=111, 
                        theta=45, depth=0, type=3)
    targets = Targets(depth = 0, distance = 75)
    
    res = cal_eject_arrival(impactor, targets)
    
    assert res == None
    
def Test_cal_ejecta_thickness():
    impactor = Impactor(diameter=111, density=111, velocity=111, 
                        theta=45, depth=0, type=3)
    targets = Targets(depth = 0, distance = 75)
    
    res = cal_ejecta_thickness(impactor, targets)
    
    assert res == None
    
def Test_cal_themal():
    impactor = Impactor(diameter=111, density=111, velocity=111, 
                        theta=45, depth=0, type=3)
    targets = Targets(depth = 0, distance = 75)
    
    res = cal_themal(impactor, targets)
    
    assert res == None
    
def Test_cal_magnitude():
    impactor = Impactor(diameter=111, density=111, velocity=111, 
                        theta=45, depth=0, type=3)
    targets = Targets(depth = 0, distance = 75)
    
    res = cal_magnitude(impactor, targets)
    
    assert res == None
    
def Test_cal_magnitude2():
    impactor = Impactor(diameter=111, density=111, velocity=111, 
                        theta=45, depth=0, type=3)
    targets = Targets(depth = 0, distance = 75)
    
    res = cal_magnitude2(impactor, targets)
    
    assert res == None
    
def Test_cal_shock_arrival():
    impactor = Impactor(diameter=111, density=111, velocity=111, 
                        theta=45, depth=0, type=3)
    targets = Targets(depth = 0, distance = 75)
    
    res = cal_shock_arrival(impactor, targets)
    
    assert res == None
    
def Test_cal_vmax():
    impactor = Impactor(diameter=111, density=111, velocity=111, 
                        theta=45, depth=0, type=3)
    targets = Targets(depth = 0, distance = 75)
    
    res = cal_vmax(impactor, targets)
    
    assert res == None
    
def Test_cal_dec_level():
    impactor = Impactor(diameter=111, density=111, velocity=111, 
                        theta=45, depth=0, type=3)
    targets = Targets(depth = 0, distance = 75)
    
    res = cal_dec_level(impactor, targets)
    
    assert res == None
    
def Test_cal_TsunamiArrivalTime():
    impactor = Impactor(diameter=111, density=111, velocity=111, 
                        theta=45, depth=0, type=3)
    targets = Targets(depth = 0, distance = 75)
    
    res = cal_TsunamiArrivalTime(impactor, targets)
    
    assert res == None
    
def Test_cal_WaveAmplitudeUpperLimit():
    impactor = Impactor(diameter=111, density=111, velocity=111, 
                        theta=45, depth=0, type=3)
    targets = Targets(depth = 0, distance = 75)
    
    res = cal_WaveAmplitudeUpperLimit(impactor, targets)
    
    assert res == None
    
def Test_cal_WaveAmplitudeLowerLimit():
    impactor = Impactor(diameter=111, density=111, velocity=111, 
                        theta=45, depth=0, type=3)
    targets = Targets(depth = 0, distance = 75)
    
    res = cal_WaveAmplitudeLowerLimit(impactor, targets)
    
    assert res == None