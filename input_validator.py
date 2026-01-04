#!/home/kyvan/python_env/bin/python


def is_integer(user_input):
    if user_input.isdigit():
        return True
    else:
        # If a ValueError is raised, the input is not a valid integer
        print("Usage: Integer is expected")
        return False


def is_string(user_input):
    # Attempt to check if input is a string
    if user_input.isalpha():
        return True
    else:
        print("Usage: String is expected")
        return False


def is_white_space(user_input):
    if user_input.isspace():
        return True
    else:
        print("Usage: White Space is expected")
        return False


def is_float(user_input):
    if user_input.isdigit():
        print("Usage: Float is expected")
        return False
    else:
        try:
            float(user_input)
            return True
        except ValueError:
            print("Usage: Float is expected")


def is_float_no_output(user_input):
    try:
        float(user_input)
        return True
    except ValueError:
        return False


def is_special_character(user_input):
    if user_input.isdigit() or user_input.isalpha() or user_input.isspace() or is_float_no_output(user_input):
        print("Usage: Special Character is expected")
        return True
    else:
        return True
