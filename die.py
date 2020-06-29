import pygame
import random
from enum import IntEnum
from constants import Number

class Die:

    # Constructor
    def __init__(self):
        self.val = Number.ONE
        self.saved = False

    def roll(self):
        if not self.saved:
            self.val = random.randrange(Number.ONE, Number.SIX)

    def setSaved(self, saved):
        self.saved = saved