from flask_wtf import Form
from wtforms import StringField, SelectField, TextAreaField, IntegerField, DateField, EmailField
from wtforms.validators import DataRequired, AnyOf, URL

class ItemForm(Form):
    username = StringField(
    )
    email = EmailField(
        "email", validators=[DataRequired()]
    )
    password = StringField(
        "password", validators=[DataRequired()]
    )
    title = StringField(
        "title", validators=[DataRequired()]
    )
    task = TextAreaField(
        'task', validators=[DataRequired()]
    )
    due_date = StringField(
        'due_date', validators=[DataRequired()]
    )