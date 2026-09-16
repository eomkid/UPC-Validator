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


def find_UPC(upc_to_validate):
    odd_upc_digits = [upc_to_validate[0:13:2]]
    even_upc_digits = [upc_to_validate[1:13:2]]
    print(f"{odd_upc_digits} {even_upc_digits}")
    return


find_UPC(user_upc)
