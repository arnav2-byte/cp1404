"""
CP1404/CP5632 Practical
"""
from project import Project
from datetime import datetime

FILENAME = "projects.txt"
DATE_PATTERN = "%d/%m/%y"

def main():
    print("Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    MENU = (
        "- (L)oad projects\n"
        "- (S)ave projects\n"
        "- (D)isplay projects\n"
        "- (F)ilter projects by date\n"
        "- (A)dd new project\n"
        "- (U)pdate project\n"
        "- (Q)uit"
    )

    while True:
        print(MENU)
        choice = input(">>> ").lower()
        if choice == "L":
            filename = input("name of the file to load from: ")
            projects = load_projects(filename)
            print(f"{len(projects)} projects loaded from {filename}")
        elif choice == "S":
            filename = input("saving the file name to : ")
            save_projects(filename, projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects(projects)
        elif choice == "A":
            add_new_project(projects)
        elif choice == "U":
            update_project(projects)
        elif choice == "Q":
            save_prompt = input(f" Would you like to save it here {FILENAME}? ").lower()
            if save_prompt in ("Y"):
                save_projects(FILENAME, projects)
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Not valid choice.")
