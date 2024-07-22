import pandas

# Hard code values into dictionaries
ingredient_dict = {
    "Ingredient": ["Flour", "Eggs", "Sugar"],
    "Amount": [300, 12, 50],
    "Unit": ["g", "", "g"]
}

store_price_dict = {
    "Ingredient": ["Flour", "Eggs", "Sugar"],
    "Amount": [2, 12, 1],
    "Unit": ["kg", "", "kg"],
    "Price": [1.53, 7.5, 2.99]
}

price_dict = {
    "Ingredient": ["Flour", "Eggs", "Sugar"],
    "Price": [1, 1, 1]
}

ingredient_frame = pandas.DataFrame(ingredient_dict)
store_price_frame = pandas.DataFrame(store_price_dict)
price_frame = pandas.DataFrame(price_dict)


# Display the formatted DataFrames without setting the index
print("*** Ingredients ***\n")
print(ingredient_frame.to_string(index=False), "\n")
print("*** Store Price ***\n")
print(store_price_frame.to_string(index=False), "\n")
print("*** Price ***\n")
print(price_frame.to_string(index=False))
