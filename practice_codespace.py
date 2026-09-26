

def main():
    name = input("What's your name ->").strip().title()
    hello(name)
    return

def hello(to = "world"):
    print(f"hello" , to)
    return

main()

