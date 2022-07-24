# Impact Effect Simulator Library

[![Python](https://img.shields.io/pypi/pyversions/tensorflow.svg?style=plastic)](https://badge.fury.io/py/tensorflow)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 

> English | [中文](./doc/README_ZH.md)

The impact of asteroids and comets is one of the core issues of planet science research. Research and modeling impacts help us understand the process and evaluate the possible impact of the impact. This is a broad demand for many researchers. This project provides a Python Library to help researchers modeling and evaluating the corresponding consequences, providing necessary functions and interfaces.

## 🍞 Features
- Support the key functions in [Earth Impact Effects Program](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1945-5100.2005.tb00157.x), which can simulate the occurrence and possible consequences of the impact event.
- A good interface design allows researchers to easily use this library and calculate related physical parameters alone.
- Easy to install, support versions above PIPY3 and Python3.6, and support PIP installation.

##  🖥 Install

ImpactEffect has been released in PyPI, which means it can be installed by PIP directly.

```python
pip install impactEffect
```
##  🚩 Usage

ImapctEffect is very easy to use. You can use the following methods to model the impact event:

```python
from impactEffects.functions.function import *
from impactEffects.instances import ImpactorClass, TargetClass

# calculate the kinetic energy of impactor
impactor = impactEffects.instances.ImpactorClass.Impactor(
        diameter=111, density=111, velocity=111, theta=45
)
targets = TargetClass.Target(depth=0, distance=75, density=2500)

res = kinetic_energy(impactor)

```

We also provide a script to simulate the whole process of impact.

```bash
python impact_example.py

## example output
please input diameter of impactor: 111
please input density of impactor: 111
please input the velocity of impactor: 111
please input the theta of impactor: 45
please input the density of target: 111
please input the depth(meters): 0
please input the distance: 111
Energy before atmospheric entry: 4.90 x 10^17 Joules  = 1.17 x 10^2 MegaTons TNT

The average interval between impacts of this size somewhere on Earth during the last 4 billion years is 4.3 x 10^3years.
Major Global Changes:
The Earth is not strongly disturbed by the impact and loses negligible mass.
The impact does not make a noticeable change in the tilt of Earth's axis (< 5 hundreths of a degree).
The impact does not shift the Earth's orbit noticeably.

Atmospheric Entry:
The projectile begins to breakup at an altitude of 134913.980633 meters = 442517.856478 ft
The projectile bursts into a cloud of fragments at an altitude of 21963.771219 meters = 72041.169599 ft
The residual velocity of the projectile fragments after the burst is 12.175785 km/s = 7.561162 miles/s
The energy of the airburst is 4.84 x 10^17 Joules = 1.16 x 10^2 MegaTons.
No crater is formed, although large fragments may strike the surface.

1.3773689431439933 134913.9806334879
1.3773689431439933 134913.9806334879
Air Blast:
What does this mean?
The air blast will arrive approximately 342.885279 seconds after impact.
Peak Overpressure:  5872.472985 Pa = 0.058725 bars = 0.833891 psi
Max wind velocity:  13.506503 m/s = 30.213236 mph
Sound Intensity:  75 dB (Loud as heavy traffic)
Damage Description:  Glass windows may shatter.

```

##  🍕 develop

If you need to perform secondary development, the easiest way is to submit an issue or public request, and we will help you as much as possible.Here are some useful help:

```bash
# 克隆项目
git clone git@github.com:acse-dx121/impact-effects.git

# 查看项目结构
cd impact-effects
```

All source codes are placed in a directory called Impacteffects.
- instances： Including all instance classes, including impacts and goals.
- functions： Contains all functions, including functions that calculate impact power and calculation functions of impact events. All interfaces are defined here. The specific calculation logic is under the core.
- core：Core computing logic, currently only supports [Earth Impact Effects Program](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1945-5100.2005.tb00157.x)
- utils: Including some tool functions

**Change the existing calculation logic**
The core logic is placed under the IMPACTEFFECT/CORE, and the corresponding function is found to change it.After completing the change, the contributor should test whether the change is effective.The basic test is to ensure all the tests in the test directory.

```python
# under the source path
pytest
```

**New calculation logic**
如果需要新增计算逻辑，建议按照以下几步完成。
1. Add relevant files in the Core package and complete the calculation logic.Modify the __init__.py file to add a heart module.
2. Add relevant files in the function package and complete the interface function.
3. In the test directory, new test files are added and the test is completed.


