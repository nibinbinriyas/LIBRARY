from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField

class AddForm(FlaskForm):

    name = StringField("Title of Book    ")
    auther = StringField("Auther of Book    ")
    price = StringField("Price of the Book ")
    image = StringField("url for image ")
    submit = SubmitField("Add Book")

class DelForm(FlaskForm):
    id = IntegerField("Id of the Book    ")
    submit = SubmitField("Buy")

class SearchForm(FlaskForm):
    auther = StringField("Enter Auther's Name    ")
    submit = SubmitField("Search")