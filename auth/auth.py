from flask import Blueprint, render_template, jsonify, request, redirect, url_for, flash
from flask_login import login_user, login_required, current_user
from .models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

DATA_churches = {
    'Athens': ['Athens'],
    'Community': ['Armor', 'Shield', 'Swords'],
    'Faith': ['Faith'],
    'Fellowship': [],
    'The Church Of Greenville': ['Liberty', 'Creatures', 'Stones', 'Vehement', 'Zealous'],
    'Logos': ['Logos'],
    'Old Suwanee': ['Old Suwanee'],
    'Progress': ['Progress'],
    'Ridgeview': ['1', '2'],
    'Tabernacle': ['Accord', 'Sons'],
    'Victory': ['Victory'],
}
# DATA_churches: dict[str, list[str]]

for church in DATA_churches:
    DATA_churches[church].insert(0, 'non-quizzer')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(username=username).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))  # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    return redirect(url_for('auth.profile'))


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html', churches=DATA_churches)

    # Get the selected values from the form
    username = request.form.get('username')
    password = generate_password_hash(request.form.get('password'), method='sha256')
    name = request.form.get('name')
    dob = request.form.get('dob')

    user = User(name=name, username=username, password=password, dob=dob)  # NOQA
    db.session.add(user)
    try:
        db.session.commit()
    except Exception as e:  # NOQA
        flash('Username already exists: ' + str(e))
        return redirect(url_for('auth.signup'))
    return redirect(url_for('auth.login'))


@auth.route('/teams_in_church')
def query():
    qchurch = request.args.get("church")
    teams = DATA_churches[qchurch]
    return jsonify(teams)


@login_required
@auth.route('/profile')
def profile():
    return render_template('profile.html', user=current_user)
