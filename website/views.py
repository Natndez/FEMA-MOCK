from flask import Blueprint

# Defining that this file is the "blueprint" for our application
views = Blueprint('views', __name__)

# This function runs whenever we go to our '/' route in our URL
@views.route('/')
def home():
    return "<h1>Testing<h1>"
