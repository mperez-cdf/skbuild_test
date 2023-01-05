"""
Copyright (c) 2022 Matthieu Perez. All rights reserved.

skbuild_only: Scikit build project descriptionnnnn
"""

from __future__ import annotations

# read version from installed package
from importlib.metadata import version  # type: ignore[import]

__version__ = version(__name__)

__all__ = ("__version__",)
