# Check that users have entered a valid answer


def string_checker(question, valid_ans=["yes", "no"]):

    error = f"please enter a valid option from the following list: {valid_ans}"
    while True:
        # get user response and make sure its lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item
            # check if the user response is the same as
            # the first letter of an item in the alphabet
            elif user_response == item[0]:
                return item

        # print out error if user does not enter something 'valid'
        print(error)
        print()

# Main routine goes here


rps_list = ["rock", "paper", "scissors", "xxx"]


want_instructions = string_checker("Do you want to see the instructions?")

print("you chose", want_instructions)

user_choice = string_checker("choose:", rps_list)
print("you chose:", user_choice)