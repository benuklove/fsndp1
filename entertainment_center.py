"""This file is the main entry point.  It runs main() which calls other
functions and thereby other modules.
"""

import fresh_tomatoes
import my_favorites
import tmdb


def main():
    print_header()
    launch()


def print_header():
    print("---------------------------------------------------------------")
    print("                         Movie Time!")
    print("---------------------------------------------------------------")


def launch():
    """Get input from user. Control flow for the user choice made.
    User selects 'm' or 's'.  'm' shows my favorites, 's' allows a search
    for the user's favorite movies.
    :return: None
    """
    cmd = input("Do you want to see [m]y favorites, or [s]earch for yours? ")

    if cmd.lower() == "m":
        fresh_tomatoes.open_movies_page(my_favorites.movies)

    elif cmd.lower() == "s":
        query = tmdb.get_movies()
        fresh_tomatoes.open_movies_page(query)

    else:
        print("Usage: 'm' or 's'.")


if __name__ == '__main__':
    main()
