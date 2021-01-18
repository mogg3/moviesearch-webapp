import json

from flask_login import login_required, login_manager, current_user
from flask_security.utils import hash_password, login_user, logout_user, verify_password
from flask_security import roles_accepted, roles_required
from flask import render_template, session, request, redirect, url_for, Response, current_app

from controllers.role_controller import create_role, get_role_by_name, get_all_roles
from controllers.user_controller import get_user_by_email, create_user, add_role_to_user, get_all_users, \
    get_user_by_username
from views.api_routes import get_movie_by_title_first, get_movies_by_title
from views.utils.flask_wtf_classes import RegisterForm, LoginForm
from views import app
import json
from data.MongoDB_MongoEngine.db.db_user_role_security import user_datastore


@app.route("/")
def index():
    # user = get_user_by_email("hanna@hanna.com")
    # role = get_role_by_name("admin")
    # add_role_to_user(user, role)

    return render_template("index.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if request.method == "POST":
        create_user(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            password=hash_password(form.password.data),
            username=form.username.data
        )

        # create_role("editor")

        # role = get_role_by_name("editor")
        # user = get_user_by_email(email=form.email.data)
        # add_role_to_user(role=role, user=user)

        # user_datastore.create_role(name="admin")
        # user = user_datastore.find_user(email="o@o.com")
        # role = user_datastore.find_role("admin")
        # user_datastore.add_role_to_user(user=user, role=role)

        return redirect(url_for('signin'))
    return render_template('signup.html', form=form)


@app.route('/search', methods=['POST'])
def search():
    global movie_search_cache
    value = request.values['current_value']

    movie_result = get_movies_by_title(value)

    response = app.response_class(
        response=json.dumps(movie_result),
        status=200,
        mimetype="application/json"
    )

    return response


@app.route("/signout")
def signout():
    logout_user()
    print("Signing out")
    return render_template('index.html')


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', first_name=current_user.first_name, roles=current_user.roles)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form = LoginForm()
    if form.validate_on_submit():
        user = user_datastore.find_user(email=form.email.data)
        if user:
            if verify_password(form.password.data, user.password):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('profile'))

    return render_template('signin.html', form=form)


@app.route('/edit_account')
def edit_account():
    return render_template('edit_account.html')


@app.route('/movies/<title>')
def movie(title):
    movie_information = get_movie_by_title_first(title)
    return render_template('movie.html', movie_information=movie_information)


@app.route('/watchlist')
@login_required
def watchlist():
    return render_template('watchlist.html', watchlist=current_user.watchlist)


@app.route('/friends')
def friends():
    return render_template("friends.html")


@app.errorhandler(404)
def handler404(_):
    return render_template('404.html')


@app.route("/admin")
@roles_required("admin")
def admin():
    return render_template('admin.html', users=get_all_users(), roles=get_all_roles())


@app.route("/admin/users/<username>")
@roles_required("admin")
def user(username):

    user = get_user_by_username(username)

    print(user)


    return render_template('user.html', user=user)


@app.route('/admin/data/users', methods=['GET'])
def get_users():
    response = app.response_class(
        response=json.dumps([u.to_json() for u in get_all_users()]),
        status=200,
        mimetype="application/json"
    )
    return response

