from wtforms import DateField, FloatField, Form, IntegerField, RadioField, SelectField, StringField, SubmitField
from wtforms.validators import NumberRange

class PizzaOrder(Form):
    pizzatype = SelectField("Type", choices=["Canadian", "Cheese", "Hawaiian", "Meat Lovers", "Pepperoni", "Vegetarian"])
    crust = SelectField("Crust", choices=["Cauliflower", "Deep Dish", "Regular", "Thin Crust"])
    size = SelectField("Size", choices=["Individual", "Small", "Medium", "Large"])
    quantity = IntegerField("Quantity", validators=[NumberRange(min=1, max=10)])
    price = FloatField("Price")
    date = DateField("Date")
    submit = SubmitField("Submit")