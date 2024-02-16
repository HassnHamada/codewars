import unittest
from ..src.the_observed_pin import get_pins


class TestGetPins(unittest.TestCase):

    def test_get_pins_with_single_digit(self):
        observed = '1'
        expected = ['1', '2', '4']
        self.assertEqual(sorted(get_pins(observed)), sorted(expected))

    def test_get_pins_with_two_digits(self):
        observed = '11'
        expected = ['11', '21', '41', '12', '22', '42', '14', '24', '44']
        self.assertEqual(sorted(get_pins(observed)), sorted(expected))

    def test_get_pins_with_single_digit_2(self):
        observed = '8'
        expected = ['5', '7', '8', '9', '0']
        self.assertEqual(sorted(get_pins(observed)), sorted(expected))

    def test_get_pins_with_two_digits_2(self):
        observed = '11'
        expected = ["11", "22", "44", "12", "21", "14", "41", "24", "42"]
        self.assertEqual(sorted(get_pins(observed)), sorted(expected))

    def test_get_pins_with_three_digits(self):
        observed = '369'
        expected = [
            "339", "366", "399", "658", "636", "258", "268", "669", "668", "266", "369", "398",
            "256", "296", "259", "368", "638", "396", "238", "356", "659", "639", "666", "359",
            "336", "299", "338", "696", "269", "358", "656", "698", "699", "298", "236", "239"
        ]
        self.assertEqual(sorted(get_pins(observed)), sorted(expected))


if __name__ == '__main__':
    unittest.main()
