#!/usr/bin/env python
# Copyright (c) 2022, Matthieu Perez
#
# Distributed under the 3-clause BSD license, see accompanying file LICENSE
# or https://github.com/Scikit-HEP/skbuild_only for details.

# Try not to modify this file.
# Do not attempt to call this file directly with the python command.
# If you see a tutorial doing that, it's probably outdated.
# Most of the time, you should be able to do what you want in the more modern pyproject.toml.
# setup.py and setuptools will likely be deprecated soon.
from __future__ import annotations

from setuptools import find_packages
from skbuild import setup

# This file seems still necessary for now (scikit-build will be more and more independent of setuptools)
# for the binary extension (C++ code) installation with pip install
# note : some information have to be duplicated here from the pyproject.toml, sorry
setup(
    name="skbuild_only",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    cmake_install_dir="src/skbuild_only",
    package_data={"skbuild_only": ["py.typed"]},
)
