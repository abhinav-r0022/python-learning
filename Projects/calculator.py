# Simple Calculator
# A basic calculator that performs arithmetic operations on two numbers

# ============================================================
# INPUT - Get numbers and operator from user
# ============================================================

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# ============================================================
# PROCESSING - Perform calculation based on operator
# ============================================================

if operator == "+":
    result = num1 + num2
    print("Result:", result)

elif operator == "-":
    result = num1 - num2
    print("Result:", result)

elif operator == "*":
    result = num1 * num2
    print("Result:", result)

elif operator == "/":
    # Check for division by zero
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error! Division by zero is not allowed.")

else:
    print("Invalid operator!")

# ============================================================
# END OF PROGRAM
# ============================================================
