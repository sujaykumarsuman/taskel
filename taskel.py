import os


# Print menu
def print_menu():
    print("""
        \t\t\tTaskel: Making tasks simple
        \t\t\t---------------------------
        1. Date
        2. Calender
        3. Create User
        4. Exit
        """)


# Validating entered IP address
def validate_ip(ip):
    bytes_sec = ip.split(".")
    if len(bytes_sec) < 4:
        return False
    for byte in bytes_sec:
        if byte < 0 or byte > 255:
            return False
    return True


# Method to run commands
def run(opt):
    if opt == '1':
        os.system("date")
    elif opt == '2':
        os.system("cal")
    elif opt == '3':
        username = input("Enter the username: ")
        os.system("useradd " + username)
    elif opt == '4':
        exit()
    else:
        print("Option not supported!")


# authenticate remote host
def authenticate(ip):
    if ip in available_remote:
        pass
    print("It seems you have not met before! Please authenticate:\n")
    os.system("ssh-keygen")
    os.system("ssh-copy-id root@" + ip)
    available_remote.append(ip)
    os.system("ssh " + ip)
    os.system("clear")


# Available connection database
available_remote = []

if __name__ == "__main__":
    conn = input("""\t\t\tTaskel: Making tasks simple
    \t\t\t---------------------------
    Enter the host IP (use 'localhost' for local terminal): """)

    while validate_ip(conn) is not True:
        conn = input("Please enter valid IP in proper format: ")
    if conn != "localhost":
        authenticate(conn)
        while True:
            os.system("clear")  # toggle comment for Linux
            print_menu()
            print("Running on IP: " + conn + " ...")
            choice = input("Choose an option: ")
            run(choice)  # remote execution
            input("Press enter to continue...")
    else:
        while True:
            print("Running on localhost...")
            choice = input("Choose an option: ")
            run(choice)
            input("Press enter to continue...")
