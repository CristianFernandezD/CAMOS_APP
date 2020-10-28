# coding: utf-8

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	username = StringField('Nombre de Usuario', validators=[DataRequired()])
	password = PasswordField('Clave', validators=[DataRequired()])
	remember_me = BooleanField('Recordarme')
	submit = SubmitField('Iniciar Sesion')