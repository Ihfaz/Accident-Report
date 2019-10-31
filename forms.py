# DataRequired -- doesn't accept empty field
# Length -- sets the length of the input
# Email -- email input
# EqualTo -- chack if equal to another field

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                            validators=[DataRequired(), Length(min=2, max=20)])        # Must be 2 to 20 characters long
    email = StringField('Email',
                        validators=[DataRequired(), Email()])                          # Email field
    password = PasswordField('Password', validators=[DataRequired()])                  # Password field
    confirm_password = PasswordField('Confirm Password', 
                                    validators=[DataRequired(), EqualTo('password')])  # Confirm password field
    submit = SubmitField('Sign up')                                                    # Sign up button


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])           # Email field
    password = PasswordField('Password', validators=[DataRequired()])   # Password field
    remember = BooleanField('Remember me')                              # Remember me option
    submit = SubmitField('Login')                                       # Login button