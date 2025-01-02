import math


def calculator():
    while True:
        print("*Welcome to Python Calculator*")
        print("1: Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Exponentiation")
        print("7. Square Root")
        print("8. Cube")
        print("9. Exit")

        try:
            choice = int(input("Enter your choice (1-9): "))
            if choice == 9:
                print("You chose to exit, Goodbye!")
                break

            if choice in [1, 2, 3, 4, 5, 6]:
                a = float(input("Enter your first number: "))
                b = float(input("Enter your second number: "))

            if choice == 1:
                print(f"Result: {a} + {b} = {a + b}")
            elif choice == 2:
                print(f"Result: {a} - {b} = {a - b}")
            elif choice == 3:
                print(f"Result: {a} * {b} = {a * b}")
            elif choice == 4:
                if b == 0:
                    print("Error: Division by zero is not allowed.")
                elif a == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    print(f"Result: {a} / {b} = {a / b}")
            elif choice == 5:
                print(f"Result: {a} % {b} = {a % b}")
            elif choice == 6:
                print(f"Result: {a} ^ {b} = {a ** b}")
            elif choice == 7:
                a = float(input("Enter a number: "))
                if a < 0:
                    print("Error: Square root of a negative number is not real.")
                else:
                    print(f"Result: √{a} = {math.sqrt(a)}")
            elif choice == 8:
                a = float(input("Enter a number: "))
                print(f"Result: {a}³ = {a ** 3}")
            else:
                print("Invalid choice. Please select a number between 1 and 9.")

        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")

        input("\nPress Enter to return to the main menu...")


calculator()
