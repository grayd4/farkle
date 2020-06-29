import pygame
from die import Die

class Player:

    def __init__(self, name):
        self.name = name
        self.diceSet = [Die(), Die(), Die(), Die(), Die(), Die()]

    def rollSet(self):
        for d in self.diceSet:
            d.roll()
    
    def saveDie(self, index):
        if index < len(self.diceSet) and index >= 0:
            self.diceSet[index].setSaved(True)
    
    def reset(self):
        for d in self.diceSet:
            d.setSaved(False)

    