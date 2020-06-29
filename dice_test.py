import unittest
from die import Die
from constants import Number
from player import Player

testName = "Sips"
testIndex = 3

class TestDieMethods(unittest.TestCase):

    def test_init(self):
        d = Die()
        self.assertEqual(d.val, Number.ONE)
        self.assertEqual(d.saved, False)

    def test_roll(self):
        d = Die()
        d.roll()
        self.assertTrue(Number.ONE <= d.val <= Number.SIX)

    def test_setSaved(self):
        d = Die()
        self.assertEqual(d.saved, False)
        d.setSaved(True)
        self.assertEqual(d.saved, True)

class TestPlayerMethods(unittest.TestCase):

    def test_init(self):
        p = Player(testName)
        self.assertEqual(p.name, testName)
        for d in p.diceSet:
            self.assertEqual(d.val, Number.ONE)

    def test_rollSet(self):
        p = Player(testName)
        p.rollSet()
        for d in p.diceSet:
            self.assertTrue(Number.ONE <= d.val <= Number.SIX)
    
    def test_saveDie(self):
        p = Player(testName)
        p.rollSet()
        ogVal = p.diceSet[testIndex].val
        p.saveDie(testIndex)
        p.rollSet()
        self.assertEqual(ogVal, p.diceSet[testIndex].val)

    def test_reset(self):
        p = Player(testName)
        p.diceSet[testIndex].setSaved(True)
        p.reset()
        for d in p.diceSet:
            self.assertEqual(d.saved, False)

if __name__ == '__main__':
    unittest.main()