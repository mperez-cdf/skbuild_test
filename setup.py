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
from skbuild import (  # note: we use the setup function from skbuild, not setuptools !
    setup,
)

# This file seems still necessary for now (scikit-build will be more and more independent of setuptools)
# for the binary extension (C++ code) installation with pip install
# note : some information have to be duplicated here from the pyproject.toml, sorry
setup(
    name="skbuild_only",  # package name
    packages=find_packages(
        where="src"
    ),  # Explicit list of all packages to include in the distribution.
    package_dir={"": "src"},  # A mapping of package to directory names
    cmake_install_dir="src/skbuild_only",  # relative directory where the CMake artifacts are installed. By default, it is set to an empty string.
    package_data={
        "skbuild_only": ["py.typed"]
    },  # A dictionary mapping package names to lists of glob patterns. For a complete description and examples, see the setuptools documentation section on Including Data Files.
)
