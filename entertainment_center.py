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
    cmd = input("Do you want to see [m]y favorites, or [s]earch for yours? ")

    if cmd == "m":
        fresh_tomatoes.open_movies_page(my_favorites.movies)

    elif cmd == "s":
        query = tmdb.get_movies()
        fresh_tomatoes.open_movies_page(query)

    else:
        print("Usage: 'm' or 's'.")


if __name__ == '__main__':
    main()
