import unittest
from die import Die
from die import Number

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


if __name__ == '__main__':
    unittest.main()