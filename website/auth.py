from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

# Defining the "blueprint" for our application
auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Method to search through database        
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password. Try again', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template('login.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():   
    logout_user()
    flash('Logged out', category='success')
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        # .get(x) x: string of the specific form item you want
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        occupation = request.form.get('occupation')

        user = User.query.filter_by(email=email).first()

        # Check validity of user inputs
        if user:
            flash('Email already in use.', category='error')
        elif len(email) < 4:
            flash('Email must be longer than 3 characters', category='error')
        elif len(first_name) < 2:
            flash('First name must be longer than 1 characters', category='error')
        elif len(last_name) < 2:
            flash('Last name must be longer than 1 characters', category='error')
        elif password1 != password2:
            flash('Your passwords do not match', category='error')
        elif len(password1) < 7:
            flash('Password at least 7 characters', category='error')
        # Succesful User creation
        else:
            # Add new user to the database
            new_user = User(email=email, first_name=first_name, last_name=last_name, password=generate_password_hash(password1, method='sha256'), role=occupation)
            db.session.add(new_user)
            db.session.commit()
            # login_user(user, remember=False)
            
            # Flash message stating account creation was successful
            flash('Account created!', category='success')

            # Redirect user to home page
            return redirect(url_for('views.home'))
            
    return render_template('signup.html', user=current_user)
