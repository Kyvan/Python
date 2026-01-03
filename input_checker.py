#!/home/kyvan/python_env/bin/python

class InputChecker:
    def is_integer(self, user_input):
        try:
            # Attempt to check if input to an integer
            int(user_input)
            print("It be a digit")
            return True
        except ValueError:
            # If a ValueError is raised, the input is not a valid integer
            print("Usage: Integer is expected")

    def is_string(self, user_input):
        try:
            # Attempt to check if input to a string
            str(user_input)
            print("It be a string")
            return True
        except ValueError:
            print("Usage: String is expected")

    def is_float(self, user_input):
        try:
            # Attempt to check if input to a float
            float(user_input)
            print("It be a float")
            return True
        except ValueError:
            print("Usage: Float is expected")
