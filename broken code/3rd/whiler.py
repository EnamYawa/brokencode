attempts = 3

while attempts >= 0:
    password = input("Enter password: ")
    if password == "admin":
        print("Access granted")
        break
    attempts = attempts - 1
else:
    print("Account locked")

