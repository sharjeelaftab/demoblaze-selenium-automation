try:
    num1 = int(input("Enter number: "))
    num2 = int(input("Enter divisor: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Please enter valid numbers.")
