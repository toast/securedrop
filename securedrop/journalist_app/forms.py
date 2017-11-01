# -*- coding: utf-8 -*-

from flask_babel import gettext
from flask_wtf import FlaskForm
from wtforms import TextAreaField, TextField, BooleanField, HiddenField
from wtforms.validators import InputRequired, Optional, Length


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
         Length(min=40, max=40,
                message=gettext('Field must be 40 characters long.')),
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
