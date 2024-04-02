def add():
    a = int(input("Enter First Number = "))
    b = int(input("Enter Second Number = "))
    return a+b
def sub():
    a = int(input("Enter First Number = "))
    b = int(input("Enter Second Number = "))
    return a-b
def mul():
    a = int(input("Enter First Number = "))
    b = int(input("Enter Second Number = "))
    return a*b
def div():
    a = int(input("Enter First Number = "))
    b = int(input("Enter Second Number = "))
    return a/b


print("----Basic Calculator----")
while True:
    print("Please select one of the following options")
    print("------------------------------------------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication ")
    print("4. Division")
    print("5. Quit")
    choice = input("\nEnter your choice = ")
    if choice == "1":
        print("Answer = ",add())
    elif choice == "2":
        print("Answer = ",sub())
    elif choice == "3":
        print("Answer = ",mul())
    elif choice == "4":
        print("Answer = ",div())
    elif choice == "5":
        exit()
    else:
        print("INVALID INPUT -- Try Again")