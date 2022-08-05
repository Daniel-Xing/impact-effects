from sre_compile import dis
from this import d
from impactEffects.core.config import *


def print_energy(energy0, energy0_megatons):
    discribe = ""
    energy_power = log(energy0) / log(10)
    energy_power = int(energy_power)
    energy0 /= 10 ** energy_power

    megaton_power = log(energy0_megatons) / log(10)
    megaton_power = int(megaton_power)
    energy0_megatons /= 10 ** megaton_power

    # Print the energy
    if energy_power == 0:
        print(
            "Energy before atmospheric entry: %.2f Joules " % (energy0),
            end="",
        )
        discribe += "Energy before atmospheric entry: %.2f Joules " % (
            energy0) + "/n"
    else:
        print(
            "Energy before atmospheric entry: %.2f x 10^%.0f Joules "
            % (energy0, energy_power),
            end="",
        )
        discribe += "Energy before atmospheric entry: %.2f x 10^%.0f Joules " % (
            energy0, energy_power) + "/n"

    if megaton_power == 0:
        if energy0_megatons < 1:
            print(
                " = %.2f KiloTons TNT" % (energy0_megatons * 1000), end=""
            )
            discribe += " = %.2f KiloTons TNT" % (
                energy0_megatons * 1000) + "/n"
        else:
            print(" = %.2f MegaTons TNT" % (energy0_megatons), end="")
            discribe += " = %.2f MegaTons TNT" % (energy0_megatons) + "/n"
    else:
        print(
            " = %.2f x 10^%.0f MegaTons TNT"
            % (energy0_megatons, megaton_power),
            end="",
        )
        discribe += " = %.2f x 10^%.0f MegaTons TNT" % (
            energy0_megatons, megaton_power) + "/n"

    print("\n")
    return discribe


def print_recurrencetime(rec_time):
    discribe = ""
    # Use scientific notation for recurrence times longer than 1000 years
    if rec_time > 1000:
        rec_time_p = log(rec_time) / log(10)
        rec_time_p = int(rec_time_p)
        rec_time /= 10 ** rec_time_p

        if rec_time * 10 ** rec_time_p < 4.5e9:
            print(
                "The average interval between impacts of this size somewhere on Earth during the last 4 billion years is %.1f x 10^%.0fyears."
                % (rec_time, rec_time_p)
            )
            discribe += "The average interval between impacts of this size somewhere on Earth during the last 4 billion years is %.1f x 10^%.0fyears." % (
                rec_time, rec_time_p) + "/n"
        else:
            print(
                "The average interval between impacts of this size is longer than the Earth's age."
            )
            discribe += "The average interval between impacts of this size is longer than the Earth's age." + "/n"
            print(
                "Such impacts could only occur during the accumulation of the Earth, between 4.5 and 4 billion years ago."
            )
            discribe += "Such impacts could only occur during the accumulation of the Earth, between 4.5 and 4 billion years ago." + "/n"

        return discribe

    # Use normal notation for intervals less than 1000 years
    if rec_time * 12 < 1:
        print(
            "The average interval between impacts of this size somewhere on Earth is less than 1 month."
        )
        discribe += "The average interval between impacts of this size somewhere on Earth is less than 1 month." + "/n"

    else:
        print(
            "The average interval between impacts of this size somewhere on Earth is %.1f years."
            % (rec_time)
        )
        discribe += "The average interval between impacts of this size somewhere on Earth is %.1f years." % (
            rec_time) + "/n"
    print("")
    return discribe


def print_change(vratio, mratio, lratio, trot_change, pratio):
    print("Major Global Changes:")
    discribe = ""

    if vratio >= 0.1:
        if vratio >= 0.5:
            print(
                "The Earth is completely disrupted by the impact and its debris forms a new asteroid belt orbiting the sun between Venus and Mars."
            )
            discribe += "The Earth is completely disrupted by the impact and its debris forms a new asteroid belt orbiting the sun between Venus and Mars." + "/n"

        else:
            print(
                "The Earth is strongly disturbed by the impact, but loses little mass."
            )
            discribe += "The Earth is strongly disturbed by the impact, but loses little mass." + "/n"
    else:
        print(
            "The Earth is not strongly disturbed by the impact and loses negligible mass."
        )
        discribe += "The Earth is not strongly disturbed by the impact and loses negligible mass." + "/n"

    if mratio >= 0.01:
        print("%.2f percent of the Earth is melted" % (mratio * 100))
        discribe += "%.2f percent of the Earth is melted" % (
            mratio * 100) + "/n"

    if lratio >= 0.001:
        print("Depending on the direction and location the collision, ")
        discribe += "Depending on the direction and location the collision, " + "/n"
        if lratio < 0.01:
            print(
                "the impact may make a very small change in the tilt of Earth's axis (< half a degree)."
            )
            discribe += "the impact may make a very small change in the tilt of Earth's axis (< half a degree)." + "/n"
        elif lratio < 0.1:
            print(
                "the impact may make a noticeable change in the tilt of Earth's axis (< 5 degrees)."
            )
            discribe += "the impact may make a noticeable change in the tilt of Earth's axis (< 5 degrees)." + "/n"
        elif lratio < 1.0:
            print(
                "the impact may make a significant change in the tilt of Earth's axis."
            )
            discribe += "the impact may make a significant change in the tilt of Earth's axis." + "/n"
        else:
            print(
                "the impact may totally change the Earth's rotation period and the tilt of its axis."
            )
            discribe += "the impact may totally change the Earth's rotation period and the tilt of its axis." + "/n"
    else:
        print(
            "The impact does not make a noticeable change in the tilt of Earth's axis (< 5 hundreths of a degree)."
        )
        discribe += "The impact does not make a noticeable change in the tilt of Earth's axis (< 5 hundreths of a degree)." + "/n"

    # Print the change in length of the day if more than one second
    if trot_change > 1e-3:
        print(
            "Depending on the direction and location of impact, the collision may cause a change in the length of the day of up to %f unit."
            % (trot_change)
        )
        discribe += "Depending on the direction and location of impact, the collision may cause a change in the length of the day of up to %f unit." % (
            trot_change) + "/n"
    if pratio >= 0.001:
        if pratio < 0.01:
            print("The impact shifts the Earth's orbit noticeably.")
            discribe += "The impact shifts the Earth's orbit noticeably." + "/n"
        elif pratio < 0.1:
            print("The imapct shifts the Earth's orbit substantially.")
            discirbe += "The imapct shifts the Earth's orbit substantially." + "/n"
        else:
            print("The impact shifts the Earth's orbit totally.")
            discribe += "The impact shifts the Earth's orbit totally." + "/n"

    else:
        print("The impact does not shift the Earth's orbit noticeably.")
        discribe += "The impact does not shift the Earth's orbit noticeably." + "/n"

    print("")
    return discribe


def print_atmospheric_entry(
    mass,
    vInput,
    velocity,
    iFactor,
    altitudeBU,
    altitudeBurst,
    pdensity,
    dispersion,
    theta,
    energy_surface,
    energy_megatons,
):
    print("Atmospheric Entry:")

    en = 0.5 * mass * ((vInput * 1000) ** 2 - (velocity * 1000) ** 2)

    en_mton = en / (4.186 * 10 ** 15)  # joules to megatons conversion

    en_power = log(en) / log(10)
    en_power = int(en_power)
    en /= 10 ** en_power

    ens_power = log(energy_surface) / log(10)
    ens_power = int(ens_power)
    energy_surface /= 10 ** ens_power

    enmton_power = log(en_mton) / log(10)
    enmton_power = int(enmton_power)
    en_mton /= 10 ** enmton_power

    megaton_power = log(energy_megatons) / log(10)
    megaton_power = int(megaton_power)
    energy_megatons /= 10 ** megaton_power

    discribe = ""

    if iFactor >= 1:
        print(
            "The projectile lands intact, with a velocity %f km/s = %f miles/s."
            % (velocity, velocity * 0.621)
        )
        discribe += "The projectile lands intact, with a velocity %f km/s = %f miles/s." % (
            velocity, velocity * 0.621) + "/n"
        print(
            "The energy lost in the atmosphere is %.2f x 10^%.0f Joules = %.2f x 10^%.0f MegaTons."
            % (en, en_power, en_mton, enmton_power)
        )
        discribe += "The energy lost in the atmosphere is %.2f x 10^%.0f Joules = %.2f x 10^%.0f MegaTons." % (
            en, en_power, en_mton, enmton_power) + "/n"
    else:
        print(
            "The projectile begins to breakup at an altitude of %f meters = %f ft"
            % (altitudeBU, altitudeBU * 3.28)
        )
        discribe += "The projectile begins to breakup at an altitude of %f meters = %f ft" % (
            altitudeBU, altitudeBU * 3.28) + "/n"
        if altitudeBurst > 0:
            print(
                "The projectile bursts into a cloud of fragments at an altitude of %f meters = %f ft"
                % (altitudeBurst, altitudeBurst * 3.28)
            )
            discribe += "The projectile bursts into a cloud of fragments at an altitude of %f meters = %f ft" % (
                altitudeBurst, altitudeBurst * 3.28) + "/n"
            print(
                "The residual velocity of the projectile fragments after the burst is %f km/s = %f miles/s"
                % (velocity, velocity * 0.621)
            )
            discribe += "The residual velocity of the projectile fragments after the burst is %f km/s = %f miles/s" % (
                velocity, velocity * 0.621) + "/n"
            print(
                "The energy of the airburst is %.2f x 10^%.0f Joules = %.2f x 10^%.0f MegaTons."
                % (en, en_power, en_mton, enmton_power)
            )
            discribe += "The energy of the airburst is %.2f x 10^%.0f Joules = %.2f x 10^%.0f MegaTons." % (
                en, en_power, en_mton, enmton_power) + "/n"
            if pdensity < 5000:
                print(
                    "No crater is formed, although large fragments may strike the surface."
                )
                discribe += "No crater is formed, although large fragments may strike the surface." + "/n"
            else:
                print(
                    "Large fragments strike the surface and may create a crater strewn field.  A more careful treatment of atmospheric entry is required to accurately estimate the size-frequency distribution of meteoroid fragments and predict the number and size of craters formed."
                )
                discribe += "Large fragments strike the surface and may create a crater strewn field.  A more careful treatment of atmospheric entry is required to accurately estimate the size-frequency distribution of meteoroid fragments and predict the number and size of craters formed." + "/n"

        else:
            print(
                "The projectile reaches the ground in a broken condition.  The mass of projectile strikes the surface at velocity %f km/s = %f miles/s"
                % (velocity, velocity * 0.621)
            )
            discribe += "The projectile reaches the ground in a broken condition.  The mass of projectile strikes the surface at velocity %f km/s = %f miles/s" % (
                velocity, velocity * 0.621) + "/n"
            print(
                "The energy lost in the atmosphere is %.2f x 10^%.0f Joules = %.2f x 10^%.0f MegaTons."
                % (en, en_power, en_mton, enmton_power)
            )
            discribe += "The energy lost in the atmosphere is %.2f x 10^%.0f Joules = %.2f x 10^%.0f MegaTons." % (
                en, en_power, en_mton, enmton_power) + "/n"
            if megaton_power != 0:
                print(
                    "The impact energy is %.2f x 10^%.0f Joules = %.2f x 10^%.0fMegaTons."
                    % (
                        energy_surface,
                        ens_power,
                        energy_megatons,
                        megaton_power,
                    )
                )
                discribe += "The impact energy is %.2f x 10^%.0f Joules = %.2f x 10^%.0fMegaTons." % (
                    energy_surface,
                    ens_power,
                    energy_megatons,
                    megaton_power,
                ) + "/n"

            else:
                print(
                    "The impact energy is %.2f x 10^%.0f Joules = %.2f MegaTons."
                    % (energy_surface, ens_power, energy_megatons)
                )
                discribe += "The impact energy is %.2f x 10^%.0f Joules = %.2f MegaTons." % (
                    energy_surface, ens_power, energy_megatons) + "/n"

            print(
                "The larger of these two energies is used to estimate the airblast damage."
            )
            discribe += "The larger of these two energies is used to estimate the airblast damage." + "/n"

            print(
                "The broken projectile fragments strike the ground in an ellipse of dimension %f km by %f km"
                % (
                    dispersion / (1000 * sin(theta * PI / 180)),
                    dispersion / 1000,
                )
            )
            discribe += "The broken projectile fragments strike the ground in an ellipse of dimension %f km by %f km" % (
                dispersion / (1000 * sin(theta * PI / 180)),
                dispersion / 1000,
            ) + "/n"

    print("")
    return discribe


def print_ejecta(
    energy_megatons,
    megaton_power,
    distance,
    Rf,
    Dtr,
    cdiameter,
    ejecta_arrival,
    ejecta_thickness,
    d_frag,
):
    # ejecta results
    print("Ejecta:")

    discribe = ""
    # Ejecta from small impacts is blocked by the atmosphere
    if (energy_megatons * 10 ** megaton_power) < 200 and (distance > Rf):
        print("Most ejecta is blocked by Earth's atmosphere")
        discribe += "Most ejecta is blocked by Earth's atmosphere" + "/n"
        return discribe

    # Ejecta comes from transient crater
    if distance * 1000 <= Dtr / 2:
        print(
            "Your position was inside the transient crater and ejected upon impact"
        )
        discribe += "Your position was inside the transient crater and ejected upon impact" + "/n"
        return discribe

    # Inside final crater
    if distance * 1000 > Dtr / 2 and distance * 1000 < cdiameter / 2:
        print(
            "Your position is in the region which collapses into the final crater."
        )
        discribe += "Your position is in the region which collapses into the final crater." + "/n"
        return discribe

    # Arrival time greater than 1 hour or almost no ejecta
    if ejecta_arrival >= 3600:
        print(
            "Little rocky ejecta reaches this site fallout is dominated by condensed vapor from the projectile."
        )
        discribe += "Little rocky ejecta reaches this site fallout is dominated by condensed vapor from the projectile." + "/n"
        return discribe

    elif ejecta_thickness * 10 ** 6 < 1:
        print("Almost no solid ejecta reaches this site.")
        discribe += "Almost no solid ejecta reaches this site." + "/n"

        return discribe

    # Type of ejecta deposit
    if distance * 1000 <= 3 * cdiameter / 2:
        print("Your position is beneath the continuous ejecta deposit.")
        discribe += "Your position is beneath the continuous ejecta deposit." + "/n"
    else:
        print(
            "At your position there is a fine dusting of ejecta with occasional larger fragments"
        )
        discribe += "At your position there is a fine dusting of ejecta with occasional larger fragments" + "/n"

    # Ejecta thickness
    print(
        "Average Ejecta Thickness:  %f %s ( = %f %s ) \n"
        % (ejecta_thickness, "meters", ejecta_thickness * 3.28, "feet")
    )
    discribe += "Average Ejecta Thickness:  %f %s ( = %f %s ) \n" % (
        ejecta_thickness, "meters", ejecta_thickness * 3.28, "feet") + "/n"

    # Fragment size
    print(
        "Mean Fragment Diameter:  %f %s ( = %f %s ) \n"
        % (d_frag, "meters", d_frag * 3.28, "feet")
    )
    discribe += "Mean Fragment Diameter:  %f %s ( = %f %s ) \n" % (
        d_frag, "meters", d_frag * 3.28, "feet") + "/n"
    print("")

    return discribe


def print_thermal(
    velocity,
    no_radiation,
    max_rad_time,
    distance,
    Rf,
    h,
    thermal_power,
    thermal_exposure,
    irradiation_time,
):
    print("Thermal Radiation:")

    print("What does this mean?")

    discribe = ""
    # No fireball at low velocity
    if velocity < 15:
        print(
            "At this impact velocity ( < 15 km/s), little vaporization occurs no fireball is created, therefore, there is no thermal radiation damage."
        )
        discribe += "At this impact velocity ( < 15 km/s), little vaporization occurs no fireball is created, therefore, there is no thermal radiation damage." + "/n"
        return discribe

    # Is fireball above the horizon?
    if no_radiation == 1:
        print(
            "The fireball is below the horizon. There is no direct thermal radiation."
        )
        discribe += "The fireball is below the horizon. There is no direct thermal radiation." + "/n"
        return discribe

    # Time of maximum radiation
    print(
        "Time for maximum radiation:  %f %s  after impact"
        % (max_rad_time, "seconds")
    )
    discribe += "Time for maximum radiation:  %f %s  after impact" % (
        max_rad_time,  "seconds") + "/n"

    # Size of the fireball
    if distance < Rf:
        print("Your position is inside the fireball.")
        discribe += "Your position is inside the fireball." + "/n"
    else:
        print(
            "Visible fireball radius:  %f %s ( = %f %s ) "
            % ((Rf - h) * 1000, "meters", (Rf - h) * 1000 * 3.28, "feet")
        )
        discribe += "Visible fireball radius:  %f %s ( = %f %s ) " % (
            (Rf - h) * 1000, "meters", (Rf - h) * 1000 * 3.28, "feet") + "/n"

    # Brightness of the fireball relative to the sun
    B = (Rf - h) / (4.4 * 10 ** -3 * distance)
    if B >= 0.1:
        print("The fireball appears %f times larger than the sun" % (B))
        discribe += "The fireball appears %f times larger than the sun" % (
            B) + "/n"

    # Thermal exposure
    if thermal_power == 0:
        print("Thermal Exposure:  %.2f Joules/m<sup2" % (thermal_exposure))
        discribe += "Thermal Exposure:  %.2f Joules/m<sup2" % (
            thermal_exposure) + "/n"
    else:
        print(
            "Thermal Exposure:  %.2f x 10^%.0f Joules/m^2"
            % (thermal_exposure, thermal_power)
        )
        discribe += "Thermal Exposure:  %.2f x 10^%.0f Joules/m^2" % (
            thermal_exposure, thermal_power) + "/n"

    # Duration of irradiation
    print("Duration of Irradiation:  %f %s" % (irradiation_time, "seconds"))
    discribe += "Duration of Irradiation:  %f %s" % (
        irradiation_time, "seconds") + "/n"

    # Radiant flux relative to solar flux
    flux = (thermal_exposure * 10 ** thermal_power) / (
        irradiation_time * 1000
    )
    print("Radiant flux (relative to the sun):  %f", flux)
    discribe += "Radiant flux (relative to the sun):  %f" % (flux) + "/n"
    if flux >= 15 and flux <= 25:
        print(" (Flux from a burner on full at a distance of 10 cm)")
        discribe += " (Flux from a burner on full at a distance of 10 cm)" + "/n"
    print("")

    return discribe


def print_seismic(magnitude, seismic_arrival):
    # seismic results
    print("Seismic Effects:")
    print("What does this mean?")

    discribe = ""

    # Don' print results if magnitude very small
    if magnitude < 0:
        print(
            "The Richter Scale Magnitude for this impact is less than zero no seismic shaking will be felt."
        )
        discribe += "The Richter Scale Magnitude for this impact is less than zero no seismic shaking will be felt." + "/n"
        return discribe

    # Arrival time
    if seismic_arrival < 0.1:
        print("The major seismic shaking will arrive almost instantly.")
        discribe += "The major seismic shaking will arrive almost instantly." + "/n"
    else:
        print(
            "The major seismic shaking will arrive approximately %f %s after impact."
            % (seismic_arrival, "seconds")
        )
        discribe += "The major seismic shaking will arrive approximately %f %s after impact." % (
            seismic_arrival, "seconds") + "/n"

    # Richter Scale Magnitude
    print("Richter Scale Magnitude:  %.1f" % (magnitude))
    discribe += "Richter Scale Magnitude:  %.1f" % (magnitude) + "/n"
    if magnitude >= 9.5:
        print(" (This is greater than any earthquake in recorded history)")
        discribe += " (This is greater than any earthquake in recorded history)" + "/n"

    # Earthquake damage
    # print("Mercalli Scale Intensity at a distance of distance km: \n<br>\n"
    # print des
    print("")
    return discribe


def print_airblast(
    opressure,
    vmax,
    shock_arrival,
    distance,
    altitudeBurst,
    dec_level,
    shock_damage,
):
    bars = opressure / 10 ** 5
    mph = vmax * 2.23694

    print("Air Blast:")

    print("What does this mean?")

    discribe = ""
    # Exit if airblast has no effect
    if opressure < 1:
        print(
            "The air blast at this location would not be noticed. (The overpressure is less than 1 Pa)"
        )
        discribe += "The air blast at this location would not be noticed. (The overpressure is less than 1 Pa)" + "/n"
        return

    # Blast wave arrival time
    print(
        "The air blast will arrive approximately %f %s after impact."
        % (shock_arrival, "seconds")
    )
    discribe += "The air blast will arrive approximately %f %s after impact." % (
        shock_arrival, "seconds")

    # Overpressure
    if distance * 1000.0 < 3 * altitudeBurst:
        print(
            "Peak Overpressure:  %f - %f Pa = %f - %f bars = %f - %f psi"
            % (
                opressure,
                2 * opressure,
                bars,
                2 * bars,
                bars * 14.2,
                2 * bars * 14.2,
            )
        )
        discribe += "Peak Overpressure:  %f - %f Pa = %f - %f bars = %f - %f psi" % (
            opressure,
            2 * opressure,
            bars,
            2 * bars,
            bars * 14.2,
            2 * bars * 14.2,
        ) + "/n"
    else:
        print(
            "Peak Overpressure:  %f Pa = %f bars = %f psi"
            % (opressure, bars, bars * 14.2)
        )
        discribe += "Peak Overpressure:  %f Pa = %f bars = %f psi" % (
            opressure, bars, bars * 14.2) + "/n"

    # Wind velocity
    print("Max wind velocity:  %f m/s = %f mph" % (vmax, mph))
    discribe += "Max wind velocity:  %f m/s = %f mph" % (vmax, mph) + "/n"

    # Sound intensity
    if dec_level > 0:
        print("Sound Intensity:  %.0f dB" % (dec_level), end="")
        discribe += "Sound Intensity:  %.0f dB" % (dec_level)
        if dec_level <= 20:
            print(" (Barely Audible)")
            discribe += " (Barely Audible)"
        elif dec_level <= 50:
            print(" (Easily Heard)")
            discribe += " (Easily Heard)"
        elif dec_level <= 90:
            print(" (Loud as heavy traffic)")
            discribe += " (Loud as heavy traffic)"
        elif dec_level <= 120:
            print(" (May cause ear pain)")
            discribe += " (May cause ear pain)"
        else:
            print(" (Dangerously Loud)")
            discribe += " (Dangerously Loud)"

    else:
        print("The blast wave will not be heard.")
        discribe += "The blast wave will not be heard." + "/n"

    # Airblast damage
    if shock_damage != "":
        print("Damage Description: ", end="")
        discribe += "Damage Description: "

    print(shock_damage)
    discribe += shock_damage + "/n"
    print("")
    return discribe


def print_tsunami(
    distance,
    wdiameter,
    TsunamiArrivalTime,
    WaveAmplitudeLowerLimit,
    WaveAmplitudeUpperLimit,
):
    FormattedTime = 0.0
    TimeUnit = "non"

    # Print the tsunami results
    print("Tsunami Wave:")

    print("What does this mean?")

    discribe = ""
    # If inside the water crater say this and finish.
    if distance * 1000 < wdiameter:
        print(
            "Your location is within the crater formed in the water layer. This is where the impact tsunami wave is generated. \n"
        )
        discribe += "Your location is within the crater formed in the water layer. This is where the impact tsunami wave is generated. \n"
        return discribe

    # Report the approximate arrival time of the tsunami
    print(
        "The impact-generated tsunami wave arrives approximately %.1f %s after impact. "
        % (TsunamiArrivalTime, "seconds")
    )
    discribe += "The impact-generated tsunami wave arrives approximately %.1f %s after impact. " % (
        TsunamiArrivalTime, "seconds") + "/n"

    # Report the two wave amplitude limits if more than 10 cm
    if WaveAmplitudeLowerLimit > 0.1:
        print(
            "Tsunami wave amplitude is between:  %.1f %s ( = %.1f %s) and %.1f %s ( = %.1f %s). "
            % (
                WaveAmplitudeLowerLimit,
                "meters",
                WaveAmplitudeLowerLimit * 3.28,
                "feets",
                WaveAmplitudeUpperLimit,
                "meters",
                WaveAmplitudeUpperLimit * 3.28,
                "feets",
            )
        )
        discribe += "Tsunami wave amplitude is between:  %.1f %s ( = %.1f %s) and %.1f %s ( = %.1f %s). " % (
            WaveAmplitudeLowerLimit,
            "meters",
            WaveAmplitudeLowerLimit * 3.28,
            "feets",
            WaveAmplitudeUpperLimit,
            "meters",
            WaveAmplitudeUpperLimit * 3.28,
            "feets",
        ) + "/n"
    elif WaveAmplitudeUpperLimit < 0.1:
        print(
            "Tsunami wave amplitude is less than 10 cm at your location. "
        )
        discribe += "Tsunami wave amplitude is less than 10 cm at your location. " + "/n"
    else:
        print(
            "Tsunami wave amplitude is less than %.1f %s ( = %.1f %s). "
            % (
                WaveAmplitudeUpperLimit,
                "meters",
                WaveAmplitudeUpperLimit * 3.28,
                "feets",
            )
        )
        discribe += "Tsunami wave amplitude is less than %.1f %s ( = %.1f %s). " % (
            WaveAmplitudeUpperLimit,
            "meters",
            WaveAmplitudeUpperLimit * 3.28,
            "feets",
        ) + "/n"

    print("")
    return discribe


def print_crater(
    vMelt,
    Dtr,
    depth,
    wdiameter,
    pdiameter,
    dispersion,
    collinsIFactor,
    depthtr,
    mratio,
    mcratio,
    cdiameter,
    depthfr,
    brecciaThickness,
    velocity,
):
    melt_thickness = vMelt / (PI * (Dtr / 2000) ** 2)

    # crater results
    print("Crater Dimensions:")

    discribe = ""
    # Print details of crater in water layer
    if depth != 0:
        print(
            "The crater opened in the water has a diameter of %f %s ( = %f %s )."
            % (wdiameter, "meters", wdiameter * 3.28, "feets")
        )
        discribe += "The crater opened in the water has a diameter of %f %s ( = %f %s ). " % (
            wdiameter, "meters", wdiameter * 3.28, "feets") + "/n"
        if Dtr > 0:
            print("For the crater formed in the seafloor:")
            discribe += "For the crater formed in the seafloor:" + "/n"

    # Report consequences of atmospheric disruption
    if pdiameter < 1000:
        if dispersion >= Dtr:
            print(
                "The result of the impact is a crater field, not a single crater.  The following dimensions are for the crater produced by the largest fragment."
            )
            discribe += "The result of the impact is a crater field, not a single crater.  The following dimensions are for the crater produced by the largest fragment." + "/n"

        elif collinsIFactor < 1:
            print(
                "Crater shape is normal in spite of atmospheric crushing fragments are not significantly dispersed."
            )
            discribe += "Crater shape is normal in spite of atmospheric crushing fragments are not significantly dispersed." + "/n"

    # Report transient crater dimensions
    print("Transient Crater Diameter:")
    discribe += "Transient Crater Diameter:" + "/n"

    print("%f %s ( = %f %s )" % (Dtr, "meters", Dtr * 3.28, "feets"))
    discribe += "%f %s ( = %f %s )" % (Dtr, "meters",
                                       Dtr * 3.28, "feets") + "/n"
    print(
        "Transient Crater Depth:  %f %s ( = %f %s )"
        % (depthtr, "meters", depthtr * 3.28, "feets")
    )
    discribe += "Transient Crater Depth:  %f %s ( = %f %s )" % (
        depthtr, "meters", depthtr * 3.28, "feets") + "/n"

    # If melt volume is equivalent to the volume of the Earth finish
    if mratio == 1:
        return discribe

    # Report final crater dimensions
    print("Final Crater Diameter:")
    discribe += "Final Crater Diameter:" + "/n"

    print(
        "%f %s ( = %f %s )"
        % (cdiameter, "meters", cdiameter * 3.28, "feets")
    )
    discribe += "%f %s ( = %f %s )" % (cdiameter, "meters",
                                       cdiameter * 3.28, "feets") + "/n"
    print(
        "Final Crater Depth:  %f %s ( = %f %s )"
        % (depthfr, "meters", depthfr * 3.28, "feets")
    )
    discribe += "Final Crater Depth:  %f %s ( = %f %s )" % (
        depthfr, "meters", depthfr * 3.28, "feets") + "/n"

    # Report the type of crater formed
    if mcratio >= 1:
        print(
            "The final crater is replaced by a large, circular melt province."
        )
        discribe += "The final crater is replaced by a large, circular melt province." + "/n"
    elif cdiameter >= 3200:
        print("complex crater .")
        discribe += "complex crater ." + "/n"
    else:
        print("simple crater ")
        discribe += "simple crater " + "/n"
        print(
            "The floor of the crater is underlain by a lens of broken rock debris (breccia) with a maximum thickness of %f %s ( = %f %s )."
            % (brecciaThickness, "meters", brecciaThickness * 3.28, "feets")
        )
        discribe += "The floor of the crater is underlain by a lens of broken rock debris (breccia) with a maximum thickness of %f %s ( = %f %s )." % (
            brecciaThickness, "meters", brecciaThickness * 3.28, "feets") + "/n"

    # Report the melt volume and thickness
    if velocity >= 12 and mratio < 0.1:

        # Melt volume
        if vMelt < 0.001:
            print(
                "The volume of the target melted or vaporized is %f m^3 = %f feet^3"
                % (vMelt * 10 ** 9, vMelt * 10 ** 9 * 3.28 ** 3)
            )
            discribe += "The volume of the target melted or vaporized is %f m^3 = %f feet^3" % (
                vMelt * 10 ** 9, vMelt * 10 ** 9 * 3.28 ** 3) + "/n"
        else:
            print(
                "The volume of the target melted or vaporized is %f km^3 = %f miles^3"
                % (vMelt, vMelt * 0.2399)
            )
            discribe += "The volume of the target melted or vaporized is %f km^3 = %f miles^3" % (
                vMelt, vMelt * 0.2399) + "/n"

            # Melt thickness for complex crater (not melt pool)
        if mcratio < 1:
            print("Roughly half the melt remains in the crater")
            discribe += "Roughly half the melt remains in the crater" + "/n"
            if Dtr >= 3200:
                print(
                    ", where its average thickness is %f %s ( = %f %s ). \n"
                    % (
                        melt_thickness * 1000,
                        "meters",
                        melt_thickness * 1000 * 3.28,
                        "feets",
                    )
                )
                discribe += ", where its average thickness is %f %s ( = %f %s ). \n" % (
                    melt_thickness * 1000,
                    "meters",
                    melt_thickness * 1000 * 3.28,
                    "feets",
                ) + "/n"
        else:
            print(
                "At this impact velocity ( < 12 km/s), little shock melting of the target occurs."
            )
            discribe += "At this impact velocity ( < 12 km/s), little shock melting of the target occurs." + "/n"

    # Melt pool
    if mcratio >= 1:
        print("Melt volume = %f times the crater volume\n" % (mcratio))
        discribe += "Melt volume = %f times the crater volume\n" % (
            mcratio) + "/n"

    print("At this size, the crater forms in its own melt pool.")
    discribe += "At this size, the crater forms in its own melt pool." + "/n"
    return discribe


if __name__ == "__main__":
    print_energy(4.8967338468637005e17, 116.9788305509723)
