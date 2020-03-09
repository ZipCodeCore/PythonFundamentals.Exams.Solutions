from typing import List, TypeVar

N = TypeVar('N', int, float)


def find_lowest_value(list_in: List[N]) -> N:
    """
    Returns the lowest value in a list of numbers.

    :param list_in: A list of numbers (integers and/or floats)
    :return: The lowest number in the list.
    """
    list_in.sort()
    return list_in[0]


def find_highest_value(list_in: List[N]) -> N:
    """
    Returns the highest value in a list of numbers.

    :param list_in: A list of numbers (integers and/or floats)
    :return: The highest number in the list.
    """
    list_in.sort()
    return list_in[-1]


def compare_two_numbers(a: N, b: N) -> int:
    """
    Compares two numbers.

    If the numbers are the same, this function will return the number 0.
    If the first number is greater than the second, this function will return the number 1.
    If the second number is greater than the second, this function will return the number -1.

    :param a: The first number.
    :param b: The second number.
    :return: an integer 0, 1, or -1
    """
    if a == b:
        return 0
    elif a > b:
        return 1
    else:
        return -1


def compare_two_strings(a: str, b: str) -> int:
    """
    Compares two strings.

    If the strings have the same length, this function will return the number 0.
    If the first string is longer than the second string, this function will return the number 1.
    If the second string is longer than the first string, this function will return the number -1.

    :param a: The first string.
    :param b: The second string.
    :return: an integer 0, 1, or -1
    """
    compare_two_numbers(len(a), len(b))
