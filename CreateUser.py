from wtforms import Form, RadioField, StringField, SubmitField
from wtforms import validators

class CreateUser(Form):
    email = StringField("Email",[validators.Email("Please enter your email")])
    password1 = StringField("Password",[validators.InputRequired("Enter your password")])
    password2 = StringField("Renter Password",[validators.InputRequired("Renter your password")])
    role = RadioField("Role", choices=[("C", "Customer"), ("S", "Staff")])
    submit = SubmitField("Submit")