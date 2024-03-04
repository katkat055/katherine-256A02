from wtforms import Form, RadioField, StringField, SubmitField
from wtforms import validators

class CreateUser(Form):
    email = StringField("Email",[validators.Email("Please enter your email")])
    password = StringField("Password",[validators.InputRequired("Enter your password")])
    role = RadioField("Role", choices=[("C", "Customer"), ("S", "Staff")])
    submit = SubmitField("Submit")