"""     UPC Validator
Created by: Brandon Barrett
Purpose: To validate 12 digit UPC's
Date of Creation September 16,2026

"""
# 123456789101 number for testing purposes

user_upc = input("Please the UPC you would like validated:\n")

while len(user_upc) != 12 or not user_upc.isdigit():
    user_upc = input(
        "\nThat input is invalid. \nPlease enter a 12 numerical digit UPC:\n")

print(f"{user_upc} {type(user_upc)}")
