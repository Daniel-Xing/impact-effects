import os
import numpy as np

import impactEffects.instances.ImpactorClass
from impactEffects.functions import *
from impactEffects.functions.function import *
from impactEffects.instances import ImpactorClass, TargetClass
from ans_config import *
from operator import methodcaller

SCRIPT_PATH = "./cgi-bin"


def run_command(cmd):
    return os.popen(cmd).read()


def process_res(res: str):
    res = res.split('\n')
    resmap = {}

    print(res)
    for subStr in res:
        value_pair = [value.strip() for value in subStr.split("=")]
        if len(value_pair) != 2:
            continue
        try:
            resmap[value_pair[0]] = float(value_pair[1])
        except:
            #             print(value_pair)
            pass

    return resmap


def Test(pdiameter=111,
         pdensity=111,
         velocity=111,
         theta=45,
         tdensity=2500,
         depth=0,
         distance=75):

    keywords = ['mwater',
                'energy_seafloor',
                'Cd',
                'seismic_arrival',
                'depthtr',
                'vMelt',
                'mcratio',
                'vCrater',
                'energy_surface',
                'mass',
                'rec_time',
                'velocity',
                'angmom',
                'linmom',
                'pratio',
                'lratio',
                'cdiameter',
                #  'depthfr',
                #  'vmax',
                #  'vratio',
                #  'eff_mag',
                #  'vBU',
                #  'energy0',
                'energy_blast',
                #  'new_energy0',
                #  'delta',
                #  'mratio',
                #  'trot_change',
                'energy_atmosphere',
                #  'altitudeBU',
                'shock_arrival',
                #  'cdiameter',
                #  'i_Factor',gk
                #  'magnitude',
                'dispersion',
                #  'beta',
                #  'velocity_at_zero',
                #  'energy0_megatons',
                #  'ejecta_arrival',
                #  'anglefac',
                #  'altitudeBurst',
                #  'vseafloor',
                #  'dec_level',
                #  'Rf',
                #  'Dtr',
                'lDisper']

    print("Get Test Case: ")
    print("Impactor - Diameter: %d, Density: %d, Velocity: %d, Theta: %d " %
          (pdiameter, pdensity, velocity, theta))
    print("Target - Density: %d, Depth: %d, Distance: %d" %
          (tdensity, depth, distance))
    cmd = "cd cgi-bin && ./crater-cig.pl %d %d %d %d %d %d %d" % (
        pdiameter, pdensity, velocity, theta, tdensity, depth, distance)
    resMap = process_res(run_command(cmd))

    impactor = impactEffects.instances.ImpactorClass.Impactor(
        diameter=int(pdiameter), density=int(pdensity), velocity=int(velocity), theta=int(theta)
    )
    targets = TargetClass.Target(
        depth=int(depth), distance=int(distance), density=int(tdensity))

    keys = resMap.keys()

    for k in keys:
        if k in keywords and resMap[k] > 0:
            function_name = "cal_%s" % (k)
    #             print(function_name)
            res = globals()[function_name](impactor, targets)
            print(res, resMap[k])
            try:
                assert abs((res - resMap[k]) / res) < 0.05
                print("__________________%s__________________Passed" %
                      (function_name))
            except:
                print("__________________%s__________________Failed" %
                      (function_name))
                print("Value from scripts: ",
                      resMap[k], " Value from library", res)


def test_auto():
    pdiameter = 1000
    pdensity = 3000
    velocity = 20
    theta = 45
    tdensity = 2500
    depth = 0
    distance = 100

    cmd = "cd cgi-bin && ./crater-cig.pl %d %d %d %d %d %d %d" % (
        pdiameter, pdensity, velocity, theta, tdensity, depth, distance)
    m1 = process_res(run_command(cmd))
    k1 = list(m1.keys())
    Test(pdiameter=pdiameter, pdensity=pdensity, velocity=velocity,
         theta=theta, tdensity=tdensity, depth=depth, distance=distance)


def test_NormalImpactor():
    diamaters = np.random.uniform(100, 1000, 100)
    for dia in diamaters:
        Test(pdiameter=int(dia))
