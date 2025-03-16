# Check that users have entered a valid answer


def int_check(question):
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


# Main routine

# initialise game variables
mode = "regular"
rounds_played = 0

print("ROCK / PAPER / SCISSORS")
print("The most fabulous game of them all!!")
print()

# instructions

# ask user for number of rounds / infinite mode
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

    user_choice = input("choose: ")

    if user_choice == "xxx":
        break

    rounds_played += 1

    # if users are in infinite mode, increase number of rounds
    if mode == "infinite":
        num_rounds += 1

# game loop ends here

# game history / stats
