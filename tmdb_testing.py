import requests
import apikey

base_url = "https://api.themoviedb.org/3/search/movie"
# url = "https://api.themoviedb.org/3/search/movie"
key = apikey.apikey
lang = "&language=en-US&query="

query = "muppets"

end = "?api_key=" + key + "&language=en-US&query=" + query + "&page=1&include_adult=false"

# url = [key, lang, query, end]


# url = "".join([base_url, end])
#
# payload = {}
# response = requests.request("GET", url, data=payload)
url = "https://api.themoviedb.org/3/search/movie?api_key={}&language=en-US&query=" \
      "{}&page=1&include_adult=false".format(key, query)

r = requests.get(url)
# print(type(r))
import pprint
pp = pprint.PrettyPrinter(indent=4)
data = r.json()
# print(pp.pprint(data["results"][0]))
# print(pp.pprint(data))
# print(len(data["results"]))
movies = []
# for result in data["results"]:
#     # d = {}
#     # d["id"] = result["id"]
#     d = dict(id=result["id"], poster=result["poster_path"])
#     movies.append(d)

[movies.append(dict(id=result["id"], poster=result["poster_path"])) for result in data["results"]]
# print(movies)
# print(type(movies[0]["id"]))
# vurl = "https://api.themoviedb.org/3/movie/{}?api_key={}".format(movies[0]["id"], key)

vurl = "http://api.themoviedb.org/3/movie/{}?api_key={}&append_to_response=videos"\
    .format(157336, key)
vr = requests.get(vurl)
vdata = vr.json()
print(pp.pprint(vdata))
