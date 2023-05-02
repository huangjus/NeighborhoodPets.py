# Author: Justin Huang
# GitHub username: huangjus
# Date: 5/2/23
# Description: This code defines the NeighborhoodPets class, which maintains a dictionary of pets, where the keys are
# the pet names and the values are dictionaries containing the species and owner of each pet. The class includes methods
# for adding and deleting pets, finding a pet owner, saving and loading data from JSON files, and getting a set of all
# pet species. The DuplicateNameError is raised when trying to add a pet with a name that already exists in the list.


import json


class DuplicateNameError(Exception):
    """Custom exception raised when a pet with the same name already exists."""

    pass


class NeighborhoodPets:
    """A class to represent neighborhood pets and their owners."""
    
    def __init__(self):
        self.__pets = {}

    def add_pet(self, name, species, owner):
        """Add a pet to the neighborhood pets list."""

        if name in self.__pets:
            raise DuplicateNameError("A pet with this name already exists.")
        self.__pets[name] = {"species": species, "owner": owner}

    def delete_pet(self, name):
        """Delete a pet from the neighborhood pets list."""

        if name in self.__pets:
            del self.__pets[name]

    def get_owner(self, name):
        """Get the owner of a pet by pet name."""

        return self.__pets.get(name, {}).get("owner")

    def save_as_json(self, filename):
        """Save the neighborhood pets list to a JSON file."""

        with open(filename, "w") as outfile:
            json.dump(self.__pets, outfile)

    def read_json(self, filename):
        """Load the neighborhood pets list from a JSON file."""

        with open(filename, "r") as infile:
            self.__pets = json.load(infile)

    def get_all_species(self):
        """Get a set of all pet species."""

        return {pet["species"] for pet in self.__pets.values()}
