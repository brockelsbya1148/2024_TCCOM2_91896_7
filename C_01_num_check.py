# Checks that input is either a float or an integer that is more than zero
def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Testing
integer_test = num_check("Please enter an integer ", "Please enter an integer that is more than 0\n", int)
print("You wrote", integer_test, "\n")

float_test = num_check("Please enter a float ", "Please enter a float that is more than 0\n", float)
print("You wrote", float_test, "\n")
