from data.omdb.repository import omdb_repository as omr


def get_movies_by_title(input_title) -> list:
    return omr.get_movies_by_title(input_title)


def get_movie_by_title_first(input_title) -> list:
    return omr.get_movie_by_title_first(input_title)


def get_movie_by_imdb_id(imdb_id) -> list:
    return omr.get_movie_by_imdb_id(imdb_id)
