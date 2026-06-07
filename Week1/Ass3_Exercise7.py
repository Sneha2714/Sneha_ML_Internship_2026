def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

a = float(input("Enter First Number: "))
b = float(input("Enter Second Number: "))

print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = int(input("Enter Choice: "))

if choice == 1:
    print("Result =", add(a, b))

elif choice == 2:
    print("Result =", subtract(a, b))

elif choice == 3:
    print("Result =", multiply(a, b))

elif choice == 4:
    print("Result =", divide(a, b))

else:
    print("Invalid Choice")