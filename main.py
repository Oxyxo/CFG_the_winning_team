import requests
from datetime import datetime

def get_genres():
    response = requests.get(
        f"https://api.themoviedb.org/3/genre/movie/list?api_key=91b59d00685f5ec6b4534a4b11ae1ffb")
    data = response.json()
    genres = {}
    for genre in data["genres"]:
        genres[genre["id"]] = genre["name"]
    return genres

genres = get_genres()

def print_movie_result(movie):
    date = datetime.strptime(movie['release_date'], "%Y-%m-%d")
    genres_movie = []
    for id in movie["genre_ids"]:
        genres_movie.append(genres[id])
    print(movie['original_title']+" - "+ str(date.year))
    print(', '.join(genres_movie))


user_movie = input("Which movie are you looking for?\n")
title_with_hyphen = user_movie.replace(" ", "-")

response_API = requests.get(
    f"https://api.themoviedb.org/3/search/movie?api_key=91b59d00685f5ec6b4534a4b11ae1ffb&page=1&query={title_with_hyphen}")
data = response_API.json()


for movie in data["results"]:
    try:
        print_movie_result(movie)
    except:
        continue

overview_for_chosen = input("About which movie would you like to read?\n")
print(overview_for_chosen)
hyphen = overview_for_chosen.replace(" ", "-")
from_API = requests.get(
    f"https://api.themoviedb.org/3/search/movie?api_key=91b59d00685f5ec6b4534a4b11ae1ffb&page=1&query={hyphen}")
print(data["results"][0]["overview"])



