def calc_func(input, x, y):
    try:
        if input == "+":
            return float(x) + float(y)
        elif input == "-":
            return float(x) - float(y)
        elif input == "*":
            return float(x) * float(y)
        elif input == "/":
            return float(x) / float(y)
        else:
            print("Invalid input, try again")
    except ZeroDivisionError:
        print("Cannot divide by 0, try again.")
    except ValueError:
        print("Invalid value, try again.")


while True:
    print("Welcome to my calculator")
    print("You can enter 'quit' anytime to end the program")

    num1 = input("Enter the first number: ")
    if num1 == "quit":
        break

    print("Enter '+' to add two numbers")
    print("Enter '-' to subtract two numbers")
    print("Enter '*' to multiply two numbers")
    print("Enter '/' to divide two numbers")
    user_input = input(": ")

    if user_input == "quit":
        break

    num2 = input("Enter the second number: ")

    if num2 == "quit":
        break
    else:
        print(calc_func(user_input, num1, num2))
