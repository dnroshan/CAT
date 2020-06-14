
from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms import PasswordField
from wtforms.fields import SelectMultipleField
from wtforms import SubmitField
from wtforms import validators
from wtforms import widgets

import constants

class FormExaminerReg(FlaskForm):
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

    subject = SelectMultipleField(
        'subject',
        choices=list(zip(constants.SUBJECTS, constants.SUBJECTS)),
        validators=[
            validators.DataRequired(),
            validators.Length(max=50, message='This field can have at most 50 characters')
        ]
    )

    school = TextField(
        'school',
        validators=[
            validators.DataRequired(),
            validators.Length(max=50, message='This field can have at most 50 characters')
        ]
    )

    submit = SubmitField(
        'submit',
        validators=[
            validators.DataRequired()
        ]
    )

