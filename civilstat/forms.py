from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Length


class RegistrationForm(FlaskForm):
    firstname = StringField("Firstname", validators=[DataRequired(), Length(min=1, max=128)])
    middlename = StringField("Middlename", validators=[Length(min=1, max=128)])
    lastname = StringField("Lastname", validators=[DataRequired(), Length(min=1, max=128)])
    suffix = StringField("Suffix", validators=[Length(min=2, max=4)])
    sex = SelectField("Sex", choices=[("Female", "female"), ("Male", "male")], validators=[DataRequired()])
    submit = SubmitField("Submit")