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
        if current_user.role == "FEMA Representative":
            itemName = request.form.get('name')
            quantityNeeded = request.form.get('quantity_needed')

            new_item = Item(name=itemName, quantity=0, requested=quantityNeeded, status="Awaiting Donations", user=current_user.last_name)
            db.session.add(new_item)
            db.session.commit()

        elif current_user.role == "Donor":
            item_id = request.form.get('item')
            quantity = int(request.form.get('quantity'))

            # Retrieve the item from the database
            item = Item.query.filter_by(id=item_id).first()

            if item:
                # Update the item's quantity and requested fields
                item.quantity += quantity
                if item.requested is not None:
                    item.requested -= quantity
                    if item.requested <= 0:
                        item.requested = 0
                        item.status = "Awaiting Driver"

                # Commit the changes to the database
                db.session.commit()

        elif current_user.role == "Driver":
            item_id = request.form.get('item_id')
            

            # Retrieve items from database
            item = Item.query.filter_by(id=item_id).first()

            if item and item.status == "Awaiting Driver":
                # Update status
                item.status = "In Transit"
                db.session.commit()

        elif current_user.role == "Worker":
            item_id = request.form.get('item_id')

            item = Item.query.filter_by(id=item_id).first()

            if item and item.status == "In Transit":

                item.status = "Delivered"
                db.session.commit()

        # Reload the items from the database
        items = Item.query.all()

        # Render the template with the updated items
        return render_template("home.html", user=current_user, items=items)

    # If the request is a GET request, just render the template with the items from the database
    items = Item.query.all()
    return render_template("home.html", user=current_user, items=items)
    
    
    

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