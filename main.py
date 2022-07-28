attempts = [0, 0]

while (True):
    username = input("Enter username: ")
    if (username == "nodeABC"):
        attempts[0] += 1
        print(attempts[0], "ssh log-in attempts were made at nodeABC")  # Output user input
    elif (username == "nodeXYZ"):
        attempts[1] += 1
        print(attempts[1], "ssh log-in attempts were made at nodeXYZ")  # Output user input
    elif (username == "admin"):
        print("ABC have", attempts[0], "attempt")
        print("XYZ have", attempts[1], "attempt")
    else:
        print("no valid user")