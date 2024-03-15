import json
from wtforms import (
    DateField,
    FloatField,
    Form,
    IntegerField,
    SelectField,
    SubmitField,
)
from wtforms.validators import NumberRange

with open("./data/init.json") as file:
    options = json.load(file)


class PizzaOrder(Form):
    pizzatype = SelectField("Type", choices=options["type"])
    crust = SelectField("Crust", choices=options["crust"])
    size = SelectField("Size", choices=options["size"])
    quantity = IntegerField("Quantity", validators=[NumberRange(min=1, max=10)])
    price = FloatField("Price")
    date = DateField("Date")
    submit = SubmitField("Submit")
