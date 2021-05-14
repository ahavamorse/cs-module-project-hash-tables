import math

# Day Three Class Notes
# Hash Tables can be useful in problems that need a quick searches with large amounts of data
# The sorting (or something else) can be done ahead of time just once instead of each time

records = [
    ('Alice', 'Engineering'),
    ('Bob', 'Sales'),
    ('Carol', 'Sales'),
    ('Sarah', 'Sales'),
    ('Pranjal', 'Sales'),
    ('Dave', 'Engineering'),
    ('Erin', 'Engineering'),
    ('Frank', 'Engineering'),
    ('Grace', 'Marketing'),
    ('Charles', 'Marketing'),
    ('Brian', 'Marketing'),
    ('Jordan', 'Marketing')
]


# Need to print all departments
# Need to print everyone in Engineering

# Proposed Dictionary
#   Keys: Departments
#   Values: Array of names

# This function is O(n)
#
def build_index(recs):
    index = {}

    for record in recs:
        name, dept = record

        # Check if department is already in index
        if dept in index:
            # If it is, add name to list
            index[dept].append(name)
        # If not create new key with list with the name in it
        else:
            index[dept] = [name]

    return index


department_index = build_index(records)

print(department_index.keys())
print(department_index["Engineering"])  # This will be O(1) no matter what key is used (but uses more space)


# A lookup table is useful to speed up time consuming computations that must be repeated many times

# Example problem: Find inverse square root of numbers between 1 and 1000

# Proposed Dictionary
#   Keys will be numbers
#   Values will be the result of get_inverse_square

def build_sqrt_lookup_table():
    lookup_table = {}
    for i in range(1, 1001):
        lookup_table[i] = get_inverse_square(i)
    return lookup_table


def get_inverse_square(num):
    return 1 / math.sqrt(num)


sqrt_lookup_table = build_sqrt_lookup_table()

print(sqrt_lookup_table[3])
print(sqrt_lookup_table[234])


# Given a string, find out how many times each letter appears init

# Proposed Dictionary
#   Keys will be the letters
#   Values will be number of times it appears

def letter_count(s):
    dict = {}
    for char in s:
        if char.isspace():
            continue

        if char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1
    return dict


print(letter_count("aaabbc"))
print(letter_count("Hello!"))
print(letter_count("The quick brown fox jumps over the lazy dogs"))


def double_letter(s):
    dict = {}
    for char in s:
        if char.isspace():
            continue

        if char not in dict:
            dict[char] = 1
        else:
            return char


print(double_letter("abcdefghijklmnopqrstuvwxyz a"))

# Dictionaries are very useful in substitution ciphers (transfer data from one thing to another)

code_table = {
    'A': 'Z',
    'B': 'Y',
    'C': 'X',
    'D': 'W',
    'E': 'V',
    'F': 'U',
    'G': 'T',
    'H': 'S',
    'I': 'R',
    'J': 'Q',
    'K': 'P',
    'L': 'O',
    'M': 'N',
    'N': 'M',
    'O': 'L',
    'P': 'K',
    'Q': 'J',
    'R': 'I',
    'S': 'H',
    'T': 'G',
    'U': 'F',
    'V': 'E',
    'W': 'D',
    'X': 'C',
    'Y': 'B',
    'Z': 'A'
}


def encode(plain_text):
    cipher = ""

    for char in plain_text:
        if char.isspace():
            cipher += ' '
        else:
            cipher += code_table[char]
    return cipher


def decode(cipher_text):
    plain_text = ''
    for char in cipher_text:
        if char.isspace():
            plain_text += ' '
        else:
            plain_text += code_table[char]
    return plain_text


print(encode("DICTIONARIES ARE AWESOME"))
print(decode("WRXGRLMZIRVH ZIV ZDVHLNV"))


# Day Four Class Notes

# Jewels and Stones
# List of jewels and stones are passed in
# Find out how many of the stones are jewels

# Naive solution:
# Use nested loops to compare each jewel and each stone

# My Proposed solution:
# Create dictionary to count number of each type of stone
# Then go through the jewels and add up the number of each among the stones
# Dictionary:
#   Keys: char from stones
#   Values: # of occurrences
# Then for each char in jewels how many times is it in stones?
# So how many of each jewel do we have? Add up the totals for result

# Better idea:
# Go through char in jewels create a key with value 0
# Then for char in stones, if it is in the dict, increment the value
# Last add up values in dict to get total num of jewels


def numJewelsInStones(self, jewels, stones) -> int:
    jewel_count = 0
    jewels_dict = {}
    for jewel in jewels:
        jewels_dict[jewel] = 0

    for stone in stones:
        if stone in jewels_dict:
            jewel_count += 1

    return jewel_count


# print(numJewelsInStones("", ""))


# Happy Number
# input is a number, output is a bool
# add up the squares of each digit of the number
# do so over and over until you get 1 or repeat the same number

# My Proposed Solution:
# Find sum of square of each digit in number
# if result is one return true or if we've already seen number return false
# otherwise store number in set and repeat process

seen_values = set()

def isHappy(self, n) -> bool:

    if n == 1:
        return True
    elif n in seen_values:
        return False
    else:
        result = 0
        for digit in str(n):
            result += int(digit) ** 2
        seen_values.add(n)
        return isHappy(result)

print(isHappy(n))
