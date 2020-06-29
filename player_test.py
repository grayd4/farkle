import unittest
from player import Player
from die import Number

testName = "Sips"
testIndex = 3

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

if __name__ == '__main__':
    unittest.main()