from guitar import Guitar

def main():
    print("Guitars")
    guitars = []

    while True:
        name = input("name: ").strip()
        if name == "":
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")

    print("\n These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_tag = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

if __name__ == "__main__":
    main()
