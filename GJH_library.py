 #####        # #     #
#     #       # #     #         #      # #####  #####    ##   #####  #   #
#             # #     #         #      # #    # #    #  #  #  #    #  # #
#  ####       # #######         #      # #####  #    # #    # #    #   #
#     # #     # #     #         #      # #    # #####  ###### #####    #
#     # #     # #     #         #      # #    # #   #  #    # #   #    #
 #####   #####  #     #         ###### # #####  #    # #    # #    #   #
                        #######

"""
Author: Martin Sliva
Date: 30.12.2024
Licence: GPLv3

Analysis of Existing Libraries/Modules:
- range(): Build-in function, represents an immutable sequence of numbers, commonly used in for loops
- sorted(): Build-in function, returns a new sorted list from the items in iterable
- py-fibonacci library: External library, function fibonacci generates a fibonacci sequence
  
Justification for the Library:
- Main need for this library was learning purposes and familiarizing with coding conventions
  
Constraints:
- Editor: I have not fully customized my editor yet and I do not know all of it functions

Criteria for Success:
- Create four functions that meet the requirements and are at least somewhat effective
- Ensure the code is clean, well commented and documented and check all PEP8 conventions
- Include examples
- Estimated time: 3 - 8 hours

"""


####################################################
#  _ __ ___  _   _     _ __ __ _ _ __   __ _  ___  #
# | '_ ` _ \| | | |   | '__/ _` | '_ \ / _` |/ _ \ #
# | | | | | | |_| |   | | | (_| | | | | (_| |  __/ #
# |_| |_| |_|\__, |   |_|  \__,_|_| |_|\__, |\___| #
#             __/ |_____                __/ |      #
#            |___/______|              |___/       #
####################################################
"""
- Returns list of values between start and stop, with step between values
- Can be used in for cycles

Arguments:
- start (int): Starting value
- stop (int): Final value, is not counted to range
- step (int, optional): Step between values, if not set defaults to 1

Examples:
>>> list(my_range(0,5,2))
Output: [0, 2, 4]

>>> list(my_range(0,5))
Output: [0, 1, 2, 3, 4]

Possible improvements:
- Change start value to optional
- Make my_range fully compatible with range
"""

def my_range(start=1,stop=1,step=1):
    if type(start) != type(1): # Fail-safe if start is not integer error out
        return "error"
    elif type(stop) != type(1): # Fail-safe if stop is not integer error out
        return "error"
    elif type(step) != type(1): # Fail-safe if step is not integer error out
        return "error"
    elif step == 0: # Fail-safe if the step is set to 0 error out
        return "error"
    output = [] # Define output as an empty list
    if step > 0: # If step is positive
        while start < stop:
            output.append(start) # Append curent start to output
            start += step # Add step to start
    else: # If step is negative
        while start > stop:
            output.append(start) # Append curent start to output
            start += step # Add step to start
    return output # Return range


################################################################
#                                     _       _                #
#                                    (_)     | |               #
#   ___ __ _  ___  ___  __ _ _ __ ___ _ _ __ | |__   ___ _ __  #
#  / __/ _` |/ _ \/ __|/ _` | '__/ __| | '_ \| '_ \ / _ \ '__| #
# | (_| (_| |  __/\__ \ (_| | | | (__| | |_) | | | |  __/ |    #
#  \___\__,_|\___||___/\__,_|_|  \___|_| .__/|_| |_|\___|_|    #
#                           ______     | |                     #
#                          |______|    |_|                     #
################################################################
"""
- Returns ciphered (or deciphered) text
- Using english alphabet as ciphering alphabet
- On unknown alphabetical characters print "?" (etc. diacritics)

Arguments:
- text (str): Text to be ciphered (or deciphered)
- offset (int, optional): Offset between characters in english alphabet (etc. A - C offset=3)
- mode (int, optional): If set to one means deciphering

Examples:
Ciphering
>>> print(caesar_cipher("Hello world!", 3, 0))
Output: Khoor zruog!

Deciphering
>>> print(caesar_cipher("Khoor zruog!",3,1))
Output: Hello world!

Possible improvements:
- Remove the need for uppercase alphabet
"""

def caesar_cipher(text="", offset=0, mode=0):
    if type(text) != type("A"): # Fail-safe if text is not string error out
        return "error"
    elif type(offset) != type(1): # Fail-safe if offset is not integer error out
        return "error"
    output = "" # Define output as empty string
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] # Define alphabet
    alphabet_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"] # Define uppercase alphabet
    if mode == 1: # Detect if mode is set to deciphering
        offset = -offset # Set mode to deciphering
    for char in text: # Loop through all characters in text
        if char.isalpha(): # Check if character is alphabetical
            if char in alphabet: # Check if it is in alphabet list
                new_number = (alphabet.index(char) + offset) % 26 # Assign number to character and add offset + fix underflow and overflow
                new_char = alphabet[new_number] # Change number back to character
                output += new_char # Add character to the list
            elif char in alphabet_upper: # Check if it is in alphabet_upper list
                new_number = (alphabet_upper.index(char) + offset) % 26 # Assign number to character and add offset + fix underflow and overflow
                new_char = alphabet_upper[new_number] # Change number back to character
                output += new_char # Add character to the list
            else: # If not in alphabet of alphabet_upper list
                output += "?" # If character is alphabetical, but is not in alphabet of alphabet_upper assign it question mark (may be due to the use of diacritics)
        else:
            output += char # If character is not alphabetical add it to the output
    
    return output # Return ciphered text


############################################
#                                     _    #
#                                    | |   #
#  _ __ ___  _   _     ___  ___  _ __| |_  #
# | '_ ` _ \| | | |   / __|/ _ \| '__| __| #
# | | | | | | |_| |   \__ \ (_) | |  | |_  #
# |_| |_| |_|\__, |   |___/\___/|_|   \__| #
#             __/ |_____                   #
#            |___/______|                  #
############################################
"""
- Returns names from names list sorted alphabetically (case-insensitive)
- Using variant of Selection sort, but in descending order
- Argument names must contain only string values

Arguments:
- names (list): Names to be sorted alphabetically

Examples:
>>> print(my_sort(['DeAndre Jordan', 'Deanna Russo', 'Deandre Ayton']))
Output: ['Deandre Ayton', 'DeAndre Jordan', 'Deanna Russo']

>>> print(my_sort(['Alojz', 'Cecil', 'Bob']))
Output: ['Alojz', 'Bob', 'Cecil']

Possible improvements:
- Changing algorithm for more efective one
"""

def my_sort(names):
    if type(names) != type(["A", "B"]): # Fail-safe if names is not list error out
        return "error"
    output = []  # Define output as an empty list
    for name in range(len(names)):  # Loop, repeats for the number of elements in names
        last = names[0]  # Set last as the first element in names
        for name in names:  # Loop through all elements in names
            if type(name) != type("A"): # Fail-safe if name is not string error out
                return "error"
            if name.lower() > last.lower():  # Finds the alphabetically last element in names, case-insensitive
                last = name  # Set it as the current last element
        names.remove(last)  # Remove the alphabetically last element from names
        output.insert(0, last)  # Insert the alphabetically last element at the beginning of the output list
    return output  # Return the sorted output list


##############################################
#   __ _ _                                _  #
#  / _(_) |                              (_) #
# | |_ _| |__   ___  _ __   __ _  ___ ___ _  #
# |  _| | '_ \ / _ \| '_ \ / _` |/ __/ __| | #
# | | | | |_) | (_) | | | | (_| | (_| (__| | #
# |_| |_|_.__/ \___/|_| |_|\__,_|\___\___|_| #
##############################################
"""
- Returns n (up to 20575) number from fibonacci sequence
- Argument n must be positive and smaller than 20575

Arguments:
- n (int): The order of the desired number from the fibonacci sequence

Examples:
>>> print(fibonacci(7))
Output: 13

>>> print(fibonacci(15))
Output: 610

Possible improvements:
- Add support for bigger numbers
"""

def fibonacci(n):
    if n < 0: # Fail-safe if n is set to negative value error out
        return "error"
    if n > 20575: # Fail-safe if n is set to negative value error out
        return "The number exceeds the limit of 20575"
    sequence = [0, 1] # List consisting of first two Fibonacci numbers
    previous = sequence[-2] # Set previous as second number from end of list
    latest = sequence[-1] # Set latest as first number from end of list
    for i in range(n):
        sequence.append(previous + latest) # Append sum of previous and latest to the end of sequence
        previous = latest # Set previous as latest
        latest = sequence[-1] # Set latest as first number from end of list
    return sequence[n] # Return n number of Fibonacci sequence