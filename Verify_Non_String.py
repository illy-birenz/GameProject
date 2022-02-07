def verify_non_string(input_test):
    try:
        input_test = int(input_test)
    except ValueError:
        print(
            f"Value error, you can only insert numbers, characters or strings will not be accepted -> value entered was '{input_test}'")
        return False
    except TypeError:
        print(
            f"Type error, you can only insert numbers, characters or strings will not be accepted -> value entered was '{input_test}'")
        return False
    return input_test
