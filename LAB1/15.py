#Write a Python program to create a person class. Include attributes like name, country and date of
#birth. Implement a method to determine the person's age.
from datetime import datetime

class Person:
    """
    A class to represent a person.
    """

    def __init__(self, name, country, date_of_birth):
       
        self.name = name
        self.country = country
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")

    def calculate_age(self):
       
        today = datetime.today()
        age = today.year - self.date_of_birth.year
        # Adjust if the birthday hasn't occurred this year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age


person = Person("Jeewan", "Nepal", "2002-06-15")
print(f"Name: {person.name}")
print(f"Country: {person.country}")
print(f"Date of Birth: {person.date_of_birth.date()}")
print(f"Age: {person.calculate_age()} years")
