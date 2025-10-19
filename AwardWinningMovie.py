# Author: Armaghan Qadiry
# File: AwardWinningMovie.py
# Description: Subclass of Movie that includes award information.

from Movie import Movie


class AwardWinningMovie(Movie):
    def __init__(self, title, director, year, award_name, award_year, category):
        super().__init__(title, director, year)
        self.__award_name = award_name
        self.__award_year = award_year
        self.__category = category

    def get_award_name(self):
        return self.__award_name

    def get_award_year(self):
        return self.__award_year

    def get_category(self):
        return self.__category

    def set_award_name(self, award_name):
        self.__award_name = award_name

    def set_award_year(self, award_year):
        self.__award_year = award_year

    def set_category(self, category):
        self.__category = category

    def __str__(self):
        return (
            f"{self.get_title()} ({self.get_year()}) - Directed by {self.get_director()}\n"
            f" Award: {self.__award_name} ({self.__award_year}) - {self.__category}"
        )

    def __repr__(self):
        return self.__str__()

    def update(self):
        super().update()
        from validation import get_string
        new_award = get_string(f"Current award: {self.__award_name}. Enter new award or press Enter to keep: ")
        if new_award:
            self.set_award_name(new_award)
        new_award_year = get_string(f"Current award year: {self.__award_year}. Enter new year or press Enter to keep: ")
        if new_award_year.isdigit():
            self.set_award_year(int(new_award_year))
        new_category = get_string(f"Current category: {self.__category}. Enter new category or press Enter to keep: ")
        if new_category:
            self.set_category(new_category)
