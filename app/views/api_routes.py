import base64
import codecs
from typing import io

from flask import request, send_file
from flask_login import current_user, login_required
from pymongo import response
from werkzeug.utils import secure_filename, redirect

from controllers.chat_controller import initiate_chat
from controllers.omdb_controller import get_movies_by_title, get_movie_by_imdb_id
from controllers.role_controller import get_role_by_name, add_admin_role_to_user
from controllers.user_controller import add_movie_to_users_watchlist, get_user_by_email, add_role_to_user, \
    add_friendship, delete_movie_from_users_watchlist, add_profile_picture_to_user
from views import app

import json

"""

Should we use post or put when updating an user?

 Update the name of the routes
 Add endpoints for chat, friends
 
 
 add role to user
 
 
"""
@app.route('/api/users/<username>/profile_picture', methods=['GET'])
@login_required
def get_profile_picture(username):
    image = current_user.profile_picture.read()
    # if image:
    #     with open('static/images/no_profile_picture.png', 'r') as no_profile_picture:

    return image

@app.route('/movie', methods=['POST'])
def get_movie():
    imdb_id = request.values['imdb_id']

    response = app.response_class(
        response=get_movie_by_imdb_id(imdb_id),
        status=200,
        mimetype="application/json"
    )

    return response

@app.route('/search', methods=['POST'])
def search():
    search_term = request.values['search_term']

    response = app.response_class(
        response=json.dumps(get_movies_by_title(search_term)),
        status=200,
        mimetype="application/json"
    )

    return response


@app.route('/api/users/<username>/watchlist', methods=['PUT'])
@login_required
def put_watchlist(username):
    movie = json.loads(request.values['movie'])
    resp = ""

    if movie in current_user.watchlist:
        resp = f"Already added {movie['Title']} to your watchlist"
    else:
        add_movie_to_users_watchlist(current_user, movie)
        resp = f"{movie['Title']} added"

    response = app.response_class(
        response=json.dumps(resp),
        status=200,
        mimetype="application/json"
    )
    return response


@app.route('/api/users/<username>/watchlist', methods=['DELETE'])
@login_required
def delete_watchlist(username):
    movie = json.loads(request.values['movie'])
    resp = ""

    delete_movie_from_users_watchlist(current_user, movie)

    if movie not in current_user.watchlist:
        resp = f"You removed {movie['Title']} to your watchlist"
    else:
        resp = f"You failed to remove {movie['Title']} to your watchlist"

    response = app.response_class(
        response=json.dumps(resp),
        status=200,
        mimetype="application/json"
    )
    return response


@app.route('/api/user/roles', methods=['PUT'])
@login_required
def add_role():
    user = get_user_by_email(json.loads(request.values['user_email']))
    add_admin_role_to_user(user)

    response = app.response_class(
        status=200,
    )
    return response

@app.route('/api/user/roles', methods=['DELETE'])
@login_required
def delete_role():
    user = get_user_by_email(json.loads(request.values['user_email']))
    response = app.response_class(
        status=200,
    )
    return response


@app.route('/user/friends', methods=['PUT'])
@login_required
def add_friendship():
    #todo: add friendship request

    friend = get_user_by_email(get_user_by_email(json.loads(request.values['friend_email'])))
    add_friendship(user=current_user, friend=friend)

    if friend in current_user.friends:
        resp = f"you are already friend with {friend.username}"
    else:
        add_friendship(user=current_user, friend=friend)
        resp = f"You are now friends with {friend.username}"

    initiate_chat(user_1=current_user, user_2=friend)

    response = app.response_class(
        response=json.dumps(resp),
        status=200,
        mimetype="application/json"
    )

    return response