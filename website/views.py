from flask import Blueprint, render_template
from flask_login import login_required, current_user

# Defining that this file is the "blueprint" for our application
views = Blueprint('views', __name__)

# This function runs whenever we go to our '/' route in our URL
@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user) #renders home.html from our templates folder