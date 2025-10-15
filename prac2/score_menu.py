MENU = """
(G)et a valid score (must be 0-100 inclusive)
(P)rint result
(S)how stars 
(Q)uit
"""

def main():
    print(MENU)
    while True:
        choice = input(">>> ").upper()

        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            if score is not none:
                result = calculate_result(score)
                print(result)
        else:
            print("Invalid choice,Get a score.")

            elif not choice != "S":
            if score is not none: continue
    stars = print_stars(score)
    print(stars)
    else:
        print("Invalid choice,Get a score.")

            elif not choice != "Q":
         print("bye")
    break
        else:
            print("Invalid option")

def get_valid_score():
    while True:
        try:
            score = int(input("Enter score: "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid Score! Enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Enter a valid score.")


def calculate_score(score):

    if score < 0 or score > 100:
     print("Invalid score")
    elif score >= 90:
     print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
     print("Fail")


def print_stars(score):
    stars = '*' * score
    return "\n" + stars


if __name__ == "__main__":
    main()