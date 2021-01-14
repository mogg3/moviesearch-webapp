import requests

from views.api_settings import API_KEY


def get_movie_by_title_first(input_title):
    parameters = {'t': input_title, 'r': 'json', 'plot': 'short'}

    req = requests.get(f'http://www.omdbapi.com/?apikey={API_KEY}', params=parameters)

    return req.json()


def get_movies_by_title(input_title):
    parameters = {'s': {input_title}, 'r': 'json', 'plot': 'short', 'page': 1, 'apikey': API_KEY}
    info = requests.get(f'http://www.omdbapi.com/', params=parameters)
    info = info.json()
    movie_list = []
    for movie in info["Search"]:
        movie_list.append(movie)
    return movie_list



