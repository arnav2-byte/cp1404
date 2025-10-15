# write a program which prompts the user for 5 numbers and stores each of this number in a list
"""cp1404- practical
"""

def main():
    numbers = []

    for i in range (5): #5 number as input from the users
            number = int(input(" enter number:"))
            numbers.append(number)

print(f" the starting number is{numbers[0]} ")
print(f" the ending number is {numbers[-1]}")
print(f" the smallest number is {min(numbers)}")
print(f" the largest number is {max(numbers)} ")
print(f" the average of numbers is {sum(numbers)/len(numbers)}:.2f ")

# asking for username
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("please Enter the  username: ")
if username in usernames:
    print("access granted")
else:
    print("access denied")

main()
