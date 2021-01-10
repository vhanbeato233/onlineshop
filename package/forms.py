from flask import request
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from package.models import User, Item
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError, NumberRange

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=25)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    fname = StringField('First Name', validators=[DataRequired(), Length(min=2, max=25)])
    lname = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=25)])
    password = PasswordField('Password', validators=[DataRequired()])
    cpassword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=request.form['username']).first()
        if user:
            raise ValidationError('The Username is Taken!')
    def validate_email(self, email):
        user = User.query.filter_by(email=request.form['email']).first()
        if user:
            raise ValidationError('The Email is Already Register!')

    def reset(self):
        blankData = MultiDict([ ('csrf', self.reset_csrf() ) ])
        self.process(blankData)

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

    def reset(self):
        blankData = MultiDict([ ('csrf', self.reset_csrf() ) ])
        self.process(blankData)

class UpdateAccountForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=25)])
    fname = StringField('First Name', validators=[DataRequired(), Length(min=2, max=25)])
    lname = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=25)])
    profile_picture = FileField('Picture', validators=[FileAllowed(['jpeg', 'png', 'jpg'])])
    submit = SubmitField('Update')

class ItemsForm(FlaskForm):
    itemname = StringField('Item Name', validators=[DataRequired(), Length(min=2, max=15)])
    description = StringField('Item Description', validators=[Length(min=2, max=355)])
    item_image = FileField('Image', validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    price = IntegerField('Price', validators=[DataRequired(), NumberRange(min=1, max=20)])
    submit = SubmitField('Add Items')

class UpdateItemsForm(FlaskForm):
    itemname = StringField('Item Name', validators=[DataRequired(), Length(min=2, max=15)])
    description = StringField('Item Description', validators=[Length(min=2, max=355)])
    item_image = FileField('Image', validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    price = IntegerField('Price', validators=[DataRequired(), NumberRange(min=1, max=20)])
    submit = SubmitField('Update Items')
