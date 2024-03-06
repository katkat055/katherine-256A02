from wtforms import DateField, FloatField, Form, IntegerField, RadioField, SelectField, StringField, SubmitField
from wtforms.validators import NumberRange

class PizzaOrder(Form):
    pizzatype = SelectField("Type", choices=[("Cheese"), ("Pepperoni"), ("Vegetarian"), ("Hawaiian")])
    crust = SelectField("Crust", choices=[("Regular"), ("Thin"), ("Cheese")])
    size = SelectField("Size", choices=[("S", "Small"), ("M", "Medium"), ("L", "Large")])
    quantity = IntegerField("Quantity", validators=[NumberRange(min=1, max=10)])
    price = FloatField("Price")
    date = DateField("Date")
    submit = SubmitField("Submit")