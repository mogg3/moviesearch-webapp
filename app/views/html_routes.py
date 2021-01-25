from flask import render_template, request, redirect, url_for, flash, g
from flask_login import login_required, current_user
from flask_security import roles_required
from flask_security.utils import login_user, logout_user, verify_password
from werkzeug.utils import secure_filename
from controllers.role_controller import get_all_roles, get_role_by_name, add_admin_role_to_user
from controllers.user_controller import create_user, get_all_users, get_user_by_username, get_user_by_email, add_profile_picture_to_user, delete_profile_picture_if_exists

from controllers.chat_controller import initiate_chat


from views import app
from views.utils.flask_wtf_classes import RegisterForm, LoginForm


@app.route("/")
def index():
    # user = get_user_by_email('hanna@hanna.com')
    # # with open('C:\\Github\\Project_Movie_Web_App\\app\\test.jpg', 'rb') as fd:
    # #     user.profile_picture.put(fd, content_type='image/jpeg')
    # # user.save()
    #
    # img = user.profile_picture
    #initiate_chat(get_user_by_username("ellica123"), get_user_by_username("marcus123"))
    return render_template("index.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if request.method == "POST":
        if form.validate_on_submit():
            # add check if user email or username already exists
            create_user(
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                email=form.email.data,
                password=form.password.data,
                username=form.username.data
            )
            return redirect(url_for('signin'))
        # {field.name: "\n".join(field.errors) for field in form}

    return render_template('signup.html', form=form)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form = LoginForm()
    error = None


    if request.method == "POST":
        if form.validate_on_submit():
            user = get_user_by_email(email=form.email.data)

            if user and verify_password(form.password.data, user.password):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('profile'))
            else:
                error = "wrong email or password"
    return render_template('signin.html', form=form, errors=error)


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')


@app.route('/profile', methods=['POST'])
@login_required
def upload_profile_picture():

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


@app.route("/signout")
@login_required
def signout():
    logout_user()
    return render_template('index.html')


@app.route('/edit_account')
@login_required
def edit_account():
    return render_template('edit_account.html')


@app.route('/friends')
@login_required
def friends():
    return render_template("friends.html", user = current_user)


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
    user=get_user_by_username(username)
    if len(user.roles) == 0:
        return render_template('user.html', user=user, role= False)
    else:
        return render_template('user.html', user=user, role= user.roles[0])


@app.route('/watchlist')
@login_required
def watchlist():
    return render_template('watchlist.html', watchlist=current_user.watchlist)
