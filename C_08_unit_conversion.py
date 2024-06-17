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


def convert_g(val: float, unit_in: str, unit_out: str) -> float:
    conversion_grams = {'mg': 0.001, 'g': 1, 'kg': 1000}
    return val * conversion_grams[unit_in] / conversion_grams[unit_out]


def convert_ml(val: float, unit_in: str, unit_out: str) -> float:
    conversion_millilitres = {'ml': 1, 'l': 1000, 'c': 240, 'tbsp': 15, 'tsp': 5}
    return val * conversion_millilitres[unit_in] / conversion_millilitres[unit_out]


# Main Routine Starts Here

unit_dict = {
    "kilograms": "kg", "kg": "kg",
    "grams": "g", "g": "g",
    "milligrams": "mg", "mg": "mg",
    "litres": "l", "l": "l",
    "millilitres": "ml", "ml": "ml",
    "cups": "c", "c": "c",
    "tablespoons": "tbsp", "tbsp": "tbsp",
    "teaspoons": "tsp", "tsp": "tsp",
    "none": "", "": ""
}

# List to store ingredients
ingredients = []

while True:
    ing_name = input("\nWhat is the name of your ingredient? (xxx if entered all ingredients) ")
    if ing_name.lower() == "xxx":
        break
    ing_unit = string_checker("What unit of measurement does the ingredient use? (or none if no units, e.g. eggs) ",
                              unit_dict.keys())
    ing_amount = num_check("How many of this unit? ", "Please enter a number more than 0 (no fractions)", float)

    # Unit abbreviation
    ing_unit = unit_dict[ing_unit]

    # Add ingredient to the list
    ingredients.append((ing_name, ing_amount, ing_unit))

print()

for ing_name, ing_amount, ing_unit in ingredients:
    if ing_unit in ["g", "mg", "kg"]:
        new_amount = convert_g(ing_amount, ing_unit, 'g')

        # if it's a whole number, make it an int
        if new_amount == int(new_amount):
            new_amount = int(new_amount)
        # print list
        print(f"{ing_name}: {new_amount}g")

    elif ing_unit in ["ml", "l", "c", "tbsp", "tsp"]:

        new_amount = convert_ml(ing_amount, ing_unit, 'ml')

        # if it's a whole number, make it an int
        if new_amount == int(new_amount):
            new_amount = int(new_amount)
        # print list
        print(f"{ing_name}: {new_amount}mL")

    else:
        if ing_amount == int(ing_amount):
            ing_amount = int(ing_amount)
        print(f"{ing_name}: {ing_amount}")
