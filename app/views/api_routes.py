from flask import request
from flask_login import current_user

from controllers.omdb_controller import get_movies_by_title
from controllers.user_controller import add_movie_to_users_watchlist
from views import app

import json


@app.route('/search', methods=['POST'])
def search():
    search_term = request.values['search_term']

    response = app.response_class(
        response=json.dumps(get_movies_by_title(search_term)),
        status=200,
        mimetype="application/json"
    )

    return response


@app.route('/post_watchlist', methods=['POST'])
def post_watchlist():
    movie = json.loads(request.values['movie'])

    response = True

    if [m for m in current_user.watchlist if m['Title'] == movie['Title']]:
        print("already added movie")
        response = False
    else:
        add_movie_to_users_watchlist(current_user, movie)

    response = app.response_class(
        response=json.dumps(response),
        status=200,
        mimetype="application/json"
    )

    return response

# @app.route('/admin/data/users', methods=['GET'])
# def get_users():
#     response = app.response_class(
#         response=json.dumps([u.to_json() for u in get_all_users()]),
#         status=200,
#         mimetype="application/json"
#     )
#     return response
