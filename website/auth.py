from flask import Blueprint, render_template, request, flash

# Defining the "blueprint" for our application
auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', boolean=True)

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        # .get(x) x: string of the specific form item you want
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # Check validity of user inputs
        if len(email) < 4:
            flash('Email must be longer than 3 characters', category='error')
        elif len(firstName) < 2:
            flash('First name must be longer than 1 characters', category='error')
        elif len(lastName) < 2:
            flash('Last name must be longer than 1 characters', category='error')
        elif password1 != password2:
            flash('Your passwords do not match', category='error')
        elif len(password1) < 7:
            flash('Password at least 7 characters', category='error')
        else:
            flash('Account created!', category='success')
            
    return render_template('signup.html')
