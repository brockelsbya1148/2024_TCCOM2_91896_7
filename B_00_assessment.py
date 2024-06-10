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


# checks that users enter a valid response (e.g. yes/ no
# units) based on a list of options
def string_checker(question, valid_responses):
    error = "Please choose a valid answer"

    while True:

        response = input(question).lower()

        for item in valid_responses:
            if response == item:
                return item

        print(error)


# Main Routine Starts Here

# String checker lists
yes_no = {
    "yes": "yes", "y": "yes",
    "no": "no", "n": "no"
}

unit_dict = {
    "kilograms": "kg", "kg": "kg",
    "grams": "g", "g": "g",
    "milligrams": "mg", "mg": "mg",
    "litres": "l", "l": "l",
    "millilitres": "ml", "ml": "ml",
    "cups": "c", "c": "c",
    "tablespoons": "tbsp", "tbsp": "tbsp",
    "teaspoons": "tsp", "tsp": "tsp",
    "none": ""
}

# Ask users if they want instructions or not
instruction_yn = string_checker("Do you want to see the instructions ", yes_no.keys())
# y/n conversion
instruction_yn = yes_no[instruction_yn]
# print instructions
if instruction_yn == "yes":
    print("\nInstructions go here")

# Find name of recipe and how many servings
recipe_name = not_blank("\nWhat is the name of your recipe? ")
recipe_servings = num_check("How many servings does it make? ", "Please enter a valid amount of servings", int)

# *** Ask user for ingredients ***

# List to store ingredients
ingredients = []

while True:
    ing_name = not_blank("\nWhat is the name of your ingredient? (xxx if entered all ingredients) ")
    if ing_name.lower() == "xxx":
        break
    ing_unit = string_checker("What unit of measurement does the ingredient use? (or none if no units, e.g. eggs) ",
                              unit_dict.keys())
    ing_amount = num_check("How many of this unit? ", "Please enter a number more than 0 (no fractions)", float)

    # Unit conversion
    ing_unit = unit_dict[ing_unit]

    # Add ingredient to the list
    ingredients.append((ing_name, ing_amount, ing_unit))

# *** Print area ***

# Print name and servings
print(f"\n**** {recipe_name} ****\n")
print(f"Servings: {recipe_servings}")


# Print all ingredients
print("\n*** Ingredients ***\n")
for ing_name, ing_amount, ing_unit in ingredients:
    # if it's a whole number, make it an int
    if ing_amount == int(ing_amount):
        ing_amount = int(ing_amount)
    # print list
    print(f"{ing_name}: {ing_amount} {ing_unit}")
