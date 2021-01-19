from data.omdb.repository import omdb_repository as omdbr


def get_movie_by_title_first(input_title):
    return omdbr.get_movie_by_title_first(input_title)


def get_movies_by_title(input_title):
    return omdbr.get_movies_by_title(input_title)


def get_movie_by_imdb_id(imdb_id):
    return omdbr.get_movie_by_imdb_id(imdb_id)
