"""
CP1404/CP5632 Practical
colour names with hex codes
"""
COLOUR_NAME_TO_HEX = {
    "alice blue": "#f0f8ff",
    "absolute zero":"#0048ba",
    "acid green": "#b0bf1a",
    "amber": "#ffbf00",
    "aqua": "#00ffff",
    "ash grey": "#b2bebf",
    "army green": "#4b5320",
    "baby blue": "#89cff0",
    "black": "#000000",
    "black olive": "#3b3c36"
}


def main():
    # Display all colors
    for colour, hex_code in COLOUR_NAME_TO_HEX.items():
        print(f"{colour.title():<15} is {hex_code}")

    while True:
        colour_name = input("Enter colour name: ").strip().lower()  # Convert input to lowercase
        if colour_name == "":
            break

        if colour_name in COLOUR_NAME_TO_HEX:
            print(f"The code for {colour_name.title()} is {COLOUR_NAME_TO_HEX[colour_name]}")
        else:
            print("Invalid colour name")


if __name__ == "__main__":
    main()