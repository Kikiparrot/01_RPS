print("hello")


# function start
def yes_no(question):
    """Checks user response to a question is yes/no (y/n), returns 'yes' or 'no'"""
    while True:
        response = input(question).lower()

        # check the user says yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please answer yes / no")


def instructions():
    """prints instructions"""

    print("""
*** Instructions ***

Choose rock, paper, or scissors and try to beat the computer!!
    """)


# Main routine

want_instructions = yes_no("do you want to see the instructions?")
print(f"you chose {want_instructions}")
# Display the instructions if user wants to see them
if want_instructions == "yes":
    instructions()

    print()
print("program continues")
