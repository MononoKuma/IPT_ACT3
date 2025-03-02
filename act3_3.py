# Asking user for their last name, first name, age, contact number, and course
last = input("Enter your last name: ")
first = input("Enter your first name: ")
age = input("Enter age Ex. 20: ")
contact = input("Enter contact number: ")
course = input("Enter course: ")

# Formatting the collected information
student_info = f"Last Name: {last}\nFirst Name: {first}\nAge: {age}\nContact Number: {contact}\nCourse: {course}\n\n"

# Writing to a file in append mode
with open("students.txt", "a") as file:
    file.write(student_info)

# Display confirmation message
print("Student information has been saved to 'students.txt'.")