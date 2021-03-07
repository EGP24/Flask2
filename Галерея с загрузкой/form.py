from flask_wtf import FlaskForm
from wtforms import SubmitField, FileField


class MyForm(FlaskForm):
    image = FileField('Добавить картинку')
    submit = SubmitField('Войти')