import unittest


def power_of_two(n):
    return n**2


class TestPowerFunction(unittest.TestCase):


    def test_power(self):
        print("\ntest_power")
        self.assertEqual(power_of_two(2), 4)

    def test_negative(self):

        print("\ntest_negative")
        self.assertEqual(power_of_two(-3), 9)


    def test_float(self):

        print("\ntest_float")
        self.assertAlmostEqual(power_of_two(1.3), 1.69, places=2)


if __name__ == '__main__':
    unittest.main()
