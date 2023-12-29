# Author: Léon Brodbeck & Simon Durrer
def showpoly(a):
    str1 = ""
    nobits = len(a)
    for x in range(nobits - 2):
        if a[x] == '1':
            str1 += "+x**" + str(nobits - x - 1) if str1 else "x**" + str(nobits - x - 1)
    if a[nobits - 2] == '1':
        str1 += "+x" if str1 else "x"
    if a[nobits - 1] == '1':
        str1 += "+1"
    print(str1)

def toList(x):
    return [int(x[i]) for i in range(len(x))]

def toString(x):
    return "".join(str(i) for i in x)

def custom_zfill(s, width):
    return '0' * (width - len(s)) + s

def custom_rjust(s, width, char=' '):
    return char * (width - len(s)) + s

def divide(val1, val2):
    a = toList(val1)
    b = toList(val2)
    working = val1 + "\n"
    res = ""
    addspace = ""
    while len(b) <= len(a) and a:
        if a[0] == 1:
            del a[0]
            for j in range(len(b) - 1):
                a[j] ^= b[j + 1]
            if a:
                working += addspace + toString(b) + "\n" + addspace + "-" * len(b) + "\n"
                addspace += " "
                working += addspace + toString(a) + "\n"
                res += "1"
        else:
            del a[0]
            working += addspace + "0" * len(b) + "\n" + addspace + "-" * len(b) + "\n"
            addspace += " "
            working += addspace + toString(a) + "\n"
            res += "0"
    print("Result is", res)
    print("Remainder is", toString(a))
    print("Working is\n\n", custom_rjust(res, len(val1)), "\n", "-" * len(val1), "\n", working)
    return toString(a)

val1 = "011000100101"
val2 = "10011"
print("Binary form:", val1, "divided by", val2)
print("")
showpoly(val1)
showpoly(val2)

strzeros = custom_zfill("", len(val2) - 1)
val3 = val1 + strzeros

print("\nBinary form (added zeros):", val3, "divided by", val2)

res = divide(val3, val2)
print("Transmitted value is:", val1 + res)

