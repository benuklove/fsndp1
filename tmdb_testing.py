import requests
import apikey
from operator import itemgetter

import pprint
pp = pprint.PrettyPrinter(indent=4)


key = apikey.apikey
query = "muppets"

url = "https://api.themoviedb.org/3/search/movie?api_key={}&language=en-US&query=" \
      "{}&page=1&include_adult=false".format(key, query)

r = requests.get(url)
data = r.json()
# print(pp.pprint(data["results"][0]))

movies = []

# Add movies to the list
[movies.append(dict(title=result["original_title"],
                    id=result["id"],
                    poster=result["poster_path"],
                    popularity=result["popularity"])) for result in data["results"]]

# Longer list of movies that results from common movie title keywords, shortened to 20 most popular
movies = sorted(movies, key=itemgetter("popularity"), reverse=True)[:20]

# For each dict, get and add youtube key
for movie in movies:
    vurl = "http://api.themoviedb.org/3/movie/{}?api_key={}&append_to_response=videos"\
        .format(movie["id"], key)
    vr = requests.get(vurl)
    vdata = vr.json()
    # for simplicity, use the first movie trailer option available for each movie
    if vdata["videos"]["results"]:
        youtube_key = vdata["videos"]["results"][0]["key"]
    else:
        youtube_key = "None"
    movie["youtube_key"] = youtube_key

print(pp.pprint(movies))
