from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import length


class Signup(FlaskForm):
    review = StringField("review")
    new_rating = StringField("rating", validators=[length(max=30)])
    submit = SubmitField("Submit")


class MovieTitle(FlaskForm):
    title = StringField("Movie name")
    submit = SubmitField("Submit")
