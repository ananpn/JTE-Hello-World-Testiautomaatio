import unittest
from laskin import plus

class TestLaskin(unittest.TestCase):
    def test_plus(self):
        self.assertEqual(plus(1, 1), 3)

if __name__ == '__main__':
    unittest.main()
