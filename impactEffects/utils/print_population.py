
from cmath import inf
from glob import glob


def Global_change(vratio, mratio, lratio, trot_change, pratio):
    """
    Arguments
    ---------
    vratio:
    mratio:
    lratio:
    trot_change:
    pratio:
    """
    global_change = "Global change:\n"

    # vratio
    global_change += " %f %% probability: " % (
        len([v for v in vratio if v >= 0.5])*100/len(vratio))
    global_change += "The Earth is completely disrupted by the impact and its debris forms a new asteroid belt orbiting the sun between Venus and Mars.\n"

    global_change += " %f probability: " % (
        len([v for v in vratio if v < 0.5 and v >= 0.1])*100/len(vratio))
    global_change += "The Earth is strongly disturbed by the impact, but loses little mass.\n"

    global_change += " %f probability: " % (
        len([v for v in vratio if v < 0.1])*100/len(vratio))
    global_change += "The Earth is not strongly disturbed by the impact and loses negligible mass.\n"

    # mratio
    subMratio = [v for v in mratio if v >= 0.01]
    global_change += " %f probability: " % (
        len(subMratio)*100/len(mratio))

    try:
        lowbound, upbound = min(subMratio) * 100, max(subMratio) * 100
    except:
        lowbound, upbound = [-inf, inf]

    global_change += "[%.2f, %2f] percent of the Earth is melted \n" % (
        lowbound, upbound)

    # lratio
    global_change += " %f probability: " % (
        len([v for v in lratio if v >= 0.001])*100/len(lratio))
    global_change += "Depending on the direction and location the collision, "

    global_change += " %f probability: " % (
        len([v for v in lratio if v >= 0.001 and v < 0.01])*100/len(lratio))
    global_change += "the impact may make a very small change in the tilt of Earth's axis (< half a degree)."

    global_change += " %f probability: " % (
        len([v for v in lratio if v >= 0.01 and v < 0.1])*100/len(lratio))
    global_change += "the impact may make a noticeable change in the tilt of Earth's axis (< 5 degrees)."

    global_change += " %f probability: " % (
        len([v for v in lratio if v >= 0.1 and v < 1.0])*100/len(lratio))
    global_change += "the impact may make a significant change in the tilt of Earth's axis."

    global_change += " %f probability: " % (
        len([v for v in lratio if v >= 1.0])*100/len(lratio))
    global_change += "the impact may totally change the Earth's rotation period and the tilt of its axis."

    global_change += "\n"

    global_change += " %f probability: " % (
        len([v for v in lratio if v < 0.001])*100/len(lratio))
    global_change += "the impact may totally change the Earth's rotation period and the tilt of its axis. \n"

    # trot_change
    subTrot = [v for v in trot_change if v >= 1e-3]
    global_change += " %f probability: " % (
        len(subTrot)*100/len(trot_change))

    try:
        lowbound, upbound = min(subTrot), max(subTrot)
    except:
        lowbound, upbound = [-inf, inf]
    global_change += "Depending on the direction and location of impact, the collision may cause a change in the length of the day of up to [%f, %f] unit." % (
        lowbound, upbound)

    # pratio
    global_change += " %f probability: " % (
        len([v for v in pratio if v >= 0.001 and v < 0.01])*100/len(pratio))
    global_change += "The impact shifts the Earth's orbit noticeably. \n"

    ## pratio >= 0.01 and pratio < 0.1
    global_change += " %f probability: " % (
        len([v for v in pratio if v >= 0.01 and v < 0.1])*100/len(pratio))
    global_change += "The imapct shifts the Earth's orbit substantially. \n"

    ## pratio >= 0.1
    global_change += " %f probability: " % (
        len([v for v in pratio if v >= 0.1])*100/len(pratio))
    global_change += "The impact shifts the Earth's orbit totally. \n"

    ## pratio < 1e-3
    global_change += " %f probability: " % (
        len([v for v in pratio if v < 1e-3])*100/len(pratio))
    global_change += "The impact does not shift the Earth's orbit noticeably. \n"

    return global_change
