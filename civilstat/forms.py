from flask_wtf import FlaskForm
from wtforms import RadioField, StringField, SubmitField
from wtforms.validators import DataRequired, Length


class RegistrationForm(FlaskForm):
    sex_choices = [("Female", "female"), ("Male", "male")]
    maristat_choices = [("Single", "single"), ("Married", "married"), ("Widowed", "widowed")]

    firstname = StringField("Firstname", validators=[DataRequired(), Length(min=1, max=128)])
    middlename = StringField("Middlename", validators=[Length(min=1, max=128)])
    lastname = StringField("Lastname", validators=[DataRequired(), Length(min=1, max=128)])
    suffix = StringField("Suffix", validators=[Length(min=2, max=4)])

    sex = RadioField("Sex", choices=sex_choices, validators=[DataRequired()])
    marital_status = RadioField("Sex", choices=maristat_choices, validators=[DataRequired()])
    submit = SubmitField("Submit")