# Author: Armaghan Qadiry
# File: ConsoleUI.py
# Description: Text-based interface for Movie Manager.

from validation import get_string, get_valid_year
from Movie import Movie
from AwardWinningMovie import AwardWinningMovie
from MovieGenre import MovieGenre


class ConsoleUI:
    all_items = MovieGenre("All Movies")
    all_categories = []

    @classmethod
    def print_menu(cls):
        print("\nMenu:")
        print("1. Exit")
        print("2. Create Movie or Award-Winning Movie")
        print("3. List All Movies")
        print("4. Show All Categories")
        print("5. Create New Category")
        print("6. Delete Category")
        print("7. View Items in Category")
        print("8. Add Item to Category")
        print("9. Remove Item from Category")
        print("10. Update Item")
        print("11. Merge Categories")

    @classmethod
    def run(cls):
        print("Welcome to the Movie Manager!")
        while True:
            cls.print_menu()
            choice = get_string("Enter your choice: ")
            if choice == "1":
                print("Goodbye!")
                break
            elif choice == "2":
                kind = get_string("Type '1' for Movie or '2' for Award-Winning Movie: ")
                title = get_string("Title: ")
                director = get_string("Director: ")
                year = get_valid_year("Release Year: ")
                if kind == "1":
                    movie = Movie.add_movie(title, director, year)
                elif kind == "2":
                    award_name = get_string("Award Name: ")
                    award_year = get_valid_year("Award Year: ")
                    category = get_string("Award Category: ")
                    movie = AwardWinningMovie(title, director, year, award_name, award_year, category)
                    Movie._Movie__map[movie.get_key()] = movie
                else:
                    print("Invalid type.")
                    continue
                if movie:
                    cls.all_items.add(movie)
                    print("Movie added to All Movies.")
            elif choice == "3":
                Movie.list_movies()
            elif choice == "4":
                for cat in cls.all_categories:
                    print(cat)
            elif choice == "5":
                name = get_string("Category name: ")
                desc = get_string("Description: ")
                cls.all_categories.append(MovieGenre(name, desc))
                print("Category created.")
            elif choice == "6":
                name = get_string("Category to delete: ")
                cls.all_categories = [c for c in cls.all_categories if c.name != name]
                print("Category deleted.")
            elif choice == "7":
                name = get_string("Category name: ")
                for cat in cls.all_categories:
                    if cat.name == name:
                        for item in cat:
                            print(item)
            elif choice == "8":
                title = get_string("Item title: ")
                year = get_string("Item year: ")
                key = f"{title}_{year}"
