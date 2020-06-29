# A set of constants used by the farkle game files\

from enum import IntEnum

class Points(IntEnum):
    ONE = 100
    FIVE = 50
    ONE_3 = 1000
    TWO_3 = 200
    THREE_3 = 300
    FOUR_3 = 400
    FIVE_3 = 500
    SIX_3 = 600
    STRAIGHT = 3000
    THREE_PAIRS = 1500

class Number(IntEnum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6