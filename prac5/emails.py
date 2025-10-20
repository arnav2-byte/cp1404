"""
CP1404/CP5632 Practical
estimate: 30 minutes
actual : 23 minutes
"""
def get_name_from_email(email):
    username_part = email.split('@')[0]

    username_part = username_part.replace('.', ' ').replace('_', ' ')
    return username_part.title()

def collecting_emails():
    email_to_username = {}

    while True:
        # Ask the user for an email
        email = input("what's the Email: ")

        if email == "":
            break

        name = get_name_from_email(email)

        response = input(f"Is your name {name}? (Y/n) ").strip().lower()

        if response == 'n' or response == 'no':
            name = input("Name: ")

        email_to_username[email] = name

    return email_to_username


def main():
    emails_dict = collecting_emails()

    for email, name in emails_dict.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    main()
