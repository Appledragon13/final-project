"""
Important imports
"""
import sys
import os

from game_rules import NpcAndPlayerRules
from game_rules import itemRules
from game_rules import importantNpcs


"""
Important dictionaries that need to load before other things
"""

items = {}

def claer_termianl():
    if os.name == "nt":
        _ = os.system('cls')
    else:
        _ = os.system("clear")