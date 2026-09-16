"""     UPC Validator
Created by: Brandon Barrett
Purpose: To validate 12 digit UPC's
Date of Creation September 16,2026

"""
user_upc = input("Please the UPC you would like validated:\n")
while len(user_upc) != 12:
    user_upc = input("Please enter a 12 numerical digit UPC:\n")
print(f"{user_upc}")
