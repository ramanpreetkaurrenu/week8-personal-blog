import os
import uuid
from functools import wraps

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    abort,
    current_app,
    Response
)

from flask_login import (
    login_user,
    logout_user,
    login_required,
    current_user
)

from flask_wtf import FlaskForm

from flask_wtf.file import (
    FileField,
    FileAllowed
)

from wtforms import (
    StringField,
    PasswordField,
    TextAreaField,
    SubmitField
)

from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length
)

from .extensions import db

from .models import (
    User,
    Post,
    Comment,
    Tag,
    ContactMessage
)