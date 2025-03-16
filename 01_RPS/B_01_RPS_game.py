import random


# Check that users have entered a valid answer
def string_checker(question, valid_ans=("yes", "no")):
    """ Checks users enter a valid answer based on a list, default list is yes / no"""
    error = f"please enter a valid option from the following list: {valid_ans}"
    while True:
        # get user response and make sure its lowercase
        response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if response == item:
                return item

            # check if the user response is the same as
            # the first letter of an item in the alphabet
            elif response == item[0]:
                return item

        # print out error if user does not enter something 'valid'
        print(error)
        print()


def instruction():
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
     
     if you want to exit anytime press <xxx>
     
     Have Fun !!
         """)


# Check that users have entered a valid answer

def int_check(question):
    """checks integers to decide rounds (i think)"""
    while True:
        error = "please enter an integer that is 1 or more."

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            if response < 1:
                print(error)

            else:
                return response

        except ValueError:
            print(error)

# compare user / computer choice and returns'
# result (win / lose / tie)
def rps_compare(user, comp):
    """compare user and computer to win / lose / tie"""
    # if the user and the computer choice is the same, it's a tie
    if user == comp:
        result = "tie"


    # three ways to win
    elif user == "paper" and comp == "rock":
        result = "win"
    elif user == "scissors" and comp == "paper":
        result = "win"
    elif user == "rock" and comp == "scissors":
        result = "win"
    # if it's not a win / tie it's a loss
    else:
        result = "lose"

    return result


# Main routine

# initialise game variables
mode = "regular"
rounds_played = 0

rps_list = ["rock", "paper", "scissors", "xxx"]

print("ROCK / PAPER / SCISSORS")
print("The most fabulous game of them all!!")
print()

# ask user if they want to see the instructions and display
# them if requested

want_instructions = string_checker("do you want to see the instructions?")
if want_instructions == "yes":
    instruction()

# checks users enter y / n

# Display the instructions if user wants to see them

num_rounds = int_check("How many rounds would you like to play? push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# game loop starts here
while rounds_played < num_rounds:

    # Rounds Heading
    if mode == "infinite":
        rounds_heading = f"\n🌜🌜🌜 Round {rounds_played + 1} (infinite mode) 🌛🌛🌛"
    else:
        rounds_heading = f"\n🌜🌜🌜 Round {rounds_played + 1} of {num_rounds} 🌛🌛🌛"

    print(rounds_heading)
    print()

    # randomly choose from the rps list (excluding the exit code)
    comp_choice = random.choice(rps_list[:-1])
    print("computer choice", comp_choice)

    user_choice = string_checker("choose: ", rps_list)
    print("you chose", user_choice)

    if user_choice == "xxx":
        break

    result = rps_compare(user_choice, comp_choice)
    print(f"{user_choice} vs {comp_choice}, {result}")

    rounds_played += 1

    # if users are in infinite mode, increase number of rounds
    if mode == "infinite":
        num_rounds += 1

# game loop ends here

# game history / stats
