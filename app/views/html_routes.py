from views import app
from flask import render_template, session, request

from views.api_routes import get_movie_by_title


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        title = request.form['search']
        result = get_movie_by_title(title)
        return render_template("index.html", title=result['Title'], poster=result['Poster'])

    return render_template("index.html")


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


@app.route('/friends')
def friends():
    return render_template("friends.html")


@app.errorhandler(404)
def handler404(_):
    return render_template('404.html')
