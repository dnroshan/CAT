
from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms import PasswordField
from wtforms.fields.html5 import DateField
from wtforms.fields import SelectField
from wtforms import SubmitField
from wtforms.fields.html5 import EmailField
from wtforms import validators

import constants

class FormCandidateReg(FlaskForm):
    username = TextField(
        'username',
        validators=[
            validators.DataRequired(),
            validators.Length(min=4, max = 50, message='Choose a username of at least 4 characters')
        ]
    )

    password = PasswordField(
        'password',
        validators=[
            validators.DataRequired(),
            validators.Length(min=8, message='Choose a password of at least 8 characters')
        ]
    )

    passwordre = PasswordField(
        'passwordre',
        validators=[
            validators.DataRequired(),
            validators.EqualTo('password', message='Passwords must match')
        ]
    )

    first_name = TextField(
        'first_name',
        validators=[
            validators.DataRequired(),
            validators.Length(max=50, message='This field can have at most 50 characters')
        ]
    )

    last_name = TextField(
        'last_name',
        validators=[
            validators.DataRequired(),
            validators.Length(max=50, message='This field can have at most 50 characters')
        ]
    )

    dob = DateField(
        'dob',
        validators=[
            validators.DataRequired()
        ]
    )

    gender = SelectField(
        'gender',
        choices=[('Male', 'Male'), ('Female', 'Female')],
        validators=[
            validators.DataRequired()
            validators.Length(max=8, message='This field can have at most 8 characters')
        ]
    )

    standard = SelectField(
        'standard',
        choices=list(zip(constants.STANDARDS, constants.STANDARDS)),
        validators=[
            validators.DataRequired()
        ]
    )

    school = TextField(
        'school',
        validators=[
            validators.DataRequired(),
            validators.Length(max=50, message='This field can have at most 50 characters')
        ]
    )

    email = EmailField(
        'email',
        validators=[
            validators.DataRequired(),
            validators.Email(),
            validators.Length(max=50, message='This field can have at most 50 characters')
        ]
    )

    phone = TextField(
        'phone',
        validators=[
            validators.DataRequired(),
            validators.Length(max=50, message='This field can have at most 20 characters')
        ]
    )
    
    submit = SubmitField(
        'submit',
        validators=[
            validators.DataRequired()
        ]
    )
