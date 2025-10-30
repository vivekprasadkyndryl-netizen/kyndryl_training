num = int(input("Enter a number to find its square root: "))
def sqrt(num):
    if num < 0:
        return "Error: Cannot compute square root of a negative number."
    return num ** 0.5   
print("The square root is:", sqrt(num))
