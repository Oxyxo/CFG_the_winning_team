import requests
from datetime import datetime

# def get_genres():
#     response = requests.get(
#         f"https://api.themoviedb.org/3/genre/movie/list?api_key=91b59d00685f5ec6b4534a4b11ae1ffb")
#     data = response.json()
#     genres = {}
#     for genre in data["genres"]:
#         genres[genre["id"]] = genre["name"]
#     return genres
#
# genres = get_genres()
#
# def print_movie_result(movie):
#     date = datetime.strptime(movie['release_date'], "%Y-%m-%d")
#     genres_movie = []
#     for id in movie["genre_ids"]:
#         genres_movie.append(genres[id])
#     print(movie['original_title']+" - "+ str(date.year))
#     print(', '.join(genres_movie))


while True:
    user_movie = input("Which movie are you looking for?\n")
    if user_movie == ":q":
        break

    title_with_hyphen = user_movie.replace(" ", "-")

    response_API = requests.get(
        f"https://api.themoviedb.org/3/search/movie?api_key=91b59d00685f5ec6b4534a4b11ae1ffb&page=1&query={title_with_hyphen}")
    data = response_API.json()

    movie_list = []
    movie_id = 0
    list_number = 1

    for movie in data["results"]:
        movie_list.append(f"{list_number}. " + data["results"][movie_id]["original_title"])
        movie_id += 1
        list_number += 1
    print("\n".join(movie_list))

    for movie in data["results"]:
        try:
            print_movie_result(movie)
        except:
            continue



    overview_for_chosen = input("About which movie would you like to read? Give me a number from the list^\n")
    if overview_for_chosen == ":q":
        break

    number = int(overview_for_chosen) - 1
    print(data["results"][number]["original_title"] +" "+ data["results"][number]["release_date"][0:4])
    print(data["results"][number]["overview"])


