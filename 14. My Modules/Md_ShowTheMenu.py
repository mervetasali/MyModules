#Shows the menu that is defined by the user

def show_menu(title, options):

    print(f" ======== {str(title).upper().strip()} ======== ")

    for index, value in enumerate(options, start=1):
        print(f"{index}. {value}")

    print("-------------------------------------------")

   