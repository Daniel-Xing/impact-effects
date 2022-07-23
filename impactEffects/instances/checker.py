def numeric_checker(num) -> bool:
    if type(num) == int or type(num) == float:
        return True
    return False


def positive_checker(num) -> bool:
    if num < 0:
        return False
    return True


if __name__ == "__main__":
    print(numeric_checker("123"))
    print(numeric_checker(123))
    print(numeric_checker(123))
    print(numeric_checker(""))
