import requests
from datetime import datetime

#part 1
def get_genres():
    response = requests.get(
        f"https://api.themoviedb.org/3/genre/movie/list?api_key=91b59d00685f5ec6b4534a4b11ae1ffb")
    data = response.json()
    genres = {}
    for genre in data["genres"]:
        genres[genre["id"]] = genre["name"]
    return genres

genres = get_genres()

def print_movie_result(number, movie):
    date = datetime.strptime(movie['release_date'], "%Y-%m-%d")
    genres_movie = []
    for id in movie["genre_ids"]:
        genres_movie.append(genres[id])
    print(str(number) +". "+ movie['original_title']+" - "+ str(date.year))
    print(', '.join(genres_movie))

while True:
    user_movie = input("Which movie are you looking for? (type exit to quit)\n")
    if user_movie == "exit":
        break
    title_with_hyphen = user_movie.replace(" ", "-")

    response_API = requests.get(
        f"https://api.themoviedb.org/3/search/movie?api_key=91b59d00685f5ec6b4534a4b11ae1ffb&page=1&query={title_with_hyphen}")
    data = response_API.json()

    movies = data["results"]

    for number, movie in enumerate(movies):
        number = number + 1
        try:
            print_movie_result(number, movie)
        except:
            continue


    #part 2 additional information about movie: overview and score
    def print_additional_data(movie):
        print(movie["original_title"] +": " +movie["overview"])
        if movie["vote_average"] >= 6.00:
            print("This movie is popular!")
        elif 0 < movie["vote_average"] < 6.00:
            print("This movie scored below average on reviews")
        else:
            return

    overview_for_chosen = input("About which movie would you like to read? Please enter a number between 1-20.\n")
    if overview_for_chosen.isdigit():
        if 1<= int(overview_for_chosen)-1<=20:
            selected_movie = movies[int(overview_for_chosen)-1]
        else:
            print("Error, number is out of range")
            break
    else:
        print("Error, wrong symbol was entered!")
        break

    #this prints the selected movie title, overview and score
    print_additional_data(selected_movie)



