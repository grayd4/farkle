import pygame
from die import Die

class Player:

    def __init__(self, name):
        self.name = name
        self.diceSet = [Die(0), Die(1), Die(2), Die(3), Die(4), Die(5)]
        self.points = 0
        self.availablePoints = []

    def rollSet(self):
        for d in self.diceSet:
            d.roll()
    
    def saveDie(self, index):
        if index < len(self.diceSet) and index >= 0:
            self.diceSet[index].setSaved(True)
    
    def reset(self):
        for d in self.diceSet:
            d.setSaved(False)

    def addPoints(self, points):
        self.points += points

    # Calculate the max number of available points in the unsaved dice
    # Return that sum
    def calcPointsAvailable(self):

        return 0

    # Calculate the max number of available points including the saved dice
    # Return that sum
    def calcPointsTotal(self):

        return 0