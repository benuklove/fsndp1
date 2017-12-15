import requests
import apikey
import media
from operator import itemgetter

import pprint
pp = pprint.PrettyPrinter(indent=4)


def get_movies():
    key = apikey.apikey
    query = input(
        "Enter movie title keywords (eg, star wars, batman, etc)? "
    )

    # Given a query, get movies from TMDB
    url = "https://api.themoviedb.org/3/search/movie?api_key={}&language=en-US&query=" \
          "{}&page=1&include_adult=false".format(key, query)
    r = requests.get(url)
    data = r.json()

    movies = []

    # Add movies to the list
    [movies.append(dict(title=result["original_title"],
                        id=result["id"],
                        poster="https://image.tmdb.org/t/p/original{}".format(result["poster_path"]),
                        popularity=result["popularity"])) for result in data["results"]]

    # Longer list of movies that results from common movie title keywords, shortened to 20 most popular
    movies = sorted(movies, key=itemgetter("popularity"), reverse=True)[:18]

    # For each dict, get and add youtube url, create movie list
    films = []
    for movie in movies:
        vurl = "http://api.themoviedb.org/3/movie/{}?api_key={}&append_to_response=videos"\
            .format(movie["id"], key)
        vr = requests.get(vurl)
        vdata = vr.json()
        # for simplicity, use the first movie trailer option available for each movie
        if vdata["videos"]["results"]:
            youtube_url = "https://www.youtube.com/watch?v={}".format(
                vdata["videos"]["results"][0]["key"])
        else:
            youtube_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        movie["youtube_url"] = youtube_url
        films.append(media.Movie(movie["title"],
                                 movie["poster"],
                                 movie["youtube_url"],))
        print("Found: {}".format(movie["title"]))

    return films


# get_movies()
