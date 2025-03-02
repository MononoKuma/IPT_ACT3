# Define the file name that contains the student information
filename = "students.txt"

try:
    # Code to try to open the file in read mode
    with open(filename, "r") as file:
        print("Student Information:\n")
        
        # if successful, read and print the content of the file
        print(file.read())  
except FileNotFoundError:
    # A error handler to print a message if the file is not found
    print(f"Error: '{filename}' not found. Please add student information first.")