# Joseph Brehm       9.26.22
import random
import re
import string

numOfCharacters = int(input("input the length of charcaters: "))
condition1 = input(
    "Select password conditions: (l)owercase, (u)ppercase, (d)igits, (p)unctuation, (w)hitespace, (a)ll: ")
conditions = re.split("\s", condition1)
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
punctuation = string.punctuation
whitespace = string.whitespace
printable_all = string.printable


def gen(x):
    joined = x
    rand_pswd = "".join(random.choice(joined)
                        for i in range(numOfCharacters))
    print("Your password is: {0}".format(rand_pswd))


if 'a' in conditions and not ('l' or 'u' or 'd' or 'p' or 'w') in conditions:
    gen(printable_all)
elif 'l' in conditions and not ('a' or 'u' or 'd' or 'p' or 'w') in conditions:
    if 'u' in conditions and not ('d' or 'p' or 'w') in conditions:
        if 'd' in conditions and not ('p' or 'w') in conditions:
            if 'p' in conditions and not ('w') in conditions:
                if 'w' in conditions:
                    gen(lowercase + uppercase + digits + whitespace)
                else:
                    gen(lowercase + uppercase + digits + punctuation)
            elif 'w' in conditions and not ('p') in conditions:
                if 'p' in conditions:
                    gen(lowercase + uppercase + digits + punctuation)
                else:
                    gen(lowercase + uppercase + digits + whitespace)
            else:
                gen(lowercase + uppercase + digits)
        elif 'p' in conditions and not ('d' or 'w') in conditions:
            if 'd' in conditions and not ('w') in conditions:
                if 'w' in conditions:
                    gen(lowercase + uppercase + digits + whitespace)
                else:
                    gen(lowercase + uppercase + digits + digits)
            elif 'w' in conditions and not ('d') in conditions:
                if 'w' in conditions:
                    gen(lowercase + uppercase + digits + digits)
                else:
                    gen(lowercase + uppercase + digits + whitespace)
            else:
                gen(lowercase + uppercase + punctuation)
        elif 'w' in conditions and not ('p' or 'd') in conditions:
            if 'p' in conditions and not ('d') in conditions:
                if 'p' in conditions:
                    gen(lowercase + uppercase + digits + punctuation)
                else:
                    gen(lowercase + uppercase + digits + digits)
            elif 'd' in conditions and not ('p') in conditions:
                if 'd' in conditions:
                    gen(lowercase + uppercase + digits + digits)
                else:
                    gen(lowercase + uppercase + digits + punctuation)
            else:
                gen(lowercase + uppercase + whitespace)
        else:
            gen(lowercase + uppercase)
    elif 'd' in conditions and not ('u' or 'p' or 'w') in conditions:
        if 'u' in conditions and not ('p' or 'w') in conditions:
            print()
        elif 'p' in conditions and not ('u' or 'w') in conditions:
            print()
        elif 'w' in conditions and not ('p' or 'u') in conditions:
            print()
        else:
            gen(lowercase + digits)
    elif 'p' in conditions and not ('d' or 'u' or 'w') in conditions:
        if 'd' in conditions and not ('u' or 'w') in conditions:
            print()
        elif 'u' in conditions and not ('d' or 'w') in conditions:
            print()
        elif 'w' in conditions and not ('u' or 'd') in conditions:
            print()
        else:
            gen(lowercase + punctuation)
    elif 'w' in conditions and not ('d' or 'p' or 'u') in conditions:
        if 'd' in conditions and not ('p' or 'u') in conditions:
            print()
        elif 'p' in conditions and not ('d' or 'u') in conditions:
            print()
        elif 'u' in conditions and not ('p' or 'd') in conditions:
            print()
        else:
            gen(lowercase + whitespace)
    else:
        gen(lowercase)
elif 'u' in conditions and not ('l' or 'a' or 'd' or 'p' or 'w') in conditions:
    gen(uppercase)
elif 'd' in conditions and not ('l' or 'u' or 'a' or 'p' or 'w') in conditions:
    gen(digits)
elif 'p' in conditions and not ('l' or 'u' or 'd' or 'a' or 'w') in conditions:
    gen(punctuation)
elif 'w' in conditions and not ('l' or 'u' or 'd' or 'p' or 'a') in conditions:
    gen(whitespace)
else:
    print("Error")
