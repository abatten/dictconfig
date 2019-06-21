"""
Dictconfig
==========
A wrapper for configparser to help create dictionaries from parameter files.

"""

from .dictconfig import read
from .__version__ import __version__
__name__ = "dictconfig"
__author__ = "Adam Batten (@abatten)"
__all__ = ["read"]
