"""
Estimated time:
Starting time: 5:00
Finishing time:6:40
Actual recorded time:100 MIN
"""
from datetime import date
class Guitar:  # name of the guitar,year and cost

    def __init__(self, name: str = "", year: int = 0, cost: float = 0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self) -> str:
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self) -> int:
        return date.today().year - self.year

    def is_vintage(self) -> bool:
        return self.get_age() >= 50
