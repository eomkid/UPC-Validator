"""     UPC Validator
Created by: Brandon Barrett
Purpose: To validate 12 digit UPC's
Date of Creation September 16,2026
"""
# 036000291452 valid UPC for testing purposes
# odd positions are to be multipled by 3
# add all values together the mod 10
# Result should be 0

user_upc = input("Please the 12-digit UPC you would like validated:\n").strip()

while len(user_upc) != 12 or not user_upc.isdigit():
    user_upc = input(
        "\nThat input is invalid. \nPlease enter a 12 numerical digit UPC:\n").strip()
user_upc = list(user_upc)
upc_validation_digit = int(user_upc[11])
print(f"{user_upc}")

# def find_UPC(upc_to_validate, validation_digit: int = upc_validation_digit):
#     odd_positioned_upc_digits = list([upc_to_validate[0:11:2]])
#     even_positioned_upc_digits = list([upc_to_validate[1:11:2]])
#     print(f"Runs")
#     return


# find_UPC(user_upc)
