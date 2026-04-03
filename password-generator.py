
import string
import secrets

length = int(input("How long should the password be? "))

use_lowercase = input("Include lowercase letters? (y/n): ")
use_uppercase = input("Include uppercase letters? (y/n): ")
use_numbers = input("Include numbers? (y/n): ")
use_symbols = input("Include symbols? (y/n): ")

characters = ""

if use_lowercase == "y":
    characters += string.ascii_lowercase

if use_uppercase == "y":
    characters += string.ascii_uppercase

if use_numbers == "y":
    characters += string.digits

if use_symbols == "y":
    characters += string.punctuation

if characters == "":
    print("You must choose at least one character type.")
else:
    password = ""

    for i in range(length):
        password += secrets.choice(characters)

    print("Your password is:", password)
