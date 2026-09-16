"""     UPC Validator
Created by: Brandon Barrett
Purpose: To validate 12 digit UPC's
Date of Creation September 16,2026

"""
# 036000291452 valid UPC for testing purposes

user_upc = input("Please the 12-digit UPC you would like validated:\n").strip()

while len(user_upc) != 12 or not user_upc.isdigit():
    user_upc = input(
        "\nThat input is invalid. \nPlease enter a 12 numerical digit UPC:\n").strip()

upc_validation_digit = user_upc[11]


def find_UPC(upc_to_validate, validation_digit=upc_validation_digit):
    odd_positioned_upc_digits = [upc_to_validate[0:11:2]]
    even_positioned_upc_digits = [upc_to_validate[1:11:2]]
    print(f"""Odd Positioned:{odd_positioned_upc_digits} \nEven Positioned:{even_positioned_upc_digits}
Validation Digit Type and value:{type(validation_digit)} {validation_digit}""")
    return


find_UPC(user_upc)
