from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, current_user
from . import db, User

# Built of Blueprint for authentication
auth = Blueprint('auth', __name__)


@auth.route('/login')
def render_to_login():
    return render_template('form_connexion.html')


@auth.route('/login_action', methods=['GET', 'POST'])
def login_action():
    # Capture the data entered from the login form
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        # remember = True if request.form.get('remember') else False

        # Verify if the user already exists
        verify_user = User.query.filter_by(email=email).first()
        # If the user does not exist Or the passwords hashed aren't the same
        if not verify_user or check_password_hash(verify_user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('auth.render_to_login'))
        # Connect the user practically
        # login_user(verify_user, remember=remember)
        login_user(verify_user)

        return render_template('profile.html', verify_user=current_user)


@auth.route('/signup')
def render_to_signup():
    return render_template('form_inscription.html')


@auth.route('/signup_action', methods=['GET', 'POST'])
def signup_action():
    # Capture the data entered from the sign up form
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    password = request.form.get('password')
    direction = request.form.get('direction')

    # Verify if the user already exists
    verify_user = User.query.filter_by(email=email).first()
    if verify_user:
        flash('Email address already exists')
        return redirect(url_for('auth.render_to_signup'))
    # If the user does not exist
    password = generate_password_hash(password, method='sha256')
    user = User(first_name, last_name, email, password, direction)
    db.session.add(user)
    db.session.commit()

    return redirect(url_for('auth.render_to_login'))

# To manage access and protect pages ==> @login_required
@auth.route('/logout')
@login_required
def render_to_logout():
    return render_template('')
