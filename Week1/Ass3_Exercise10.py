class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name :", self.name)
        print("Marks :", self.marks)

try:
    a = int(input("Enter Number 1: "))
    b = int(input("Enter Number 2: "))

    result = a / b

    print("Result =", result)

except ZeroDivisionError:
    print("Division by Zero is not allowed")

student = Student("Sneha", 95)
student.display()