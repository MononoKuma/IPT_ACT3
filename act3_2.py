# Asking the user for their first name, last name, and age
first = input("Enter your first name: ")
last = input("Enter your last name: ")

# Combining first and last name
full_name = first + " " + last

# Changing the full name to upper and lower case as well as getting the length
upper = full_name.upper()
lower = full_name.lower()
length = len(full_name)

# Displaying the full name, full name in upper case, full name in lower case, and the length of the full name
print("\nFull Name:", full_name)
print("Full Name (Upper Case):", upper)
print("Full Name (Lower Case):", lower)
print("Length of Full Name:", length)