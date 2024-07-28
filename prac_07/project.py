"""
Estimate: 20 minutes
Actual:   12 minutes
"""

from datetime import datetime


class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        # Ensure start_date is a datetime object
        if isinstance(start_date, str):
            self.start_date = datetime.strptime(start_date, '%d/%m/%Y')
        elif isinstance(start_date, datetime):
            self.start_date = start_date
        else:
            raise TypeError("start_date must be a string or datetime object")

        self.name = name
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def update_completion(self, new_completion):
        self.completion_percentage = new_completion

    def update_priority(self, new_priority):
        self.priority = new_priority

    def __str__(self):
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"
