# Asking user for their last name, first name, age, contact number, and course
last = input("Enter your last name Ex. Aries: ")
first = input("Enter your first name Ex. Ong: ")
age = input("Enter age Ex. 20: ")
contact = input("Enter contact number Ex 0123 456 7890: ")
course = input("Enter course Ex. BSIT-BA: ")

# Formatting the collected information
student_info = f"Last Name: {last}\nFirst Name: {first}\nAge: {age}\nContact Number: {contact}\nCourse: {course}\n\n"

# Writing to a file in append mode
with open("students.txt", "a") as file:
    file.write(student_info)

# Display confirmation message
print("Student information has been saved to 'students.txt'.")