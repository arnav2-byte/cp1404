from datetime import date
class Guitar:  # name of the guitar,year and cost

    def __init__(self, name: str = "", year: int = 0, cost: float = 0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self) -> str:
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        return self.year < other.year

    def get_age(self) -> int:
        return date.today().year - self.year

    def is_vintage(self) -> bool:
        return self.get_age() >= 50
