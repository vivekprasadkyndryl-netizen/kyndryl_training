a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

print("The result is:", divide(a, b))