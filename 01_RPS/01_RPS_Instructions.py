# Check that users have entered a valid answer

# Main routine
print()
print("ROCK / PAPER / SCISSORS")
print("The most fabulous game of them all!!")
print()
def string_checker(question, valid_ans=("yes", "no")):

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


def instructions():
    """prints instructions"""

    print("""
*** Instructions ***

To begin, choose the number of rounds
 (or you can play infinite mode.)
 
 Then play against the computer
 (you need to play rock (r) paper (p) or scissors (s)
 
 paper beats rock
 rock beats scissors
 scissors beat paper
 
 
 Have Fun !!
     """)


# Main routine

want_instructions = string_checker("do you want to see the instructions?")
# Display the instructions if user wants to see them
if want_instructions == "yes":
    instructions()

    print()
print("program blows up and explodes")
