# Impact Effect Simulator Library

[![Python](https://img.shields.io/pypi/pyversions/tensorflow.svg?style=plastic)](https://badge.fury.io/py/tensorflow)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 

> [English](../README.md) | 中文

小行星和彗星的撞击事件是行星科学研究的核心问题之一，研究和建模撞击事件有助于我们了解其过程，评估撞击事件的可能造成的影响。这是一种广泛的需求对于很多研究者来说。本项目提供了一个python library来帮助研究者建模撞击事件并评估相应后果，通过提供必要的函数和接口。


## 🍞 Features

- features


##  🖥 Install

ImpactEffect has been released in PyPI, which means it can be installed by PIP directly.

```python
pip install impactEffect
```

##  🚩 Usage

ImapctEffect 是非常易于使用的，你可以使用以下方法来建模撞击事件：

```python
# calculate the kinetic energy of impactor
impactor = impactEffects.instances.ImpactorClass.Impactor(
        diameter=111, density=111, velocity=111, theta=45
)
targets = TargetClass.Target(depth=0, distance=75, density=2500)

res = kinetic_energy(impactor)

```

我们也提供了一个脚本来模拟撞击的全过程。

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

如果你需要进行二次开发，


