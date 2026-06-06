# Student Result System

name = input("Enter student name: ")
roll = input("Enter roll number: ")

marks = []
total = 0

for i in range(1, 6):
    mark = float(input(f"Enter marks of Subject {i}: "))
    marks.append(mark)
    total += mark

percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n----- Student Result -----")
print("Name :", name)
print("Roll No :", roll)
print("Total Marks :", total)
print("Percentage :", percentage)
print("Grade :", grade)