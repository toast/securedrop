# -*- coding: utf-8 -*-

from flask_babel import gettext
from flask_wtf import FlaskForm
from wtforms import (TextAreaField, TextField, BooleanField, HiddenField,
                     ValidationError)
from wtforms.validators import InputRequired, Optional, Length

from db import Journalist


def otp_secret_validation(form, field):
    strip_whitespace = field.data.replace(' ', '')
    if len(strip_whitespace) != 40:
        raise ValidationError(gettext('Field must be 40 characters long.'))


class NewUserForm(FlaskForm):
     username = TextField('username', validators=[
         InputRequired(message=gettext('This field is required.')),
         Length(min=Journalist.MIN_USERNAME_LEN,
                message=gettext('Field must be at least {min_chars} '
                                'characters long.'.format(
                                    min_chars=Journalist.MIN_USERNAME_LEN))),
     ])
     password = HiddenField('password')
     is_admin = BooleanField('is_admin')
     is_hotp = BooleanField('is_hotp')
     otp_secret = TextField('otp_secret', validators=[
         otp_secret_validation,
         Optional()
     ])


class ReplyForm(FlaskForm):
    message = TextAreaField(
        u'Message',
        id="content-area",
        validators=[
            InputRequired(message=gettext('You cannot send an empty reply.')),
        ],
    )
