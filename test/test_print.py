import impactEffects.instances.ImpactorClass
from impactEffects.functions import *
from impactEffects.functions.function import *
from impactEffects.instances import ImpactorClass, TargetClass
from impactEffects.utils.print import print_airblast, print_change, print_crater, print_ejecta, print_energy, print_recurrencetime, print_atmospheric_entry, print_seismic, print_thermal, print_tsunami


def test_print_case1():
    impactor = impactEffects.instances.ImpactorClass.Impactor(
        diameter=111, density=111000, velocity=111, theta=45
    )
    targets = TargetClass.Target(depth=0, distance=111, density=2750)
    # cal_energy
    _kinetic_energy = kinetic_energy(impactor)
    _kinetic_energy_megatons = kinetic_energy_megatons(impactor)
    print_energy(_kinetic_energy, _kinetic_energy_megatons)

    _rec_time = rec_time(impactor)
    print(_rec_time)
    print_recurrencetime(_rec_time)

    # atmospheric_entry
    collins_iFactor, _av, _rStrength = iFactor(impactor, targets)
    print(collins_iFactor)

    altitudeBU, altitudeBurst, dispersion, energy_surface, energy_megatons = 0, 0, 0, 0, 0
    if collins_iFactor >= 1:
        velocity = burst_velocity_at_zero(impactor, targets)
    else:
        altitudeBU = altitude_of_breakup(impactor, targets)
        vBU = velocity_at_breakup(impactor, targets)

        lDisper = dispersion_length_scale(impactor, targets)

        altitudeBurst = airburst_altitude(impactor, targets)

        velocity = brust_velocity(impactor, targets)

        dispersion = dispersion_of_impactor(impactor, targets)

    lratio, pratio = fraction_of_momentum(impactor, targets)

    trot_change = cal_trot_change(impactor, targets)
    energy_atmosphere = cal_energy_atmosphere(impactor, targets)
    energy_blast, energy_surface = cal_energy_blast_surface(impactor, targets)

    mwater = cal_mass_of_water(impactor, targets)
    vseafloor = cal_velocity_projectile(impactor, targets)
    print("vseafloor", vseafloor)
    energy_seafloor = cal_energy_at_seafloor(impactor, targets)
    delta = cal_ePIcentral_angle(targets)
    # end_cal_energy

    # find_crater
    Cd, beta = cal_scaling_diameter_constant(target=targets)
    anglefac = cal_anglefac(impactor)

    wdiameter = 0
    if targets.depth != 0:
        wdiameter = cal_wdiameter(impactor, targets)

    Dtr = cal_transient_crater_diameter(impactor, targets)

    depthtr = cal_depthr(impactor, targets)

    cdiameter = cal_cdiamater(impactor, targets)

    depthfr = cal_depthfr(impactor, targets)
    brecciaThickness = cal_brecciaThickness(impactor, targets)

    vCrater, vRatio = cal_vCrater_vRation(impactor, targets)

    vMelt = cal_vMelt(impactor, targets)

    mratio, mcratio = cal_mratio_and_mcratio(impactor, targets)
    # end find_crater

    print_change(vRatio, mratio, lratio, trot_change, pratio)

    energy_megatons = energy_surface / (4.186 * 10**15)
    if impactor.get_mass() <= 1.5707963e12:
        print_atmospheric_entry(impactor.get_mass(), impactor.velocity, velocity, collins_iFactor, altitudeBU,
                                altitudeBurst, impactor.density, dispersion, impactor.theta, energy_surface, energy_megatons)

    if altitudeBurst <= 0:
        ejecta_arrival = cal_eject_arrival(impactor, targets)

        ejecta_thickness = cal_ejecta_thickness(impactor, targets)
        d_frag = cal_d_frag(impactor=impactor, target=targets,
                            cdiameter=cdiameter, altitudeBurst=altitudeBurst, Dtr=Dtr)

        if velocity >= 15:
            (
                h,
                Rf,
                thermal_exposure_,
                no_radiation_,
                max_rad_time_,
                irradiation_time_,
                megaton_factor_,
                thermal_power_,
            ) = cal_themal(impactor, targets)

        magnitude = cal_magnitude(impactor, targets)

        eff_mag, seismic_arrival = cal_magnitude2(impactor, targets)

        print_crater(vMelt, Dtr, targets.depth, wdiameter, impactor.pdiameter, dispersion,
                     collins_iFactor, depthtr, mratio, mcratio, cdiameter, depthfr, brecciaThickness, velocity)
        if targets.distance * 1000 <= Dtr/2:
            print_ejecta(energy_megatons, int(log(energy_megatons)/log(10)), targets.distance,
                         Rf, Dtr, cdiameter, ejecta_arrival, ejecta_thickness, d_frag)
            return

        print_thermal(velocity, no_radiation_, max_rad_time_, targets.distance, Rf,
                      h, thermal_power_, thermal_exposure_, irradiation_time_)
        print_seismic(magnitude, seismic_arrival)
        print_ejecta(energy_megatons, int(log(energy_megatons)/log(10)), targets.distance,
                     Rf, Dtr, cdiameter, ejecta_arrival, ejecta_thickness, d_frag)

    # Compute the effects of the airblast and print
    shock_arrival = cal_shock_arrival(impactor, targets)
    vmax, opressure = cal_vmax(impactor, targets)
    shock_damage = cal_shock_damage(
        impactor=impactor, target=targets, opressure=opressure, vmax=vmax)
    dec_level = cal_dec_level(impactor, targets)
    print_airblast(opressure, vmax, shock_arrival,
                   targets.distance, altitudeBurst, dec_level, shock_damage)

    # Compute the tsunami amplitude if water layer present
    if targets.depth > 0:
        TsunamiArrivalTime = cal_TsunamiArrivalTime(impactor, targets)
        WaveAmplitudeUpperLimit = cal_WaveAmplitudeUpperLimit(
            impactor, targets)
        WaveAmplitudeLowerLimit = cal_WaveAmplitudeLowerLimit(
            impactor, targets)
        print_tsunami(targets.distance, wdiameter, TsunamiArrivalTime,
                      WaveAmplitudeLowerLimit, WaveAmplitudeUpperLimit)


def test_print_case2():
    impactor = impactEffects.instances.ImpactorClass.Impactor(
        diameter=1000, density=3000, velocity=20, theta=45
    )
    targets = TargetClass.Target(depth=100, distance=100, density=1000)
    # cal_energy
    _kinetic_energy = kinetic_energy(impactor)
    _kinetic_energy_megatons = kinetic_energy_megatons(impactor)
    print_energy(_kinetic_energy, _kinetic_energy_megatons)

    _rec_time = rec_time(impactor)
    print(_rec_time)
    print_recurrencetime(_rec_time)

    # atmospheric_entry
    collins_iFactor, _av, _rStrength = iFactor(impactor, targets)
    print(collins_iFactor)

    altitudeBU, altitudeBurst, dispersion, energy_surface, energy_megatons = 0, 0, 0, 0, 0
    if collins_iFactor >= 1:
        velocity = burst_velocity_at_zero(impactor, targets)
    else:
        altitudeBU = altitude_of_breakup(impactor, targets)
        vBU = velocity_at_breakup(impactor, targets)

        lDisper = dispersion_length_scale(impactor, targets)

        altitudeBurst = airburst_altitude(impactor, targets)

        velocity = brust_velocity(impactor, targets)

        dispersion = dispersion_of_impactor(impactor, targets)

    lratio, pratio = fraction_of_momentum(impactor, targets)

    trot_change = cal_trot_change(impactor, targets)
    energy_atmosphere = cal_energy_atmosphere(impactor, targets)
    energy_blast, energy_surface = cal_energy_blast_surface(impactor, targets)

    mwater = cal_mass_of_water(impactor, targets)
    vseafloor = cal_velocity_projectile(impactor, targets)
    print("vseafloor", vseafloor)
    energy_seafloor = cal_energy_at_seafloor(impactor, targets)
    delta = cal_ePIcentral_angle(targets)
    # end_cal_energy

    # find_crater
    Cd, beta = cal_scaling_diameter_constant(target=targets)
    anglefac = cal_anglefac(impactor)

    wdiameter = 0
    if targets.depth != 0:
        wdiameter = cal_wdiameter(impactor, targets)

    Dtr = cal_transient_crater_diameter(impactor, targets)

    depthtr = cal_depthr(impactor, targets)

    cdiameter = cal_cdiamater(impactor, targets)

    depthfr = cal_depthfr(impactor, targets)
    brecciaThickness = cal_brecciaThickness(impactor, targets)

    vCrater, vRatio = cal_vCrater_vRation(impactor, targets)

    vMelt = cal_vMelt(impactor, targets)

    mratio, mcratio = cal_mratio_and_mcratio(impactor, targets)
    # end find_crater

    print_change(vRatio, mratio, lratio, trot_change, pratio)

    energy_megatons = energy_surface / (4.186 * 10**15)
    if impactor.get_mass() <= 1.5707963e12:
        print_atmospheric_entry(impactor.get_mass(), impactor.velocity, velocity, collins_iFactor, altitudeBU,
                                altitudeBurst, impactor.density, dispersion, impactor.theta, energy_surface, energy_megatons)

    if altitudeBurst <= 0:
        ejecta_arrival = cal_eject_arrival(impactor, targets)

        ejecta_thickness = cal_ejecta_thickness(impactor, targets)
        d_frag = cal_d_frag(impactor=impactor, target=targets,
                            cdiameter=cdiameter, altitudeBurst=altitudeBurst, Dtr=Dtr)

        if velocity >= 15:
            (
                h,
                Rf,
                thermal_exposure_,
                no_radiation_,
                max_rad_time_,
                irradiation_time_,
                megaton_factor_,
                thermal_power_,
            ) = cal_themal(impactor, targets)

        magnitude = cal_magnitude(impactor, targets)

        eff_mag, seismic_arrival = cal_magnitude2(impactor, targets)

        print_crater(vMelt, Dtr, targets.depth, wdiameter, impactor.pdiameter, dispersion,
                     collins_iFactor, depthtr, mratio, mcratio, cdiameter, depthfr, brecciaThickness, velocity)
        if targets.distance * 1000 <= Dtr/2:
            print_ejecta(energy_megatons, int(log(energy_megatons)/log(10)), targets.distance,
                         Rf, Dtr, cdiameter, ejecta_arrival, ejecta_thickness, d_frag)
            return

        print_thermal(velocity, no_radiation_, max_rad_time_, targets.distance, Rf,
                      h, thermal_power_, thermal_exposure_, irradiation_time_)
        print_seismic(magnitude, seismic_arrival)
        print_ejecta(energy_megatons, int(log(energy_megatons)/log(10)), targets.distance,
                     Rf, Dtr, cdiameter, ejecta_arrival, ejecta_thickness, d_frag)

    # Compute the effects of the airblast and print
    shock_arrival = cal_shock_arrival(impactor, targets)
    vmax, opressure = cal_vmax(impactor, targets)
    shock_damage = cal_shock_damage(
        impactor=impactor, target=targets, opressure=opressure, vmax=vmax)
    dec_level = cal_dec_level(impactor, targets)
    print_airblast(opressure, vmax, shock_arrival,
                   targets.distance, altitudeBurst, dec_level, shock_damage)

    # Compute the tsunami amplitude if water layer present
    if targets.depth > 0:
        TsunamiArrivalTime = cal_TsunamiArrivalTime(impactor, targets)
        WaveAmplitudeUpperLimit = cal_WaveAmplitudeUpperLimit(
            impactor, targets)
        WaveAmplitudeLowerLimit = cal_WaveAmplitudeLowerLimit(
            impactor, targets)
        print_tsunami(targets.distance, wdiameter, TsunamiArrivalTime,
                      WaveAmplitudeLowerLimit, WaveAmplitudeUpperLimit)
