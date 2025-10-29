"""
CP1404/CP5632 Practical
"""
def read_wimbledon_data(filename):

    wimbledon_data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)
        for line in in_file:
            parts = line.strip().split(',')
            wimbledon_data.append(parts)
    return wimbledon_data


def compute_champions(data):
    champions_count = {}
    for row in data:
        champion = row[2]
        if champion in champions_count:
            champions_count[champion] += 1
        else:
            champions_count[champion] = 1
    return champions_count


def list_countries(data):
    countries = set()
    for row in data:
        country = row[1]
        countries.add(country)
    return sorted(countries)


def main():
    filename = "wimbledon.csv"
    wimbledon_data = read_wimbledon_data(filename)

    champions = compute_champions(wimbledon_data)

    countries = list_countries(wimbledon_data)

    print("champions of wimbledon:")
    for champion, wins in champions.items():
        print(f"{champion} {wins}")

    print(f"\n Therefore, here's the list of the 12 countries which took over the wimbledon championship {(countries)} :")
    print(", ".join(countries))


if __name__ == "__main__":
    main()