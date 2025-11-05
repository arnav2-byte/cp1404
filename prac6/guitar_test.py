from guitar import Guitar
from datetime import date

current_year = date.today().year
def main():
    Guitar_l5= Guitar("Gibson L-5 CES", 1922, 16035.40)

    expected_l5_age = current_year - 1922

    print(f"{Guitar_l5.name} get_age() - Expected {expected_l5_age}. Got {Guitar_l5.get_age()}")
    print(f"{Guitar_l5.name} is_vintage() - Expected {expected_l5_age >= 50}. Got {Guitar_l5.is_vintage()}")

if __name__ == "__main__":
    main()
