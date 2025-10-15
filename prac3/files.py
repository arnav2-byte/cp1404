# Ask the user for their name
name = input("Please enter your name: ")

file = open("name.txt", "w")
file.write(name)
file.close()

print(f"Your name has been written to name.txt.")

# Open the file in read mode and read the name
file = open("name.txt", "r")
name = file.read().strip()

# Close the file
file.close()

print(f"Hi {name}!")

# Open the file using 'with' and read the first two numbers
with open("numbers.txt", "r") as file:
    # Read the first two lines and convert them to integers
    first_number = int(file.readline().strip())
    second_number = int(file.readline().strip())

# Add the two numbers and print the result
result = first_number + second_number
print(result)  # Output should be 59
