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

##  🍕 develop

如果你需要进行二次开发，


