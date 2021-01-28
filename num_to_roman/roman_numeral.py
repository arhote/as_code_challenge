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
        self.numeral = RomanNumeral.num_to_roman(number)

    def __str__(self):
        return self.numeral

    @staticmethod
    def num_to_roman(number):
        if number < 1 or number > 3999:
            msg = "The number you tried to enter is outside of the allowed values, please try again."
            raise OutOfRangeException(msg)

        running_count = number
        numeral = ""

        while running_count > 0:
            if running_count >= 1000:
                running_count -= 1000
                numeral += RomanNumeral.ONE_THOUSAND
            elif running_count >= 900:
                running_count -= 900
                numeral += RomanNumeral.NINE_HUNDRED
            elif running_count >= 500:
                running_count -= 500
                numeral += RomanNumeral.FIVE_HUNDRED
            elif running_count >= 400:
                running_count -= 400
                numeral += RomanNumeral.FOUR_HUNDRED
            elif running_count >= 100:
                running_count -= 100
                numeral += RomanNumeral.ONE_HUNDRED
            elif running_count >= 90:
                running_count -= 90
                numeral += RomanNumeral.NINETY
            elif running_count >= 50:
                running_count -= 50
                numeral += RomanNumeral.FIFTY
            elif running_count >= 40:
                running_count -= 40
                numeral += RomanNumeral.FORTY
            elif running_count >= 10:
                running_count -= 10
                numeral += RomanNumeral.TEN
            elif running_count >= 9:
                running_count -= 9
                numeral += RomanNumeral.NINE
            elif running_count >= 5:
                running_count -= 5
                numeral += RomanNumeral.FIVE
            elif running_count >= 4:
                running_count -= 4
                numeral += RomanNumeral.FOUR
            else:
                running_count -= 1
                numeral += RomanNumeral.ONE

        return numeral
