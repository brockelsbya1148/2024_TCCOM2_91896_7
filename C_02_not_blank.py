# Checks that input is not blank
def not_blank(question):

    while True:
        response = input(question)

        # If response is blank, output error
        if response == "":
            print("Cannot be blank\n")
        else:
            return response


# Testing
blank_test = not_blank("Enter some text: ")
print(blank_test)
