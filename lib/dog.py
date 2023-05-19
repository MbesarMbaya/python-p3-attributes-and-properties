#!/usr/bin/env python3
APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name=None, breed=None):
        self._name = None
        self._breed = None

        if name is not None:
            self.name = name
        if breed is not None:
            self.breed = breed
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 25 characters.")

    @property
    def breed(self):
        return self._breed
    
    @breed.setter
    def breed(self, value):
        if value in APPROVED_BREEDS:
            self._breed = value
        else:
            raise ValueError("Breed must be in the list of approved breeds.")


# Example usage
my_dog = Dog(name="Max", breed="Beagle")

print(my_dog.name)  # Output: Max
print(my_dog.breed)  # Output: Beagle

try:
    my_dog.name = "This is a very long name for a dog."  # Invalid name
except ValueError as e:
    print(str(e))  # Output: Name must be a string between 1 and 25 characters.

try:
    my_dog.breed = "Labrador"  # Invalid breed
except ValueError as e:
    print(str(e))  # Output: Breed must be in the list of approved breeds.
