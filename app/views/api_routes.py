from flask import request
from flask_login import current_user, login_required

import json

from data.MongoDB_MongoEngine.models.messages import Message

from controllers.chat_controller import initiate_chat, get_all_chats, add_message_to_chat
from controllers.omdb_controller import get_movies_by_title, get_movie_by_imdb_id
from controllers.role_controller import get_role_by_name, delete_admin_role_from_user
from controllers.user_controller import add_movie_to_users_watchlist, get_user_by_email, add_role_to_user, \
    add_friendship, delete_movie_from_users_watchlist, get_user_by_username

from views import app


# ska man försöka skapa så att routen blir /api/search?=imdb_id (exempelvis 2134384)
# har gjort det på watchlist men det funkar ju på att jinja2 har tillgång till flasks current_user..
# man behöver inte alltid ha data på jquery requests? när man använder sig av current user så går det ju att skicka infon i konstruktorn?


@app.route('/api/search', methods=['POST'])
def post_search():
    search_term = request.values['search_term']

    response = app.response_class(
        response=json.dumps(get_movies_by_title(search_term)),
        status=200,
        mimetype="application/json"
    )

    return response


@app.route('/api/movies/movie', methods=['POST'])
def get_movie():
    imdb_id = request.values['imdb_id']
    response = app.response_class(
        response=get_movie_by_imdb_id(imdb_id),
        status=200,
        mimetype="application/json"
    )

    return response


@app.route('/api/users/<username>/watchlist', methods=['PUT'])
@login_required
def put_watchlist(username):
    movie = json.loads(request.values['movie'])

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


@app.route('/api/users/<username>/watchlist', methods=['GET'])
@login_required
def get_watchlist(username):
    watchlist = current_user.watchlist
    print(watchlist)
    response = app.response_class(
        response=json.dumps(watchlist),
        status=200,
        mimetype="application/json"
    )
    return response


@app.route('/api/users/<username>/watchlist', methods=['DELETE'])
@login_required
def delete_from_watchlist(username):
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


@app.route('/api/users/<username>/friends', methods=['PUT'])
@login_required
def post_friendship(username):
    # todo: add friendship request

    friend = get_user_by_email(get_user_by_email(json.loads(request.values['friend_email'])))

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


@app.route('/api/users/<username>/friends/chats', methods=['GET'])
@login_required
def get_chat(username):
    chat = get_all_chats()[0]
    response = app.response_class(
        response=json.dumps(chat.to_json()),
        status=200,
        mimetype="application/json"
    )
    return response


# Not done
@app.route('/api/users/<username>/friends/chats/user_name_for_reciever/post', methods=['POST'])
@login_required
def post_message(username):
    message = request.values['message']
    sent_by = request.values['sent_by']
    chat = get_all_chats()[0]
    message = Message(sent_by=get_user_by_username(sent_by), text=message)
    add_message_to_chat(chat, message)
    response = app.response_class(
        response=json.dumps("sent"),
        status=200,
        mimetype="application/json"
    )
    return response


@app.route('/api/users/<username>/roles', methods=['PUT'])
@login_required
def add_role(username):
    user = get_user_by_username(json.loads(request.values['username']))
    admin_role = get_role_by_name("admin")
    add_role_to_user(user=user, role=admin_role)
    resp = f"added role"
    response = app.response_class(
        response=json.dumps(resp),
        status=200,
        mimetype="application/json"
    )
    return response


@app.route('/api/users/<username>/roles', methods=['DELETE'])
@login_required
def delete_role(username):
    user = get_user_by_username(json.loads(request.values['username']))
    delete_admin_role_from_user(user)
    resp = f"removed role"
    response = app.response_class(
        response=json.dumps(resp),
        status=200,
        mimetype="application/json"
    )
    return response


@app.route('/api/users/<username>/roles/admin', methods=['GET'])
@login_required
def get_if_admin_role():
    user = get_user_by_username(json.loads(request.values['username']))
    print("hello")
    # ändra så att det är true or false tillbaka
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


@app.route('/api/users/<username>/profile_picture', methods=['GET'])
@login_required
def get_profile_picture(username):
    # TODO: add check if picture do not exist
    response = current_user.profile_picture.read()

    return response

