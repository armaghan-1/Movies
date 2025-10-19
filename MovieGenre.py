# Author: Armaghan Qadiry
# File: MovieGenre.py
# Description: Category class to group movies.

class MovieGenre:
    def __init__(self, name, description=""):
        self.name = name
        self.description = description
        self.items = []

    def add(self, item):
        if item not in self.items:
            self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)

    def __iter__(self):
        return iter(self.items)

    def __contains__(self, item):
        return item in self.items

    def __add__(self, other):
        new_name = f"{self.name}/{other.name}"
        new_genre = MovieGenre(new_name)
        new_genre.items = self.items + other.items
        return new_genre

    def __str__(self):
        return f"Category: {self.name} ({len(self.items)} items)"
