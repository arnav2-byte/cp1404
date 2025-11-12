from datetime import datetime
class Project:    #Represent a project with its details

    def __init__(self, name, initializing_date, priority, budget_estimate, completed_percentage):
        self.name = name
        self.initializing_date = initializing_date  # datetime
        self.priority = priority
        self.budget_estimate = budget_estimate
        self.completed_percentage = completed_percentage

    def __str__(self):
        return (f"{self.name}, initializing: {self.initializing_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.budget_estimate:,.2f}, "
                f"completion: {self.completed_percentage}%")

    def __lt__(self, other):    #(lower = higher priority).
        return self.priority < other.priority

    def is_complete(self):
        return self.completed_percentage == 100

    def update(self, new_percentage=None, new_priority=None):
        if new_percentage is not None:
            self.completed_percentage = new_percentage
        if new_priority is not None:
            self.priority = new_priority