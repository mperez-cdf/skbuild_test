#!/usr/bin/env python
# Copyright (c) 2022, Matthieu Perez
#
# Distributed under the 3-clause BSD license, see accompanying file LICENSE
# or https://github.com/Scikit-HEP/skbuild_only for details.

from __future__ import annotations

from setuptools import find_packages
from skbuild import setup

setup(
    name="skbuild_only",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    cmake_install_dir="src/skbuild_only",
    package_data={"skbuild_only": ["py.typed"]},
)
