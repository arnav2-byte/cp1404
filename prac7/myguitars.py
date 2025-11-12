"""
CP1404/CP5632 Practical
"""

from guitar import Guitar


def main():  # this Load the  guitars and display them
    guitars = load_guitars()
    print(f"{len(guitars)} All the guitars are loaded from guitars.csv\n")

    display_guitars(guitars, "Here, these are my guitars:")

    guitars = add_new_guitars(guitars)

    guitars.sort()

    display_all_guitars(guitars, "\nSorted guitars:")

    save_guitars(guitars)
    print("\nGuitars are saved to guitars.csv.")


def load_guitars():
    guitars = []
    try:
        with open("guitars.csv", "r") as in_file:
            for line in in_file:
                parts = line.strip().split(",")
                if len(parts) != 3:
                    continue
                name, year, cost = parts[0], int(parts[1]), float(parts[2])
                guitars.append(Guitar(name, year, cost))
    except FileNotFoundError:
        print("File guitars.csv not found, start again")
    return guitars


def display_guitars(guitars, starter="Guitars:"):
    print(starter)
    for i, guitar in enumerate(guitars, 1):
        vintage_tag = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), "
              f"worth ${guitar.cost:10,.2f}{vintage_tag}")


def add_new_guitars(guitars):
    print("\nEnter new guitars (empty space to stop):")
    while True:
        name = input("Name: ").strip()
        if not name:
            break
        try:
            cost = float(input("Cost: $"))
            year = int(input("Year: "))
        except ValueError:
            print(" Input error , please enter valid number for cost and year ")
            continue

        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.\n")
    return guitars


def save_guitars(guitars):  # Save the guitars to the CSV file
    with open("guitars.csv", "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


if __name__ == "__main__":
    main()
