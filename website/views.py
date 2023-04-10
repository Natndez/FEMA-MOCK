from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, Item
from . import db
import json

# Defining that this file is the "blueprint" for our application
views = Blueprint('views', __name__)

# This function runs whenever we go to our '/' route in our URL
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        
        # TODO: Figure out how to get Notes and Items functioning
        # note = request.form.get('note')

        # if len(note) < 1:
        #     flash('Note is too short!', category='error')
        # else:
        #     new_note = Note(data=note, user_id=current_user.id)
        #     db.session.add(new_note)
        #     db.session.commit()
        #     flash('Note added!', category='success')
        
        # CODE TO MANIPULATE DATABASE TABLES
        itemName = request.form.get('name')
        quantityNeeded = request.form.get('quantity_needed')

        new_item = Item(name=itemName, quantity=0, requested=quantityNeeded)
        db.session.add(new_item)
        db.session.commit()


    return render_template("home.html", user=current_user) #renders home.html from our templates folder

@views.route('/delete-note', methods=['POST'])
def delete_note():
    data = json.loads(request.data)
    noteId = data['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    
    return jsonify({})