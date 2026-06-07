name = input("Enter Name: ")
roll = input("Enter Roll No: ")

file = open("student.txt", "w")

file.write("Name: " + name + "\n")
file.write("Roll No: " + roll)

file.close()

print("Data Saved Successfully")