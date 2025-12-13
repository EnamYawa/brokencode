# Login validation program

def login(username, password):
    correct_username = "admin"
    correct_password = "8285"

    if username == correct_username and password == correct_password:
        print("Login successful")
    else:
        print("Access denied")

user = input("Enter username: ")
pwd = input("Enter password: ")

login(user, pwd)

