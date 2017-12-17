"""Get list of Movie objects from The Movie Database (TMDb)."""

import requests
import apikey
import media
from operator import itemgetter


def get_movies():
    """Retrieve movie info from TMDB API.
    Ask user for movie title keyword(s) search. Make call to search API
    to get list of movies.  Make another call, to video API, to get
    YouTube key for relevant movies.
    :returns list: List of movie objects.
    """

    # Given a query, get movies from TMDB
    key = apikey.apikey
    query = input(
        "Enter movie title keywords (eg, star wars, batman, etc)? "
    )
    url = "https://api.themoviedb.org/3/search/movie?api_key={}&language=en-US" \
          "&query={}&page=1&include_adult=false".format(key, query)
    r = requests.get(url)
    data = r.json()

    # Add movies to the list if they have a poster
    movies = []
    [movies.append(dict(title=result["original_title"],
                        id=result["id"],
                        poster="https://image.tmdb.org/t/p/original{}".format(
                            result["poster_path"]),
                        popularity=result["popularity"]))
     for result in data["results"] if result["poster_path"]]

    # Longer list of movies that results from common movie title keywords,
    # shortened to 20 most popular
    movies = sorted(movies, key=itemgetter("popularity"), reverse=True)[:20]

    # For each movie, get and add youtube url, create (new) movie list of
    # Movie objects for use in fresh_tomatoes.py
    films = []
    for movie in movies:
        vurl = "http://api.themoviedb.org/3/movie/{}?api_key={}&append_to_" \
               "response=videos".format(movie["id"], key)
        vr = requests.get(vurl)
        vdata = vr.json()

        # for simplicity, use first movie trailer option available per movie
        if vdata["videos"]["results"]:
            youtube_url = "https://www.youtube.com/watch?v={}".format(
                vdata["videos"]["results"][0]["key"])
        else:
            youtube_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

        movie["youtube_url"] = youtube_url

        films.append(media.Movie(movie["title"],
                                 movie["poster"],
                                 movie["youtube_url"],))

        # Print each movie found
        print("Found: {}".format(movie["title"]))

    return films
