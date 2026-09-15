import sys


def register():
    global saved_username,saved_password

    username=input("Enter Username")
    password=input("Password")
    cnf_pass=input("Confirm password")
    if password==cnf_pass:
        saved_username=username
        saved_password=password
        print("Account created successfully")
    else:
        print("Passwords do not match")

def login():
    username=input("Enter Username")
    password=input("Password")
    if username==saved_username and password==saved_password:
        print("Login successful!")
    else:
        print("Invalid username or password.")


while True:
    print("\n========================")
    print("      LOGIN SYSTEM")
    print("========================")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice=input("choose an option")

    match choice:
        case "1":
            register()
        case "2":
            login()
        case "3":
            print("Goodbye!")
            sys.exit()
        case _:
            print("Invalid choice.")
            


    
