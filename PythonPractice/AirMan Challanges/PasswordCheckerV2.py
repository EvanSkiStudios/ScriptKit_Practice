import string
# when normal strings are just not enough


def password_checker(password_to_validate: str):

    # personally I hate these functions, they are gross
    def count_symbols_two(input_string):
        symbols = set(string.punctuation)
        symbol_count = 0

        for char in input_string:
            if char in symbols:
                symbol_count += 1
                if symbol_count >= 2:
                    return True

        return False

    def has_two_letters(input_string):
        capital_count = 0

        for char in input_string:
            if char.islower():
                capital_count += 1
                if capital_count >= 2:
                    return True

        return False

    def has_two_capital_letters(input_string):
        capital_count = 0

        for char in input_string:
            if char.isupper():
                capital_count += 1
                if capital_count >= 2:
                    return True

        return False

    max_length = 16
    required_length = 5

    if len(password_to_validate) > max_length:
        print(f"Password can not be longer then 16 characters")
        return False

    if len(password_to_validate) < required_length:
        print(f"Password can not be shorter then 5 characters")
        return False

    if not count_symbols_two(password_to_validate):
        print(f"Password must have more than 1 special char")
        return False

    if not has_two_letters(password_to_validate):
        print(f"Password must have more than 1 lowercase")
        return False

    if not has_two_capital_letters(password_to_validate):
        print(f"Password must have more than 1 capital")
        return False

    return True


# example
check = False
while not check:
    password = input(f"Input Password:")
    check = password_checker(password)
print(f"Password is Valid")
