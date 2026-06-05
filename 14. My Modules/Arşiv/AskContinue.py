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