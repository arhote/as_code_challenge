import unittest
from num_to_roman.roman_numeral import RomanNumeral


class RomanNumeralTestCase(unittest.TestCase):
    def test_number_to_numeral(self):
        """
        Test Base Cases
        """
        self.assertEqual(RomanNumeral.num_to_roman(1), RomanNumeral.ONE)
        self.assertEqual(RomanNumeral.num_to_roman(4), RomanNumeral.FOUR)
        self.assertEqual(RomanNumeral.num_to_roman(5), RomanNumeral.FIVE)
        self.assertEqual(RomanNumeral.num_to_roman(9), RomanNumeral.NINE)
        self.assertEqual(RomanNumeral.num_to_roman(10), RomanNumeral.TEN)
        self.assertEqual(RomanNumeral.num_to_roman(40), RomanNumeral.FORTY)
        self.assertEqual(RomanNumeral.num_to_roman(50), RomanNumeral.FIFTY)
        self.assertEqual(RomanNumeral.num_to_roman(90), RomanNumeral.NINETY)
        self.assertEqual(RomanNumeral.num_to_roman(100), RomanNumeral.ONE_HUNDRED)
        self.assertEqual(RomanNumeral.num_to_roman(400), RomanNumeral.FOUR_HUNDRED)
        self.assertEqual(RomanNumeral.num_to_roman(500), RomanNumeral.FIVE_HUNDRED)
        self.assertEqual(RomanNumeral.num_to_roman(900), RomanNumeral.NINE_HUNDRED)
        self.assertEqual(RomanNumeral.num_to_roman(1000), RomanNumeral.ONE_THOUSAND)



if __name__ == '__main__':
    unittest.main()
