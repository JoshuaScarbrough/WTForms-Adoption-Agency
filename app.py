"""

These are the things when using Flask I need you to commit to memory by heart.

# Things used for the install
python -m venv venv
python -m pip install flask
python install Flask-DebugToolbar

# Commands to activate
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

# This variable is made so that we can run flask and it is also used for our debugger
app = Flask(__name__)

# The variable used when configurating the debugger
app.config['SECRET_KEY'] = "password"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

# This is the call that is made using the variable name app so that you can run your code.
if __name__ == '__main__':
    app.run(debug=True)

"""
from flask import Flask, render_template, url_for, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

# SQLALchemy Setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:football8114@localhost:5432/adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True


# This is what configurates the debugger
app.config['SECRET_KEY'] = "password"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

# Connects our app.py to our models.py
connect_db(app)
# db.create_all()

# This is an established route that is going to take us to our first page when the python file is ran
@app.route('/')
def home_page():
    """ Shows all pets"""

    # def __repr__(self):
    #     p = self
    #     return f"<pet id = {p.id} name = {p.name} species = {p.species} age = {p.age} notes = {p.notes}>"

    # This is querying inside of flask-sqlalchemy. Querying is calling / refrencng something inside of your database in pythonic language. For example pet.query.all() would be similar to SELECT * FROM pet
    # After the call SELECT * FROM pet its assigning the pet to the variable pets. Thats what this query is doing 
    pets = pet.query.all()

    # We pass in this query so that we can user are dunder quotes inside of our html application to pull the value out of the database and into the html.
    return render_template('home.html', pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Add a pet."""

    form = AddPetForm()

    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        new_pet = pet(**data)
        # new_pet = Pet(name=form.name.data, age=form.age.data, ...)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} added.")
        return redirect(url_for('home_page'))

    else:
        # re-present form for editing
        return render_template("pet_add_form.html", form=form)
    

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edit pet."""

    pets = pet.query.get_or_404(pet_id)
    form = EditPetForm(obj = pets)

    if form.validate_on_submit():
        pets.notes = form.notes.data
        pets.available = form.available.data
        pets.photo_url = form.photo_url.data
        db.session.commit()
        flash(f"{pets.name} updated.")
        return redirect(url_for('home_page'))

    else:
        # failed; re-present form for editing
        return render_template("pet_edit_form.html", form=form, pets=pets)
    

@app.route("/api/pets/<int:pet_id>", methods=['GET'])
def api_get_pet(pet_id):
    """Return basic info about pet in JSON."""

    pet = pet.query.get_or_404(pet_id)
    info = {"name": pet.name, "age": pet.age}

    return jsonify(info)


if __name__ == '__main__':
    app.run(debug=True)