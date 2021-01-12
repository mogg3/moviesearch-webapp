from flask_login import login_required, login_manager
from flask_security.utils import hash_password, login_user

from views import app, user_datastore
from flask import render_template, session, request, redirect, url_for

from views.api_routes import get_movie_by_title_first
from views.utils.flask_wtf import RegisterForm, LoginForm


@app.route('/', methods=['GET', 'POST'])
def index():
    global movie_information

    if request.method == 'POST':
        title = request.form['search']
        movie_information = get_movie_by_title_first(title)
        return render_template("index.html", movie_information=movie_information, title=movie_information['Title'],
                               poster=movie_information['Poster'])

    return render_template("index.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if request.method == "POST":
        user_datastore.create_user(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            password=hash_password(form.password.data)
        )
        return redirect(url_for('signin'))
    return render_template('signup.html', form=form)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form = LoginForm()

    if form.validate_on_submit():
        user = user_datastore.find_user(email=form.email.data)
        print(user.__str__)
        if user:
            login_user(user, remember=form.remember.data)
            # session['email'] = user.email
            return redirect(url_for('profile'))
    else:
        print(form.errors)
    return render_template('signin.html', form=form)


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')


@app.route('/edit_account')
def edit_account():
    return render_template('edit_account.html')

movie_information = None

@app.route('/movie/<title>')
def movie(title):
    return render_template('movie.html', title=title, movie_information=movie_information)


@app.route('/watchlist')
def watchlist():
    return render_template('watchlist.html')


# @app.route("/logout")
# def logout():
#     session.clear()
#     return None
#     return render_template('index.html')
# username = session['username']
# if username is None:
#     return render_template('index.html')
# return render_template('profile.html', username=username)

@app.route('/friends')
def friends():
    return render_template("friends.html")


@app.errorhandler(404)
def handler404(_):
    return render_template('404.html')
