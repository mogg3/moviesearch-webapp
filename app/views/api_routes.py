from flask import request
from flask_login import current_user, login_required

from controllers.chat_controller import initiate_chat
from controllers.omdb_controller import get_movies_by_title
from controllers.role_controller import get_role_by_name, add_admin_role_to_user, delete_admin_role_from_user
from controllers.user_controller import add_movie_to_users_watchlist, get_user_by_email, add_role_to_user, \
    add_friendship, delete_movie_from_users_watchlist, get_user_by_username
from views import app

import json

"""

Should we use post or put when updating an user?

 Update the name of the routes
 Add endpoints for chat, friends
 
 
 add role to user
 
 
"""


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


@app.route('/api/user/roles', methods=['GET'])
@login_required
def check_role():
    user = get_user_by_username(json.loads(request.values['username']))
    if len(user.roles) == 0:
        resp = "noadmin"
    else:
        resp = "admin"
    response = app.response_class(
        response=json.dumps(resp),
        status=200,
        mimetype="application/json"
    )
    return response


@app.route('/api/user/roles', methods=['PUT'])
@login_required
def add_role():
    user = get_user_by_username(json.loads(request.values['username']))
    admin_role = get_role_by_name("admin")
    add_role_to_user(user=user, role=admin_role)
    resp = f"added role to {user.username}"
    response = app.response_class(
        response=json.dumps(resp),
        status=200,
        mimetype="application/json"
    )
    return response


@app.route('/api/user/roles', methods=['DELETE'])
@login_required
def delete_role():
    user = get_user_by_username(json.loads(request.values['username']))
    delete_admin_role_from_user(user)
    resp = f"removed role from {user.username}"
    response = app.response_class(
        response=json.dumps(resp),
        status=200,
        mimetype="application/json"
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