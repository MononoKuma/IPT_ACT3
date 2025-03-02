# Asking the user for their first name, last name, and age
first = input("Enter your first name: ")
last = input("Enter your last name: ")
age = input("Enter your age: ")

# Combining the first and last name to create the full name
full = first + " " + last

# Extracting the first four characters of the first name
sliced = first[:4]

# Displaying the full name, sliced name, and a greeting message
print("\nFull Name:", full)
print("Sliced Name:", sliced)
print("Greeting Message: Hello, {}! Welcome. You are {} years old.".format(sliced, age))