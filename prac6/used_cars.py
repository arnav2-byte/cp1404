"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac6.car import Car
def main():
    """Demo test code to show how to use car class."""
    my_car = Car(42)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    limo = Car("Limo",137)  # it creates a new line for limo car

    limo.add_fuel(20)
    print("refueling limo car: {limo.fuel}")

    limo.drive(115)

    print(limo)
main()
