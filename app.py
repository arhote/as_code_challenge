from num_to_roman.exceptions import OutOfRangeException
from num_to_roman.roman_numeral import RomanNumeral

while True:
    """
    Attempt to get valid input
    """
    while True:
        try:
            number = int(input("Please enter a number to convert to Roman Numerals: "))
            break
        except ValueError:
            print("That was not a valid number. Please try again.")
        except KeyboardInterrupt:
            quit()

    try:
        print(RomanNumeral(number))
    except OutOfRangeException as ex:
        print(ex.message)
