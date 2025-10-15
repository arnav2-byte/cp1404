"""
CP1404/CP5632 - Practical
Program for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":

    def celsius_to_fahreneheit(celsius):
        fahrenheit = (celsius * 9 / 5) + 32
        return fahrenheit


    def fahrenheit_to_celsius(fahrenheit):
        celsius = (fahrenheit - 32) / 5
        return celsius

    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius_to_fahreneheit(celsius)
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit : "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"Result: {celsius:.2f} C")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")

