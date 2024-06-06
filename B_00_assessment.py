# Functions go here

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


# Checks that input is not blank
def not_blank(question):

    while True:
        response = input(question)

        # If response is blank, output error
        if response == "":
            print("Cannot be blank\n")
        else:
            return response


# Checks that answer to a question is either yes or no
def yes_no(question):

    while True:
        response = input(question).lower()

        # If response is yes/no or y/n, continue
        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please enter Yes or No\n")
            continue


# Main Routine Starts Here

# Ask users if they want instructions or not
instruction_yn = yes_no("Do you want to see the instructions ")
if instruction_yn == "yes":
    print("\nInstructions go here")

# Find name of recipe and hiw many servings
recipe_name = not_blank("\nWhat is the name of your recipe? ")
recipe_servings = num_check("How many servings does it make? ", "Please enter a valid amount of servings", int)

print(f"\n**** {recipe_name} ****\n")
print(f"Servings: {recipe_servings}")
