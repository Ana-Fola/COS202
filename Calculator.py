while True:
        print("="*35)
        print("  MATHEMATICAL CALCULATOR  ")
        print("="*35)
        print(" [ + ] Addition")
        print(" [ - ] Subtraction")
        print(" [ * ] Multiplication")
        print(" [ / ] Division")
        print(" [ \\ ] Integer Division")
        print(" [ ^ ] Power / Exponent")
        print(" [ % ] Modulo / Remainder")
        print(" [ C ] Clear Screen")
        print(" [ OFF ] Turn Off Calculator")
        print("="*35)
        
        choice = input("Select an operation symbol: ")
        
        if choice == 'OFF':
            print("Turning off... Goodbye!")
            break
        elif choice == 'C':
            print("Clearing screen...")
            continue
            
        if choice in ('+', '-', '*', '/', '\\', '^', '%'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                if choice == '+':
                    print("Result:", num1, "+", num2, "=", num1 + num2)
                elif choice == '-':
                    print("Result:", num1, "-", num2, "=", num1 - num2)
                elif choice == '*':
                    print("Result:", num1, "*", num2, "=", num1 * num2)
                elif choice == '/':
                   if num2 != 0:
                      print("Result:", num1, "/", num2, "=", num1 / num2)
                   else:
                      print("Error: Cannot divide by zero.")
                elif choice == '\\':
                   if num2 != 0:
                      print("Result:", num1, "\\", num2, "=", num1 // num2)
                   else:
                      print(" Error: Cannot divide by zero.")
                elif choice == '^':
                     print("Result:", num1, "^", num2, "=", num1 ** num2)
                elif choice == '%':
                      print("Result:", num1, "%", num2, "=", num1 % num2)
            except ValueError:
                print("Invalid input! Please enter numerical values only.")
        else:
            print("Invalid operation selected. Please try again.")
