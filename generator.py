# Joseph Brehm       #9.25.22
import random
import string
numOfCharacters = int(input("input the length of charcaters: "))
condition1 = input(
    "Select password conditions: (l)owercase, (u)ppercase, (d)igits, (p)unctuation, (w)hitespace, (a)ll")
# condition2 = input(
#     "Select password conditions: (l)owercase, (u)ppercase, (d)igits, (p)unctuation, (w)hitespace, (a)ll, (s)top")
# condition3 = input(
#     "Select password conditions: (l)owercase, (u)ppercase, (d)igits, (p)unctuation, (w)hitespace, (a)ll, (s)top")
# condition4 = input(
#     "Select password conditions: (l)owercase, (u)ppercase, (d)igits, (p)unctuation, (w)hitespace, (a)ll, (s)top")
# condition5 = input(
#     "Select password conditions: (l)owercase, (u)ppercase, (d)igits, (p)unctuation, (w)hitespace, (a)ll, (s)top")
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
punctuation = string.punctuation
whitespace = string.whitespace
printable_all = string.printable

if condition1 == "l":
    print("Lowercase")
    condition2 = input(
        "Select password conditions: (u)ppercase, (d)igits, (p)unctuation, (w)hitespace, (a)ll, (s)top")
    if condition2 == "u":
        print("Lowercase + Uppercase")
        condition3 = input(
            "Select password conditions: (d)igits, (p)unctuation, (w)hitespace, (a)ll, (s)top")
        if condition3 == "d":
            print("Lowercase + Uppercase + Digits")
            joined = lowercase + uppercase + digits
            rand_pswd = "".join(random.choice(joined)
                                for i in range(numOfCharacters))
            print("Your random password is: {0}".format(rand_pswd))
        elif condition3 == "p":
            print("Lowercase + Digits + Punctuation")
            joined = lowercase + digits + punctuation
            rand_pswd = "".join(random.choice(joined)
                                for i in range(numOfCharacters))
        elif condition3 == "w":
            print("Lowercase + Digits + Whitespace")
            joined = lowercase + digits + whitespace
            rand_pswd = "".join(random.choice(joined)
                                for i in range(numOfCharacters))
        else:
            joined = lowercase + uppercase
            rand_pswd = "".join(random.choice(joined)
                                for i in range(numOfCharacters))
            print("Your random password is: {0}".format(rand_pswd))
    elif condition2 == "d":
        print("Lowercase + Digits")
        joined = lowercase + digits
        rand_pswd = "".join(random.choice(joined)
                            for i in range(numOfCharacters))
        print("Your random password is: {0}".format(rand_pswd))
    elif condition2 == "p":
        print("Lowercase + punctuation")
        joined = lowercase + punctuation
        rand_pswd = "".join(random.choice(joined)
                            for i in range(numOfCharacters))
        print("Your random password is: {0}".format(rand_pswd))
    elif condition2 == "w":
        print("Lowercase + whitespace")
        joined = lowercase + whitespace
        rand_pswd = "".join(random.choice(joined)
                            for i in range(numOfCharacters))
        print("Your random password is: {0}".format(rand_pswd))
    else:
        rand_pswd = "".join(random.choice(lowercase)
                            for i in range(numOfCharacters))
        print("Your random password is: {0}".format(rand_pswd))
elif condition1 == "u":
    print("Uppercase")
    rand_pswd = "".join(random.choice(uppercase)
                        for i in range(numOfCharacters))
    print("Your random password is: {0}".format(rand_pswd))
elif condition1 == "d":
    print("Digits")
    rand_pswd = "".join(random.choice(digits)
                        for i in range(numOfCharacters))
    print("Your random password is: {0}".format(rand_pswd))
elif condition1 == "p":
    print("Punctuation")
    rand_pswd = "".join(random.choice(punctuation)
                        for i in range(numOfCharacters))
    print("Your random password is: {0}".format(rand_pswd))
elif condition1 == "w":
    print("Whitespace")
    rand_pswd = "".join(random.choice(whitespace)
                        for i in range(numOfCharacters))
    print("Your random password is: {0}".format(rand_pswd))
else:
    print("Error, something went wrong")
