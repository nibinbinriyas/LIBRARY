from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField,PasswordField
from wtforms.validators import DataRequired,EqualTo,Email
from library.models import User
from wtforms import ValidationError

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



class LoginForm(FlaskForm):

    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    
    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),EqualTo('pass_confirm',message='Password must match')])
    pass_confirm = PasswordField('Confirm Password',validators=[DataRequired()])
    submit = SubmitField('Register')

def check_email(self,field):
    if User.query.filter_by(email=field.data).first():
        raise ValidationError('Email already registered!')

def check_username(self,field):
    if User.query.filter_by(username=field.data).first():
        raise ValidationError('Username already taken!')