import unittest

from sinus import sinus


class SinusTestCase(unittest.TestCase):
    def test_poprawny_wynik(self):
        self.assertEqual(sinus(0.), 0.)


if __name__ == '__main__':
    unittest.main()
