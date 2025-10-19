# Author: Armaghan Qadiry
# File: Movie.py
# Description: Base class for storing movie information.

class Movie:
    __map = {}

    def __init__(self, title, director, year):
        self.__title = title
        self.__director = director
        self.__year = year

    def get_key(self):
        return f"{self.__title}_{self.__year}"

    def get_title(self):
        return self.__title

    def get_director(self):
        return self.__director

    def get_year(self):
        return self.__year

    def set_title(self, title):
        self.__title = title

    def set_director(self, director):
        self.__director = director

    def set_year(self, year):
        self.__year = year

    def __str__(self):
        return f"{self.__title} ({self.__year}) - Directed by {self.__director}"

    def __repr__(self):
        return self.__str__()

    def update(self):
        from validation import get_string
        new_title = get_string(f"Current title: {self.__title}. Enter new title or press Enter to keep: ")
        if new_title:
            self.set_title(new_title)
        new_director = get_string(f"Current director: {self.__director}. Enter new director or press Enter to keep: ")
        if new_director:
            self.set_director(new_director)
        new_year = get_string(f"Current year: {self.__year}. Enter new year or press Enter to keep: ")
        if new_year.isdigit():
            self.set_year(int(new_year))

    @classmethod
    def add_movie(cls, title, director, year):
        key = f"{title}_{year}"
        if key in cls.__map:
            print(f"Movie '{key}' already exists.")
            return None
        movie = Movie(title, director, year)
        cls.__map[key] = movie
        return movie

    @classmethod
    def get_movie(cls, key):
        return cls.__map.get(key)

    @classmethod
    def list_movies(cls):
        if not cls.__map:
            print("No movies stored.")
        else:
            for movie in cls.__map.values():
                print(movie)
