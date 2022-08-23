import numpy


def numeric_checker(num) -> bool:
    if type(num) == int or type(num) == float or type(num) == numpy.float64:
        return True
    return False


def positive_checker(num) -> bool:
    if num < 0:
        return False
    return True
