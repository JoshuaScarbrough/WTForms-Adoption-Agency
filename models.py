"""
Important things to remember when creating a model in python. Remeber that the model is where your gonna connect your sqlalchemy
In this course specifically were using flask-sqlalchemy so we have to remember the command 
pip install Flask-SQLAlchemy

We set it up with the command from flask_sqlalchemy import SQLAlchemy

Were also gonna want to give SQLAlchemy a variable, which we use as db that is gonna help with setup.
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Image just in case the animal doesn't have one just yet
GENERIC_IMAGE = "https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif"

# This is what connects our SQLAlchemy to our app.py
# Remember the reason that were using flask_sqlalchemy is because it adds support for SQLAlchemy to your application. It simplifies using SQLAlchemy with Flask by setting up common objects and patterns for using those objects, such as a session tied to each web request, models, and engines.
# SQLAlchemy is used to connect python to our databases. We can use pythonic language to code our databases using sqlalchemy
def connect_db(app):
    db.app = app
    db.init_app(app)

# This is the model that were gonna use inside of the adopt database. There is gonna be a class for pet that can be entered.
# The pets have an id, name, species, photo_url, age, notes, availability of animal on website.
# In the future make sure you capatilize this 
class pet(db.Model):

    __tablename__ = "pets"

    # Was giving an example of what a class method was / is / and the value of one
    # @classmethod
    # def get_by_species(cls, species):
    #     return cls.query.filter_by(species = species.all)

    
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.Text, nullable = False)
    species = db.Column(db.Text, nullable = False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable = False, default = True)

    # This is a method. These are helpful. This does something with the information you have.
    def greet(self):
        return f"Hi, I am {self.name} the {self.species} "
    
    def image_url(self):
        """Return image for pet -- bespoke or generic."""

        return self.photo_url or GENERIC_IMAGE


