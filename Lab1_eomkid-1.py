"""     UPC Validator
Created by: Brandon Barrett
Purpose: To validate 12 digit UPC's
Date of Creation September 16,2026
"""

user_upc = input(
    "Please enter the 12-digit UPC you would like validated:\n").strip()

while len(user_upc) != 12 or not user_upc.isdigit():
    user_upc = input(
        "\nThat input is invalid. \nPlease enter a 12 numerical digit UPC:\n").strip()

user_upc = list(map(int, user_upc))

upc_validation_digit = int(user_upc[11])


def find_UPC(upc_to_validate):
    odd_positioned_upc_digits = upc_to_validate[0:11:2]
    even_positioned_upc_digits = upc_to_validate[1:11:2]
    odd_positioned_tripled = [digit * 3 for digit in odd_positioned_tripled]

    validation_digit_check = sum(odd_positioned_tripled +
                                 even_positioned_upc_digits) % 10

    return validation_digit_check


calc_digit = find_UPC(user_upc)
if calc_digit == upc_validation_digit or 10 - calc_digit == upc_validation_digit:
    print(f"Valid UPC: Good to go")
else:
    print("Invalid UPC: Please check that you entered the right UPC and run the program again.")
