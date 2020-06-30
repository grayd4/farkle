import pygame
from constants import Points
from constants import Number
from die import Die

class AvailablePoints:

    def __init__(self, diceSet):
        self.diceSet = diceSet  # The dice we analyze for points
        self.points = 0         # The point total in the given dice
        self.pointsSet = []     # The set of dice contributing to the point total

    def getResult(self):
        return self.points, self.pointsSet
    
    def calcSingles(self):
        for d in self.diceSet:
            if d.val == Number.ONE:
                points += Points.ONE
                self.pointsSet.append(d.index)
            elif d.val == Number.FIVE:
                points += Number.FIVE
                self.pointsSet.append(d.index)

    def calcTriples(self):
        counter = [0, 0, 0, 0, 0, 0, 0] # Holds total of each die
        for d in self.diceSet:
            counter[d.index] += 1
        for i, c in enumerate(counter):
            if c == 6:
                self.checkIndexForTriples(i, 2)
            elif c >= 3:
                self.checkIndexForTriples(i, 1)

    def calcThreePairs(self):
        
            
    def checkIndexForTriples(self, i, multiplier):
        if i + 1 == Number.ONE:
            self.points += Points.ONE_3 * multiplier
            self.addTripleToPointsSet(Number.ONE)
        if i + 1 == Number.TWO:
            self.points += Points.TWO_3 * multiplier
            self.addTripleToPointsSet(Number.TWO)
        if i + 1 == Number.THREE:
            self.points += Points.THREE_3 * multiplier
            self.addTripleToPointsSet(Number.THREE)
        if i + 1 == Number.FOUR:
            self.points += Points.FOUR_3 * multiplier
            self.addTripleToPointsSet(Number.FOUR)
        if i + 1 == Number.FIVE:
            self.points += Points.FIVE_3 * multiplier
            self.addTripleToPointsSet(Number.FIVE)
        if i + 1 == Number.SIX:
            self.points += Points.SIX_3 * multiplier
            self.addTripleToPointsSet(Number.SIX)

    def addTripleToPointsSet(self, num):
        for d in self.diceSet:
            if d.val == num:
                self.pointsSet.append(d.index)


    