#!/usr/bin/env python3

import sys

from .nbttag import NBTTagType, NBTTag
from .nbttagio import writesnbttostream

def print_help() -> None :
    print(f"Usage: {sys.argv[0]} read [<filename>]")

ARGC: int = len(sys.argv)

if ARGC == 1 :
    print_help()