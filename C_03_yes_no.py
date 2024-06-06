# checks that answer to a question is either yes or no
def yes_no(question):

    while True:
        response = input(question).lower()

        # If response is yes/no or y/n, continue
        if response == "yes" or response == "y":
            print("You said: Yes")
            return "yes"

        elif response == "no" or response == "n":
            print("You said: No")
            return "no"

        else:
            print("Please enter Yes or No")
            continue


# testing
while True:
    test = yes_no("Yes or No? ")
