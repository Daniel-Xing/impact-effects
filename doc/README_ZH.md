# Impact Effect Simulator Library

[![Python](https://img.shields.io/pypi/pyversions/tensorflow.svg?style=plastic)](https://badge.fury.io/py/tensorflow)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 

> [English](../README.md) | 中文

小行星和彗星的撞击事件是行星科学研究的核心问题之一，研究和建模撞击事件有助于我们了解其过程，评估撞击事件的可能造成的影响。这是一种广泛的需求对于很多研究者来说。本项目提供了一个python library来帮助研究者建模撞击事件并评估相应后果，通过提供必要的函数和接口。


## 🍞 Features

- 支持[Earth Impact Effects Program](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1945-5100.2005.tb00157.x)中的重点函数计算，能够模拟撞击事件的发生和可能的后果。
- 良好的接口设计，能够让研究者轻松地使用这个库并单独计算相关的物理参数。
- 易于安装，支持PiPy3和Python3.6以上的版本，支持PIP安装。


##  🖥 Install

ImpactEffect has been released in PyPI, which means it can be installed by PIP directly.

```python
pip install impactEffect
```

##  🚩 Usage

ImapctEffect 是非常易于使用的，你可以使用以下方法来建模撞击事件：

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

如果你需要进行二次开发，最简单的方式是提交一个issue或者pull request，我们会尽可能的帮助你。下面是一些可能有用的帮助:

```bash
# 克隆项目
git clone git@github.com:acse-dx121/impact-effects.git

# 查看项目结构
cd impact-effects
```

所有的源代码被放在了一个名为 `impactEffects` 的目录下。
- instances： 包含了所有的实例类，包括撞击者和目标。
- functions： 包含了所有的函数，包括计算撞击力的函数和撞击事件的计算函数。这里定义了所有的接口。具体的计算逻辑在core下。
- core：核心计算逻辑，目前只支持[Earth Impact Effects Program](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1945-5100.2005.tb00157.x)
- utils: 包含一些工具函数

**对现有计算逻辑进行更改**
核心逻辑被放在impactEffect/core下，找到对应函数进行更改。在完成更改之后，贡献者应当测试更改是否是有效的。基本的测试为保证test目录下的所有测试通过。

```python
# under the source path
pytest
```

**新增计算逻辑**
如果需要新增计算逻辑，建议按照以下几步完成。
1. 在 core包内新增相关文件，并完成计算逻辑。修改__init__.py文件, 添加心动模块。
2. 在 function包内新增相关文件，并完成接口函数。
3. 在 test目录下，新增测试文件，并完成测试。


