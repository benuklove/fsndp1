import requests
import apikey


key = apikey.apikey

query = "muppets"

url = "https://api.themoviedb.org/3/search/movie?api_key={}&language=en-US&query=" \
      "{}&page=1&include_adult=false".format(key, query)

r = requests.get(url)

import pprint
pp = pprint.PrettyPrinter(indent=4)
data = r.json()
# print(pp.pprint(data["results"][0]))

movies = []
# for result in data["results"]:
#     # d = {}
#     # d["id"] = result["id"]
#     d = dict(id=result["id"], poster=result["poster_path"])
#     movies.append(d)

# Add movies to the list
[movies.append(dict(id=result["id"], poster=result["poster_path"], popularity=result["popularity"]))
 for result in data["results"]]

vurl = "http://api.themoviedb.org/3/movie/{}?api_key={}&append_to_response=videos"\
    .format(157336, key)
vr = requests.get(vurl)
vdata = vr.json()
# print(pp.pprint(vdata["videos"]["results"][0]["key"]))

# Shorten longer list of movies that results from common movie title keywords


# for each dict, get and add youtube key
for movie in movies:
    vurl = "http://api.themoviedb.org/3/movie/{}?api_key={}&append_to_response=videos"\
        .format(movie["id"], key)
    vr = requests.get(vurl)
    vdata = vr.json()
    # for simplicity, use the first movie trailer option
    if vdata["videos"]["results"]:
        youtube_key = vdata["videos"]["results"][0]["key"]
    else:
        youtube_key = "None"
    movie["youtube_key"] = youtube_key

print(pp.pprint(movies))

