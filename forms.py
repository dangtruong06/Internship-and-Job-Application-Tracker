from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, DateField
from wtforms.validators import DataRequired, Email, Optional

# REGISTER FORM
class Register(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    name = StringField('Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

# LOGIN FORM
class Login(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])   

# JOB FORM
class AddJob(FlaskForm):
    company = StringField('Company', validators=[DataRequired()])
    role = StringField('Role', validators=[DataRequired()])
    status = SelectField('Status', choices=[('Interview', 'Interview'), 
                                            ('Rejected', 'Rejected'), 
                                            ('Screen', 'Phone Screen'),
                                            ('Applied', 'Applied')],
                                            validators=[DataRequired()])
    url = StringField('URL', validators=[DataRequired()])
    notes = StringField('Notes', validators=[Optional()])
    date = DateField('Applied On', validators=[Optional()])

