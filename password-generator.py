# Joseph Brehm       9.28.22
# Random Password Generator
from operator import truediv
import random
import string
import re

# Handle if user inputs a number too long for a password
while True:
    numOfCharacters = int(input("Input length of characters: "))
    if numOfCharacters > 60:
        print("Error: Password must be > 60 characters")
        continue
    else:
        break

# Handle if user doesn't input correct conditions
while True:
    condition1 = input(
        "Select password conditions: L (lowercase), U (uppercase), D (digits), P (punctuation), W (whitespace): ")
    if ('L' or 'U' or 'D' or 'P' or 'W') not in condition1:
        print("Error: L, U, D, P, or W must be in conditions")
        continue
    else:
        break
condition1 = condition1.upper()
conditions = []

# Handle if the user uses spaces or types them all together
if re.match("\s", condition1):
    conditions = re.split("\s", condition1)
# checks if characters out of range were used
else:
    for i, c in enumerate(condition1):
        conditions.append(c)

options = {
    "L": string.ascii_lowercase,
    "U": string.ascii_uppercase,
    "D": string.digits,
    "W": string.whitespace,
    "P": string.punctuation
}


def generate():
    # Narrow down the options
    characterList = ""
    for value in conditions:
        # Test the condition is in the dictionary of options
        if value in options:
            characterList += options[value]

    joined = characterList
    rand_pswd = "".join(random.choice(joined) for i in range(numOfCharacters))
    print("Your password is: {0}".format(rand_pswd))


if __name__ == '__main__':
    generate()
