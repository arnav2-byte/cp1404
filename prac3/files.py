# Ask the user for their name
name = input("Please write your name here : ")

file = open("name.txt", "w")
file.write(name)
file.close()

print(f"Your name should be written to name.txt.")
# Open the file in read mode and read the name
file = open("name.txt", "r")
name = file.read().strip()

# Close the file
file.close()

print(f"Hi {name}!")


with open("numbers.txt", "r") as file:

    first_number = int(file.readline().strip())
    second_number = int(file.readline().strip())

result = first_number + second_number
print(result)  # Output should be 59
