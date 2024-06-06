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


# testing
yes_no_list = ["yes", "no", "y", "n"]
unit_list = ["kilograms", "kg", "grams", "g", "milligrams", "mg", "litres", "l", "millilitres", "ml", "cups", "c",
             "tablespoons", "tbsp", "teaspoons", "tsp"]

for case in range(0, 6):
    yes_no = string_checker("Yes or No? ", yes_no_list)

    if yes_no == "n":
        yes_no_ans = "no"
    elif yes_no == "y":
        yes_no_ans = "yes"
    else:
        yes_no_ans = yes_no

    print(yes_no_ans)

for case in range(0, 5):
    unit = string_checker("Unit? ", unit_list)
    print(unit)
