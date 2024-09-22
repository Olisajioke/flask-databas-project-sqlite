from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TimeField, SelectField, URLField, FloatField
from wtforms.validators import DataRequired, URL, ValidationError


class MyForms(FlaskForm):
    title = StringField("Title",  validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    rating = FloatField("Rating", validators=[DataRequired()])
    review = StringField("Review")
    submit = SubmitField("Submit")