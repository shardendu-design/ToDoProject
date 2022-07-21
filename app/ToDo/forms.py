# import all the necessary library


from wtforms.fields.core import DateField, IntegerField, SelectField
from app.ToDo.models import ToDos
from flask_wtf import FlaskForm, form
from wtforms import StringField, TextField, SubmitField, PasswordField, BooleanField,validators
from wtforms.validators import DataRequired, InputRequired, Length, Email, EqualTo, URL, ValidationError,Optional,Regexp
from datetime import datetime, date

#  create todo form


class CreateToDo(FlaskForm):
    today = date.today()
    todo_name = StringField('ToDo Name', render_kw={'autofocus': True}, validators=[DataRequired()])
    todo_description = StringField('ToDo Description',validators=[DataRequired()])
    todo_created_date = DateField('ToDo Created Date',default=today,validators=[DataRequired()])
    todo_status = SelectField('Status Type',choices=['','NotStarted','OnGoing','Completed'],validators=[DataRequired()])

 # edit todo form


class EditToDoForm(FlaskForm):
    todo_name = StringField('ToDo Name', render_kw={'autofocus': True}, validators=[DataRequired()])
    todo_description = StringField('ToDo Description', validators=[DataRequired()])
    todo_created_date = DateField('ToDo Created Date', validators=[DataRequired()])
    todo_status = SelectField('Status Type', choices=['', 'NotStarted', 'OnGoing', 'Completed'],validators=[DataRequired()])
    submit = SubmitField('Update')

    