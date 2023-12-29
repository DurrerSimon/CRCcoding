# Author: Léon Brodbeck & Simon Durrer

def showpoly(a):
    # Converts binary polynomial to human-readable format
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
    # String to list of integers
    return [int(x[i]) for i in range(len(x))]

def toString(x):
    # List of integers to string
    return "".join(str(i) for i in x)

def custom_zfill(s, width):
    # Fills string with zeros up to specified width
    return '0' * (width - len(s)) + s

def custom_rjust(s, width, char=' '):
    # Right-justifies a string
    return char * (width - len(s)) + s

def divide(val1, val2):
    # Performs CRC division
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

def decodeCRC(transmitted_val, generator_polynomial):
    # Decodes CRC and checks data integrity
    transmitted_val_list = toList(transmitted_val)
    generator_polynomial_list = toList(generator_polynomial)
    remainder = divide(transmitted_val, generator_polynomial)
    if set(remainder) == {'0'}:
        print("Data is valid")
        original_data = transmitted_val[:-len(generator_polynomial) + 1]
        print("Original Data:", toString(original_data))
    else:
        print("Data is corrupted")

# Main variabels
transmitted_val = "0110001001010001"  # Transmitted value including CRC
generator_polynomial = "10011"       # Generator polynomial used for encoding

# Main script
decodeCRC(transmitted_val, generator_polynomial)

