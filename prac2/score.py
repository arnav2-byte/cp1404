"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random

def main():
    score = float(input("Enter score: "))
    print(calculate_score(score))

    random_score = random.randint(0, 100)
    print(f"random_score):{random_score} RESULT:{calculate_score(random_score)}")

def calculate_score(score):

    if score < 0 or score > 100:
     print("Invalid score")
    elif score >= 90:
     print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
     print("Fail")
if __name__ == '__main__':
    main()