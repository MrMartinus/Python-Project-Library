"""
Author: Martin Sliva
Date: 1.3.2024
License: GPLv3

Analysis of existing libraries/modules:
- range(): Built-in function, represents an immutable sequence of numbers, often used in for loops
- sorted(): Built-in function, returns a new sorted list from the items in iterable
- py-fibonacci library: External library, function fibonacci generates a fibonacci sequence
  
Justification for the Library:
- Main need for this library was for learning purposes and familiarizing with coding conventions
  
Constraints:
- Editor: I have not yet fully customized my editor and I do not know all of its features

Criteria for success:
- Create four functions that meet the requirements, and are at least somewhat effective
- Ensure the code is clean, well commented and documented, and check all PEP8 conventions
- Include examples
- Estimated time: 3 - 8 hours

"""


def my_range(start=1,stop=1,step=1):
    """
    - Returns list of values between start and stop, with step between values
    - Can be used in for cycles

    Arguments:
    - start (int): Start value
    - stop (int): End value, not counted in range
    - step (int, optional): Step between values, if not set defaults to 1

    Examples:
    >>> my_range(0,5,2)
    Output: [0, 2, 4]

    >>> my_range(0,5)
    Output: [0, 1, 2, 3, 4]

    Possible improvements:
    - Change start value to optional
    - Make my_range fully compatible with range
    """

    if not isinstance(start, int): # Failsafe if start is not integer error out
        return "error"
    elif not isinstance(stop, int): # Failsafe if stop is not integer error out
        return "error"
    elif not isinstance(step, int): # Failsafe if step is not integer error out
        return "error"
    elif step == 0: # Failsafe if the step is set to 0 error out
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

def caesar_cipher(text="", offset=0, mode=0):
    """
    - Returns ciphered (or deciphered) text
    - Use English alphabet as cipher alphabet
    - Print "?" on unknown alphabetic characters (e. g. diacritics)

    Arguments:
    - text (str): The text to cipher (or decipher)
    - offset (int, optional): Offset between characters in the English alphabet (e.g. A - C offset=3)
    - mode (int, optional): If set to one, means deciphering

    Examples:
    Ciphering
    >>> print(caesar_cipher("Hello world!", 3, 0))
    Output: Khoor zruog!

    Deciphering
    >>> print(caesar_cipher("Khoor zruog!",3,1))
    Output: Hello world!

    Possible improvements:
    - Remove the need for the uppercase alphabet
    """

    if not isinstance(text, str): # Failsafe if text is not string error out
        return "error"
    elif not isinstance(offset, int): # Failsafe if offset is not integer error out
        return "error"
    output = "" # Define output as empty string
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] # Define alphabet
    if mode == 1: # Detect if mode is set to deciphering
        offset = -offset # Set mode to deciphering
    for char in text: # Loop through all characters in text
        if char.lower() in alphabet: # If char is in alphabet list, case-insensitive
            new_number = (alphabet.index(char.lower()) + offset) % 26 # Assign number to character and add offset + fix underflow and overflow, case-insensitive
            if char.isupper(): # If original character was uppercase
                new_char = alphabet[new_number].upper() # Change number back to uppercase character
            else:
                new_char = alphabet[new_number] # Change number back to character
            output += new_char # Add character to the list
        else:
            output += char # If character is not in alphabet add it to the output
    return output # Return ciphered text

def my_sort(names):
    """
    - Returns names from names list sorted alphabetically (case-insensitive)
    - Uses a variant of Selection sort, but in descending order
    - Support for string, integer and float values

    Arguments:
    - names (list): Names to sort alphabetically

    Examples:
    >>> print(my_sort(['DeAndre Jordan', 'Deanna Russo', 'Deandre Ayton']))
    Output: ['Deandre Ayton', 'DeAndre Jordan', 'Deanna Russo']

    >>> print(my_sort(['Alojz', 'Cecil', 'Bob']))
    Output: ['Alojz', 'Bob', 'Cecil']

    Possible improvements:
    - Change the algorithm for a more efective one
    """

    if not isinstance(names, list): # Failsafe if names is not list error out
        return "error"
    output = [] # Define output as an empty list
    for name in range(len(names)): # Loop, repeats for the number of elements in names
        last = names[0] # Set last as the first element in names
        for name in names: # Loop through all elements in names
            if isinstance(name, str) and isinstance(last, str): # If both name and last are string
                if name.lower() > last.lower(): # Finds the alphabetically last element in names, case-insensitive
                    last = name # Set it as the current last element
            elif not isinstance(name, str) and not isinstance(last, str): # If neither name or last is string
                if name > last: # Finds the alphabetically last element in names, case-insensitive
                    last = name # Set it as the current last element
            else:
                if str(name) > str(last): # Finds the alphabetically last element in names, convert to string
                    last = name # Set it as the current last element
        names.remove(last) # Remove the alphabetically last element from names
        output.insert(0, last) # Insert the alphabetically last element at the beginning of the output list
    return output # Return the sorted output list

def fibonacci(n):
    """
    - Returns n (up to 20575) number from the Fibonacci sequence
    - The argument n must be positive and less than 20575

    Arguments:
    - n (int): The order of the desired number from the Fibonacci sequence

    Examples:
    >>> print(fibonacci(7))
    Output: 13

    >>> print(fibonacci(15))
    Output: 610

    Possible improvements:
    - Add support for larger numbers
    """
    if not isinstance(n, int): # Failsafe if n is not integer error out
        return "error"
    if n < 0: # Failsafe if n is set to negative value error out
        return "error"
    if n > 20575: # Failsafe if n is set to negative value error out
        return "The number exceeds the limit of 20575"
    sequence = [0, 1] # List consisting of first two Fibonacci numbers
    previous = sequence[-2] # Set previous as second number from end of list
    latest = sequence[-1] # Set latest as first number from end of list
    for i in range(n):
        sequence.append(previous + latest) # Append sum of previous and latest to the end of sequence
        previous = latest # Set previous as latest
        latest = sequence[-1] # Set latest as first number from end of list
    return sequence[n] # Return n number of Fibonacci sequence


"""
Readability:
- Code is consistent and follows PEP 8 conventions

Validate the program:
- Validated with all possible inputs

User-friendliness:
- Well-documented functions
- Examples
- Free license

Possible improvements:
- Clearer error messages

Time spent: cca 12 hours
"""