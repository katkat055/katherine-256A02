import json
import os
from flask import Flask, redirect, render_template, request, session, url_for
from CreateUser import CreateUser
from PizzaOrder import PizzaOrder

app = Flask(__name__)
app.secret_key = "cat"


def check_login(email, password):
    with open("./data/users.json", "r") as file:
        users = json.load(file)
    for user in users:
        if user["email"] == email and user["password"] == password:
            return True
    return False


def sort_by_date(order):
    return order["date"]


@app.route("/")
def home():
    # if "login" not in session:
    #     return redirect(url_for("login"))
    if (
        os.path.exists("./data/pizzaorders.json")
        and os.path.getsize("./data/pizzaorders.json") > 0
    ):
        with open("./data/pizzaorders.json") as file:
            orders = json.load(file)
            orders_sorted = sorted(orders, key=sort_by_date)
            return render_template("sortedorders.html", orders=orders_sorted)
    return "Server up and running"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        if check_login(email, password):
            session["login"] = "login"
            session["email"] = email
            return redirect(url_for("home"))
        else:
            return redirect(url_for("login"))


@app.route("/create", methods=["GET", "POST"])
def create():
    form = CreateUser()
    if request.method == "GET":
        return render_template("createuser.html", form=form)
    if request.method == "POST":
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        role = request.form.get("role")

        users = []
        new_id = 1
        if (
            os.path.exists("./data/users.json")
            and os.path.getsize("./data/users.json") > 0
        ):
            with open("./data/users.json", "r") as file:
                users = json.load(file)
            max_id = max(users, key=lambda x: x.get("id", 0)).get("id", 0)
            new_id = max_id + 1
        if password1 == password2:
            user_info = {
                "id": new_id,
                "email": email,
                "password": password1,
                "role": role,
            }
            users.append(user_info)
        else:
            message = "Passwords need to match"
            return render_template("createuser.html", form=form, alert=message)

        with open("./data/users.json", "w") as file:
            json.dump(users, file, indent=4)
        return redirect(url_for("home"))


@app.route("/pizza", methods=["GET", "POST"])
def pizza():
    # if "login" not in session:
    #     return redirect(url_for("login"))
    form = PizzaOrder()
    if request.method == "GET":
        return render_template("pizzaorder.html", form=form)
    if request.method == "POST":
        pizzatype = request.form.get("pizzatype")
        crust = request.form.get("crust")
        size = request.form.get("size")
        quantity = request.form.get("quantity")
        price = request.form.get("price")
        date = request.form.get("date")

        orders = []
        pizza_id = 1
        if (
            os.path.exists("./data/pizzaorders.json")
            and os.path.getsize("./data/pizzaorders.json") > 0
        ):
            with open("./data/pizzaorders.json", "r") as file:
                orders = json.load(file)
            max_id = max(orders, key=lambda x: x["id"])["id"]
            pizza_id = max_id + 1
        order_info = {
            "id": pizza_id,
            "pizzatype": pizzatype,
            "crust": crust,
            "size": size,
            "quantity": quantity,
            "price": price,
            "date": date,
        }
        orders.append(order_info)
        with open("./data/pizzaorders.json", "w") as file:
            json.dump(orders, file, indent=4)
        return redirect(url_for("home"))


@app.route("/pizza/<int:id>", methods=["GET", "POST", "DELETE"])
def get_pizza(id):
    # if "login" not in session:
    #     return redirect(url_for("login"))
    form = PizzaOrder()
    if request.method == "GET":
        with open("./data/pizzaorders.json") as file:
            orders = json.load(file)
            for order in orders:
                if order["id"] == id:
                    return render_template("order.html", form=form, order=order)
            return redirect(url_for("home"))
    if request.method == "POST":
        with open("./data/pizzaorders.json", "r") as file:
            orders = json.load(file)
            for order in orders:
                if order["id"] == id:
                    order["date"] = request.form["date"]
                    order["pizzatype"] = request.form["pizzatype"]
                    order["crust"] = request.form["crust"]
                    order["size"] = request.form["size"]
                    order["quantity"] = request.form["quantity"]
                    order["price"] = request.form["price"]
                    with open("./data/pizzaorders.json", "w") as file:
                        file.seek(0)
                        json.dump(orders, file, indent=4)
                        file.truncate()
                        return redirect(url_for("home"))
    if request.method == "DELETE":
        with open("./data/pizzaorders.json") as file:
            orders = json.load(file)
            for order in orders:
                if order["id"] == id:
                    orders.remove(order)
                    with open("./data/pizzaorders.json", "w") as file:
                        json.dump(orders, file, indent=4)
                    return redirect(url_for("home"))


@app.route("/logout/")
def logout():
    if "login" in session:
        session.pop("login")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True, port=8888)
