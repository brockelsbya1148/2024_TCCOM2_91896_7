import pandas


# Checks that input is either a float or an integer that is more than zero and less than 100
def num_check(question, error, num_type):
    valid = False
    while not valid:
        try:
            response = input(question)
            response_num = num_type(response)
            if len(response) >= 100 or response_num <= 0:
                print(error)
            else:
                return response_num
        except ValueError:
            print(error)


# Checks that input is not blank
def not_blank(question):
    while True:
        response = input(question)
        if response == "":
            print("Cannot be blank")
        else:
            return response


# checks that users enter a valid response (e.g. yes/ no units) based on a list of options
def string_checker(question, valid_responses):
    error = "Please choose a valid answer"
    while True:
        response = input(question).lower()
        if response in valid_responses:
            return response
        print(error)


# Converts units into g and ml
def convert_unit(val: float, unit_in: str) -> float:
    conversion_units = {'mg': 0.001, 'g': 1, 'kg': 1000, 'ml': 1, 'l': 1000, 'c': 240, 'tbsp': 15, 'tsp': 5}
    return val * conversion_units.get(unit_in, 1)


# List to store ingredients
ingredients = []
store_ingredients = []

# Dictionary for unit conversions
unit_dict = {
    "kilograms": "kg", "kg": "kg",
    "grams": "g", "g": "g",
    "milligrams": "mg", "mg": "mg",
    "litres": "l", "l": "l",
    "millilitres": "ml", "ml": "ml",
    "cups": "c", "c": "c",
    "tablespoons": "tbsp", "tbsp": "tbsp",
    "teaspoons": "tsp", "tsp": "tsp",
    "": ""
}

while True:
    ing_name = not_blank("\nWhat is the name of your ingredient? (xxx to exit) ")
    if ing_name.lower() == "xxx":
        break
    ing_unit = string_checker("What unit of measurement does the ingredient use? (or leave blank if no units are"
                              " required, e.g. eggs) ", unit_dict.keys())
    if ing_unit == "":
        ing_amount = num_check(f"How many? ", "Please enter a number more than 0 and less than 100 (no fractions)",
                               float)
    else:
        ing_amount = num_check(f"How many {ing_unit}? ", "Please enter a number more than 0 and less than 100 "
                                                         "(no fractions)", float)

    store_unit = string_checker(f"\nWhat unit of measurement do you buy {ing_name} in? (leave blank if no units) ",
                                unit_dict.keys())
    store_amount = num_check(f"How many {store_unit}? ", "Please enter a number more than 0 and less than 100 "
                                                         "(no fractions)", float)
    store_cost = num_check("How much does it cost? $", "Please enter a price", float)

    # Unit conversion
    ing_unit = unit_dict[ing_unit]
    store_unit = unit_dict[store_unit]

    # Add ingredient to the list
    ingredients.append({"Ingredient": ing_name, "Amount": ing_amount, "Unit": ing_unit})
    store_ingredients.append({"Ingredient": ing_name, "Amount": store_amount, "Unit": store_unit, "Price": store_cost})

ingredient_frame = pandas.DataFrame(ingredients)
store_price_frame = pandas.DataFrame(store_ingredients)

# Display the formatted DataFrames without setting the index
print("\n*** Ingredients ***\n")
print(ingredient_frame.to_string(index=False), "\n")
print("*** Store Price ***\n")
print(store_price_frame.to_string(index=False))
