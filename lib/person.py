#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    # ...
]

class Person:
    def __init__(self, name: str, job: str):
        self._name = name
        self._job = job

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string between 1 and 25 characters.")

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value in APPROVED_JOBS:
            self._job = value
        else:
            raise ValueError("Job must be in list of approved jobs.")

# Example usage
person = Person(name="Guido", job="Sales")

print(person.name)  # Output: Guido
print(person.job)  # Output: Sales

try:
    person.name = "This is a very long name for a person."  # Invalid name
except ValueError as e:
    print(str(e))  # Output: Name must be a non-empty string between 1 and 25 characters.

try:
    person.job = "Software Developer"  # Invalid job
except ValueError as e:
    print(str(e))  # Output: Job must be in list of approved jobs.
