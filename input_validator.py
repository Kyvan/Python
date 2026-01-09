#!/home/kyvan/python_env/bin/python


def is_integer(user_input):
    if user_input.isdigit():
        return True
    else:
        return False

def is_string(user_input):
    # Attempt to check if input is a string
    if user_input.isalpha():
        return True
    else:
        return False


def is_float(user_input):
    if is_integer(user_input):
        return False
    elif is_string(user_input):
        return False
    else:
        return True