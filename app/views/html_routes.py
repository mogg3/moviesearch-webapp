from views import app
from flask import render_template, session, request

from views.api_routes import get_movie_by_title_first, get_movies_by_title


@app.route('/login')
def login():
    #session['username'] = username
    return render_template('login.html')


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        title = request.form['search']
        movie_information = get_movie_by_title_first(title)


        return render_template("index.html", movie_information=movie_information, title=movie_information['Title'], poster=movie_information['Poster'])

    return render_template("index.html")


@app.route('/movie/<title>')
def movie(title):

    movie_information = get_movie_by_title_first(title)

    return render_template('movie.html', movie_information=movie_information)


@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/watchlist')
def watchlist():
    return render_template('watchlist.html')

@app.route('/create_account')
def create_account():
    return render_template('create_account.html')

@app.route('/edit_account')
def edit_account():
    return render_template('edit_account.html')


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
