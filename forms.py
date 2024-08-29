"""
When creating a form using Flask WTForms you must have an import first. The import is pip install -U Flask-WTF
The purpose of this is so that we don't have to keep recreating forms over and over again. You can make all the forms in here and then inherit from them inside of your html.

"""
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField(
        "Pet Name",
        validators =[InputRequired()],
    )

    species = SelectField(
        "Species",
        choices=[("dog", "Dog")],
    )

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],
    )

    age = IntegerField(
        "Age",
        validators=[Optional(), NumberRange(min=0, max=30)],
    )

    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10)],
    )


class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],
    )

    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10)],
    )

    available = BooleanField("Available?")