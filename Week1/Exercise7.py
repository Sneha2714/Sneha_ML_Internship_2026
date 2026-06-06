# Student Report Program

name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")

m1 = float(input("Marks 1: "))
m2 = float(input("Marks 2: "))
m3 = float(input("Marks 3: "))
m4 = float(input("Marks 4: "))
m5 = float(input("Marks 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

print("\nStudent Report")
print("Name :", name)
print("Roll :", roll)
print("Total :", total)
print("Percentage :", percentage)