from flask import Blueprint, render_template

# Defining that this file is the "blueprint" for our application
views = Blueprint('views', __name__)

# This function runs whenever we go to our '/' route in our URL
@views.route('/')
def home():
    return render_template("home.html") #renders home.html from our templates folder