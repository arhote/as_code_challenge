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
        """
        Test Groupings
        """
        self.assertEqual(RomanNumeral.num_to_roman(3), "III")
        self.assertEqual(RomanNumeral.num_to_roman(30), "XXX")
        self.assertEqual(RomanNumeral.num_to_roman(300), "CCC")
        self.assertEqual(RomanNumeral.num_to_roman(3000), "MMM")
        self.assertEqual(RomanNumeral.num_to_roman(15), "XV")
        self.assertEqual(RomanNumeral.num_to_roman(45), "XLV")
        self.assertEqual(RomanNumeral.num_to_roman(55), "LV")
        self.assertEqual(RomanNumeral.num_to_roman(105), "CV")
        self.assertEqual(RomanNumeral.num_to_roman(1100), "MC")
        self.assertEqual(RomanNumeral.num_to_roman(1110), "MCX")
        self.assertEqual(RomanNumeral.num_to_roman(1111), "MCXI")
        """
        Test Weird Numbers
        """
        self.assertEqual(RomanNumeral.num_to_roman(44), "XLIV")
        self.assertEqual(RomanNumeral.num_to_roman(49), "XLIX")
        self.assertEqual(RomanNumeral.num_to_roman(94), "XCIV")
        self.assertEqual(RomanNumeral.num_to_roman(99), "XCIX")
        self.assertEqual(RomanNumeral.num_to_roman(444), "CDXLIV")
        self.assertEqual(RomanNumeral.num_to_roman(449), "CDXLIX")
        self.assertEqual(RomanNumeral.num_to_roman(494), "CDXCIV")
        self.assertEqual(RomanNumeral.num_to_roman(499), "CDXCIX")
        self.assertEqual(RomanNumeral.num_to_roman(944), "CMXLIV")
        self.assertEqual(RomanNumeral.num_to_roman(949), "CMXLIX")
        self.assertEqual(RomanNumeral.num_to_roman(994), "CMXCIV")
        self.assertEqual(RomanNumeral.num_to_roman(999), "CMXCIX")



if __name__ == '__main__':
    unittest.main()
