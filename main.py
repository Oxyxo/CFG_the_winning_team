import requests
import json
import pprint

user_movie = input("Which movie are you looking for?\n")

title_with_hyphen = user_movie.replace(" ", "-")
response_API = requests.get(
    f"https://api.themoviedb.org/3/search/movie?api_key=91b59d00685f5ec6b4534a4b11ae1ffb&page=1&query={title_with_hyphen}")
data = response_API.json()
number = 0

for movie in data["results"]:
    movie_overview = data["results"][number]["original_title"]
    number += 1
    print(movie_overview)

overview_for_chosen = input("About which movie would you like to read?\n")
print(overview_for_chosen)
hyphen = overview_for_chosen.replace(" ", "-")
from_API = requests.get(
    f"https://api.themoviedb.org/3/search/movie?api_key=91b59d00685f5ec6b4534a4b11ae1ffb&page=1&query={hyphen}")
print(data["results"][0]["overview"])



