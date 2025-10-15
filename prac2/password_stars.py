def main():
    password = get_password()
    asterisks = show_stars(password)
    print(asterisks)

def show_stars(password):
    return '*' * len(password)

def get_password():
    password = input('please Enter password: ')
    return password

if __name__ == '__main__':
    main()