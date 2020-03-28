import os

# Print menu 
def print_menu():
    print("""
        \t\t\tTaskel: Making tasks simple
        \t\t\t---------------------------
        1. Date
        2. Calander
        3. Create User
        4. Exit
        """)


# Method to run commands locally
def run_local(choice):
    if choice == '1':
        os.system("date")
    elif choice == '2':
        os.system("cal")
    elif choice == '3':
        username = input("Enter the username: ")
        os.system("useradd " + username)
    elif choice == '4':
        exit()
    else:
        print("Option not supported!")


if __name__ == "__main__":
    conn = input("""\t\t\tTaskel: Making tasks simple
    \t\t\t---------------------------
    Enter the host IP (use 'localhost' for local terminal): """)
    while True:
        # os.system("cls") # toggle comment for Windows
        os.system("clear") # toggle comment for Linux
        print_menu()
        if conn == "localhost":
            print("Running on localhost...")
            choice = input("Choose an option: ")
            run_local(choice)
            input("Press enter to continue...")
        else:
            print("Remote execution is comming soon!")
        
