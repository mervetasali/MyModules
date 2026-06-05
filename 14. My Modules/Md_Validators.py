# Get yes or no as answer to quit or continue the proccess from the user 
def get_yes_no():
    userAns = input("Do you want to quit? (y/n)").strip().lower() #removes if there is a space after the answer
    answer = "waiting"
    if userAns == "y":
        answer = "break"
    elif userAns == "n":
        answer = "continue"
    else:
        print("Please enter a valid option!")
    
    return answer

# Get a integer value from the user
def get_int(message):

    while True:

        try:
            return int(input(message))
        except ValueError:
            print("Please, enter only a valid integer!")

# Get a float value from the user
def get_float(message):

    while True:

        try:
            return float(input(message))
        except ValueError:
            print("Please, enter only a valid float value!")