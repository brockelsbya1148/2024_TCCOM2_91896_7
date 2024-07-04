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


# Converts units into g and ml
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
instruction_yn = string_checker("Do you want to see the instructions ", yes_no.keys())
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

# List to store ingredients
ingredients = []
store_ingredients = []

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
    if store_unit == "none":
        store_amount = num_check(f"How many? ", "Please enter a number more than 0 and less than 100(no fractions)",
                                 float)
    else:
        store_amount = num_check(f"How many {store_unit}? ", "Please enter a number more than 0 and less than 100 "
                                                             "(no fractions)", float)
    store_cost = num_check("How much does it cost? $", "Please enter a price", float)

    # Remove decimals on whole numbers
    if store_amount == int(store_amount):
        store_amount = int(store_amount)

    # Unit conversion
    ing_unit = unit_dict[ing_unit]
    store_unit = unit_dict[store_unit]

    # Change name of ing_name, so we can use it when calculating the recipe cost
    store_name = ing_name

    # Add ingredient to the list
    ingredients.append((ing_name, ing_amount, ing_unit))
    store_ingredients.append((store_name, store_amount, store_unit, store_cost))


# *** Print area ***

# Print name and servings
print(f"\n**** {recipe_name} ****\n")
print(f"Servings: {recipe_servings}")


# Print all ingredients
print("\n*** Ingredients ***\n")

for ing_name, ing_amount, ing_unit in ingredients:
    # Remove decimal from whole numbers
    if ing_amount == int(ing_amount):
        ing_amount = int(ing_amount)

    # Print
    print(f"{ing_name}: {ing_amount}{ing_unit}")

# Print store-bought ingredients and their prices
print("\n*** Ingredient Prices ***\n")
for store_name, store_amount, store_unit, store_cost in store_ingredients:
    print(f"{store_name}: ${store_cost:.2f} for {store_amount}{store_unit}")

# Calculate total cost for store-bought ingredients
total_cost_store = sum(store_cost for _, _, _, store_cost in store_ingredients)
print(f"\n-- Total cost for ingredients from store: ${total_cost_store:.2f} --")

# ** Calculate cost per unit of each ingredient in the recipe **

total_cost = 0  # Make total cost counter

print("\n*** Cost per Ingredient ***\n")
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

            print(f"{ing_name}: {ing_amount}{ing_unit} - Cost: ${ing_cost:.2f}")

            # Add to total cost
            total_cost += ing_cost

# Calculate cost per serving
per_serve = total_cost / recipe_servings

# Print final costs
print(f"\n-- Total cost for recipe: ${total_cost:.2f} --")
print(f"-- Cost per serving: ${per_serve:.2f} --")
