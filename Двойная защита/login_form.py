from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    userID = StringField('ID астронавта', validators=[DataRequired()])
    user_password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    captainID = StringField('ID капитана', validators=[DataRequired()])
    captain_password = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Войти')