from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from flask_security import roles_required
from flask_security.utils import login_user, logout_user, verify_password

from controllers.role_controller import get_all_roles
from controllers.user_controller import create_user, get_all_users, get_user_by_username, get_user_by_email, \
    add_profile_picture_to_user, delete_profile_picture_if_exists

from views import app
from views.utils.flask_wtf_classes import RegisterForm, LoginForm


@app.route("/", methods =['GET', 'POST'])
def index():
    form = LoginForm()
    error = None
    if request.method == "POST":
        if form.validate_on_submit():
            user = get_user_by_email(email=form.email.data)
            if user and verify_password(form.password.data, user.password):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('profile'))
            else:
                error = "Wrong email or password"
    return render_template("index.html", form=form, errors=error)


# @app.route('/', methods=['POST'])
# def sign_in():
#     form = LoginForm()
#     error = None
#     if request.method == "POST":
#         if form.validate_on_submit():
#             user = get_user_by_email(email=form.email.data)
#
#             if user and verify_password(form.password.data, user.password):
#                 login_user(user, remember=form.remember.data)
#                 return redirect(url_for('profile'))
#             else:
#                 error = "Wrong email or password"
#     return render_template('signin.html', form=form, errors=error)


@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    form = RegisterForm()

    if request.method == "POST":
        if form.validate_on_submit():

            create_user(
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                email=form.email.data,
                password=form.password.data,
                username=form.username.data
            )
            return redirect(url_for('sign_in'))

    return render_template('signup.html', form=form)


@app.route("/signout")
@login_required
def sign_out():
    logout_user()
    return redirect(url_for('index'))


@app.route('/profile', methods=['GET'])
@login_required
def profile():
    if len(current_user.roles) == 0:
        return render_template('profile.html', user=current_user, role=False)
    else:
        return render_template('profile.html', user=current_user, role=current_user.roles[0])


@app.route('/profile', methods=['POST'])
@login_required
def post_profile_picture(): #change name
    if request.method == "POST":
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file.filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}:
            delete_profile_picture_if_exists(current_user)
            add_profile_picture_to_user(current_user, file)
        else:
            flash('Wrong file format. Choose between png, jpg, jpeg and gif.')

    return redirect(url_for('profile'))


@app.route('/watchlist', methods=['GET'])
@login_required
def watchlist():
    return render_template('watchlist.html', watchlist=current_user.watchlist)


@app.route('/friends', methods=['GET'])
@login_required
def friends():
    return render_template("friends.html", user=current_user)


@app.route("/admin", methods=['GET'])
@roles_required("admin")
def admin():
    return render_template('admin.html', users=get_all_users(), roles=get_all_roles())


@app.route("/admin/users/<username>", methods=['GET'])
@roles_required("admin")
def user(username):
    user = get_user_by_username(username)
    if len(user.roles) == 0:
        return render_template('user.html', user=user, role=False)
    else:
        return render_template('user.html', user=user, role=user.roles[0])


@app.errorhandler(404)
def handler404(_):
    return render_template('404.html')
