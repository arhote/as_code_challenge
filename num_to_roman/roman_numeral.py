class RomanNumeral:
    ONE = "I"
    FOUR = "IV"
    FIVE = "V"
    NINE = "IX"
    TEN = "X"
    FORTY = "XL"
    FIFTY = "L"
    NINETY = "XC"
    ONE_HUNDRED = "C"
    FOUR_HUNDRED = "CD"
    FIVE_HUNDRED = "D"
    NINE_HUNDRED = "CM"
    ONE_THOUSAND = "M"

    def __init__(self, number):
        self.numeral = RomanNumeral.number_to_numeral(number);

    def __str__(self):
        return self.numeral

    @staticmethod
    def num_to_roman(number):
        return ""
