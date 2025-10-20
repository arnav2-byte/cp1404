"""
CP1404/CP5632 Practical
"""

def main():
    numbers = []

    for i in range(5):
        number = int(input("Enter the Number: "))
        numbers.append(number)

    # Output
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers):.1f}")


main()

#Ask the user for their username. If the username is in the above list of authorised users, print "Access granted", otherwise print "Access denied".
def main():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']

    username = input("Enter the username: ")

    # Check for the username if in the list of authorised users
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


main()