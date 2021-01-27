from data.omdb.repository import omdb_repository as omr


def get_movie_by_title_first(input_title):
    return omr.get_movie_by_title_first(input_title)


def get_movies_by_title(input_title):
    return omr.get_movies_by_title(input_title)


def get_movie_by_imdb_id(imdb_id):
    return omr.get_movie_by_imdb_id(imdb_id)
