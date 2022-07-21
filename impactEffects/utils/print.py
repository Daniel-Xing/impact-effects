from impactEffects.core.config import *


def print_energy(energy0, energy0_megatons):
    # Format energy in scientific notation and in different units
    energy_power = log(energy0)/log(10)
    energy_power = int(energy_power)
    energy0 /= 10**energy_power

    megaton_power = log(energy0_megatons)/log(10)
    megaton_power = int(megaton_power)
    energy0_megatons /= 10**megaton_power

    # Print the energy
    if energy_power == 0:
        print("Energy before atmospheric entry: %.2f Joules " %
              (energy0),  end='')
    else:
        print("Energy before atmospheric entry: %.2f x 10^%.0f Joules " %
              (energy0, energy_power),  end='')

    if megaton_power == 0:
        if energy0_megatons < 1:
            print(" = %.2f KiloTons TNT" % (energy0_megatons * 1000),  end='')
        else:
            print(" = %.2f MegaTons TNT" % (energy0_megatons),  end='')
    else:
        print(" = %.2f x 10^%.0f MegaTons TNT" %
              (energy0_megatons, megaton_power),  end='')

    print("")


def print_recurrencetime(rec_time):
    # Use scientific notation for recurrence times longer than 1000 years
    if rec_time > 1000:
        rec_time_p = log(rec_time)/log(10)
        rec_time_p = int(rec_time_p)
        rec_time /= 10**rec_time_p

        if rec_time * 10**rec_time_p < 4.5e9:
            print("The average interval between impacts of this size somewhere on Earth during the last 4 billion years is %.1f x 10^%.0fyears." % (
                rec_time, rec_time_p))
        else:
            print(
                "The average interval between impacts of this size is longer than the Earth's age.")
            print("Such impacts could only occur during the accumulation of the Earth, between 4.5 and 4 billion years ago.")

        return

    # Use normal notation for intervals less than 1000 years
    if rec_time * 12 < 1:
        print("The average interval between impacts of this size somewhere on Earth is less than 1 month.")
    else:
        print("The average interval between impacts of this size somewhere on Earth is %.1f years." % (rec_time))


if __name__ == "__main__":
    print_energy(4.8967338468637005e+17, 116.9788305509723)
