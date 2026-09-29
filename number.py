def showing_x():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        #the code it has possible to make an error
        try:
            x = int (input("What's x? "))
        #the process when an error is happened
        except ValueError:
            pass
        #the code it doesn't have possible to make an error
        else:
            break
    return x

showing_x()
