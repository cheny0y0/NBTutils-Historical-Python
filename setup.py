import logging
import sys
from setuptools import find_packages, setup

if sys.version_info < (3, 7) or sys.version_info > (3, 7) :
    raise SystemError("Python 3.7.x required")

setup(
    name = "nbtutils",
    version = "0.0.1a1",
    author = "REGE",
    packages = find_packages()
)