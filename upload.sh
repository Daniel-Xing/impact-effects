#!/bin/bash

# username: CarryMeRookie
rm -rf dist/*
python3 -m build
python3 -m twine upload  dist/* --verbose