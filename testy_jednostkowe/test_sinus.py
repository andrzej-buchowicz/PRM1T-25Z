import unittest
import math

from sinus import sinus


class SinusTestCase(unittest.TestCase):
    def test_poprawny_wynik(self):
        self.assertAlmostEqual(sinus(0.), 0.)
        self.assertAlmostEqual(sinus(math.pi / 2), 1.0)
        self.assertAlmostEqual(sinus(math.pi / 4), math.sqrt(2.) / 2)

    def test_zly_typ_danych(self):
        self.assertRaises(AssertionError, sinus, 'abc')


if __name__ == '__main__':
    unittest.main()
