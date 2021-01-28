from num_to_roman.out_of_range import OutOfRangeException


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
        try:
            self.numeral = RomanNumeral.number_to_numeral(number)

    def __str__(self):
        return self.numeral

    @staticmethod
    def num_to_roman(number):
        if(number > 1 or number < 3999):
            msg = "The number you tried to enter is outside of the allowed values, please try again."
            raise OutOfRangeException(msg)


        return
