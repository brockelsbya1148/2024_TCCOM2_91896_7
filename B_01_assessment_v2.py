# Functions go here
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

        # If response is blank, output error
        if response == "":
            print("Cannot be blank")
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


# Converts units into a common unit
def convert_unit(val: float, unit_in: str) -> float:
    conversion_units = {'mg': 0.001, 'g': 1, 'kg': 1000, 'ml': 1, 'l': 1000, 'c': 240, 'tbsp': 15, 'tsp': 5}
    if unit_in in conversion_units:
        return val * conversion_units[unit_in]
    else:
        return val  # No conversion needed if no unit


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
    "": ""
}

# Ask users if they want instructions or not
instruction_yn = string_checker("Do you want to see the instructions? (yes/no) ", yes_no.keys())
# y/n conversion
instruction_yn = yes_no[instruction_yn]
# print instructions
if instruction_yn == "yes":
    print("""
    Welcome to the Recipe Cost Calculator! This tool helps you determine the total cost of making a recipe and the cost
    per serving. Follow these steps to use the calculator:

    1. Enter the recipe name:
       - Type the name of your recipe when asked.

    2. Enter the number of servings:
       - Provide the number of servings your recipe makes. This should be a positive integer.

    3. Enter ingredients:
       - For each ingredient in your recipe:
         - Enter the ingredient name.
         - Specify the unit of measurement (e.g., grams, cups) or leave it blank if the ingredient has no specific unit
         (e.g., eggs).
         - Provide the amount of the ingredient needed. This should be a positive number.
         - To stop entering ingredients, type "xxx" when asked for the ingredient name.

    4. Enter store prices for ingredients:
       - For each ingredient you entered:
         - Specify the unit of measurement in which you buy the ingredient from the store (e.g., grams, kilograms,
         liters) or type "none" if there is no specific unit.
         - Provide the quantity of the ingredient you buy from the store in that unit. This should be a positive number.
         - Enter the cost of that quantity of the ingredient. This should be a positive number.

    5. Review the results:
       - The calculator will display:
         - The name of your recipe and the number of servings.
         - A list of all ingredients with their quantities.
         - The cost of each store-bought ingredient and the quantity purchased.
         - The total cost for all store-bought ingredients.
         - The cost per unit of each ingredient used in the recipe.
         - The total cost for making the recipe.
         - The cost per serving of the recipe.
    """)

# Find name of recipe and how many servings
recipe_name = not_blank("\nWhat is the name of your recipe? ")
recipe_servings = num_check("How many servings does it make? ", "Please enter a reasonable amount of servings", int)

# *** Ask user for ingredients ***

# Lists to store ingredients
ingredients = []
store_ingredients = []
prices_list = []
calc_prices_list = []
ing_name_list = []
ing_amount_list = []
ing_unit_list = []
store_amount_list = []
store_unit_list = []
ing_cost_list = []

ingredient_dict = {
    "Ingredient": ing_name_list,
    "Amount": ing_amount_list,
    "Unit": ing_unit_list
}

store_dict = {
    "Ingredient": ing_name_list,
    "Amount": store_amount_list,
    "Unit": store_unit_list,
    "Price": prices_list
}

price_dict = {
    "Ingredient": ing_name_list,
    "Amount": ing_amount_list,
    "Price": ing_cost_list
}

while True:
    ing_name = not_blank("\nWhat is the name of your ingredient? (xxx to exit) ")
    if ing_name.lower() == "xxx":
        break
    ing_unit = string_checker("What unit of measurement does the ingredient use? (or leave blank if no units are "
                              "required, e.g. eggs) ", unit_dict.keys())
    if ing_unit == "":
        ing_amount = num_check(f"How many? ", "Please enter a number more than 0 and less than 100 (no fractions)",
                               float)
    else:
        ing_amount = num_check(f"How many {ing_unit}? ", "Please enter a number more than 0 and less than "
                                                         "100 (no fractions)", float)

    store_unit = string_checker(f"\nWhat unit of measurement do you buy {ing_name} in? (leave blank if no units) ",
                                unit_dict.keys())
    if store_unit == "":
        store_amount = num_check(f"How many? ", "Please enter a number more than 0 and less than 100(no fractions)",
                                 float)
    else:
        store_amount = num_check(f"How many {store_unit}? ", "Please enter a number more than 0 and less than 100 "
                                                             "(no fractions)", float)
    store_cost = num_check("How much does it cost? $", "Please enter a price", float)

    # Remove decimals on whole numbers
    if store_amount == int(store_amount):
        store_amount = int(store_amount)
    if ing_amount == int(ing_amount):
        ing_amount = int(ing_amount)

    # Unit conversion
    ing_unit = unit_dict[ing_unit]
    store_unit = unit_dict[store_unit]
    ing_amount_unit = f"{ing_amount}{ing_unit}"
    store_amount_unit = f"{store_amount}{store_unit}"
    store_name = ing_name

    # Round price to 2dp for table
    store_cost_rounded = f"${store_cost:.2f}"

    # Add ingredient to the lists
    ingredients.append((ing_name, ing_amount, ing_unit))
    store_ingredients.append((store_name, store_amount, store_unit, store_cost))
    ing_name_list.append(ing_name)
    ing_amount_list.append(ing_amount)
    ing_unit_list.append(ing_unit)
    store_amount_list.append(store_amount)
    store_unit_list.append(store_unit)
    prices_list.append(store_cost_rounded)
    calc_prices_list.append(store_cost)

ingredient_frame = pandas.DataFrame(ingredient_dict)
store_price_frame = pandas.DataFrame(store_dict)

# ** Calculate cost per unit of each ingredient in the recipe **
total_cost = 0  # Make total cost counter

for ing_name, ing_amount, ing_unit in ingredients:
    for store_name, store_amount, store_unit, store_cost in store_ingredients:
        if ing_name == store_name:
            price_conv_amount = convert_unit(store_amount, store_unit)
            ing_amount_base = convert_unit(ing_amount, ing_unit)

            # If amount is a whole number, remove decimal place
            if ing_amount == int(ing_amount):
                ing_amount = int(ing_amount)

            # Calculate
            cost_per_unit = store_cost / price_conv_amount
            ing_cost = cost_per_unit * ing_amount_base

            # Add to total cost
            total_cost = total_cost + ing_cost

            # Round to 2dp for table
            ing_cost_rounded = f"${ing_cost:.2f}"

            # Add to table
            ing_cost_list.append(ing_cost_rounded)

# Calculate cost per serving
per_serve = total_cost / recipe_servings

# *** Print area ***

# Print name and servings
print(f"\n**** {recipe_name} ****\n")
print(f"Servings: {recipe_servings}")

# Print all ingredients
print("\n*** Ingredients ***\n")
print(ingredient_frame.to_string(index=False))

# Print store-bought ingredients and their prices
print("\n*** Ingredient Prices ***\n")
print(store_price_frame.to_string(index=False))

# Calculate total cost for store-bought ingredients
total_cost_store = sum(calc_prices_list)
print(f"\n-- Total cost for ingredients from store: ${total_cost_store:.2f} --")

print("\n*** Cost per Ingredient ***\n")
# Make and print cost per ingredient table
recipe_price_frame = pandas.DataFrame(price_dict)
print(recipe_price_frame.to_string(index=False))

# Print final costs
print(f"\n*** Final Costs ***\n")
print(f"-- Total cost for recipe: ${total_cost:.2f} --")
print(f"-- Cost per serving: ${per_serve:.2f} --")
