from types import ModuleType
from typing import Tuple
import unittest
from . import test_nbtpath, test_nbttag, test_nbttagio

MODS: Tuple[ModuleType, ...] = (
    test_nbtpath, test_nbttag, test_nbttagio
)
[unittest.main(module=i, exit=False) for i in MODS]