# -----------------------------------------------------------------------------
# Copyright © 2021
#
# EnPython Version 0.1
#
# EnPython: Basic feature expansion module.
# Simplifies stuff like sorting algorithms, etc...
#
# Creative Commons Zero v1.0 Universal
# -----------------------------------------------------------------------------

# -------
# Imports
# -------
import secrets
import string

# -------------------
# Sorting Algorithsms
# -------------------

# Verify that passed Variable is a list
def verify_list(array):
    if type(array) != list:
        print('Passed variable type is not "list".')
        return False
    else:
        return True


# Bubble Sort Algorithm
def bubble_sort(array):
    if not verify_list(array):
        return

    for i in range(len(array) - 1):
        for j in range(0, len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


# Insertion Sort Algorithm
def insertion_sort(array):
    if not verify_list(array):
        return

    for i in range(1, len(array)):
        j = array[i]
        k = i - 1

        while k >= 0 and j < array[k]:
            array[k + 1] = array[k]
            k -= 1
        array[k + 1] = j

    return array


# Selection Sort Algorithm
def selection_sort(array):
    if not verify_list(array):
        return

    for i in range(len(array)):
        j = i
        for k in range(i+1, len(array)):
            if array[j] > array[k]:
                j = k

        array[i], array[j] = array[j], array[i]

    return array


# Merge Sort Algorithm
def merge_sort(array):
    if not verify_list(array):
        return

    if not len(array) > 1:
        return

    list_mid = len(array) // 2
    list_left = array[:list_mid]
    list_right = array[list_mid:]

    merge_sort(list_right)
    merge_sort(list_left)

    i = 0
    j = 0
    k = 0

    while i < len(list_left) and j < len(list_right):
        if list_left[i] <= list_right[j]:
            array[k] = list_left[i]
            i += 1
        else:
            array[k] = list_right[j]
            j += 1
        k += 1

    while i < len(list_left):
        array[k] = list_left[i]
        i += 1
        k += 1

    while j < len(list_right):
        array[k] = list_right[j]
        j += 1
        k += 1

    return array


# Quick Sort Algorithm
def quick_sort(array):
    def partition(array, low, high):
        i = (low - 1)
        pivot = array[high]

        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]

        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1

    def actual_sort(array, low, high):
        if len(array) == 1:
            return array

        if low < high:
            p = partition(array, low, high)
            actual_sort(array, low, p - 1)
            actual_sort(array, p + 1, high)

    actual_sort(array, 0, len(array) - 1)
    return array


# ----------
# Converters
# ----------

# Converts Integer to Roman Numeral
def int_to_roman(integer_input):
    roman_numerals = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    regular_nummers = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    converted_string = ""
    i = len(regular_nummers) - 1
    while integer_input != 0:
        if regular_nummers[i] <= integer_input:
            converted_string += roman_numerals[i]
            integer_input -= regular_nummers[i]
        else:
            i -= 1
    return converted_string


# ------------
# Temperatures
# ------------

# Convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


# Convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return 5/9 * (fahrenheit - 32)


# Convert Celsius to Kelvin
def celsius_to_kelvin(celsius):
    return celsius + 273.15


# Convert Kelvin to Celsius
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


# --------
# Security
# --------

# Generates a password with customizable modifiers
def generate_password(length, include_uppercase, include_numbers, include_symbols):
    modifiers = string.ascii_lowercase

    if include_uppercase:
        modifiers += string.ascii_uppercase
    if include_numbers:
        modifiers += string.digits
    if include_symbols:
        modifiers += string.punctuation

    password = "".join(secrets.choice(modifiers) for i in range(length))

    return password
