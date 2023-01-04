"""
Copyright (c) 2022 Matthieu Perez. All rights reserved.

skbuild_only: Scikit build project descriptionnnnn
"""

# read version from installed package
from importlib.metadata import version
__version__ = version(__name__)

__all__ = ("__version__",)
