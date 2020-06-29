import pygame
import random
from enum import IntEnum

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



class Number(IntEnum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6