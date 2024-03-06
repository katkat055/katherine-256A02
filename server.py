import json
import os
from flask import Flask, redirect, render_template, request, session, url_for
from CreateUser import CreateUser
from PizzaOrder import PizzaOrder

app = Flask(__name__)

def check_login(email, password):
    return email and password

@app.route("/")
def server_status():
    return "Server is up and running"

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
        else:
            return redirect(url_for("login"))
        
@app.route("/create", methods=["GET", "POST"])
def create():
    # if "login" not in session:
    #     return redirect(url_for("login"))
    form = CreateUser()
    if request.method == "GET":
        return render_template("createuser.html", form=form)
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        role = request.form.get("role")
        
        users = []
        new_id = 0
        if os.path.exists("./data/users.json") and os.path.getsize("./data/users.json") > 0:
            with open("./data/users.json", "r") as file:
                users = json.load(file)
            max_id = max(users, key=lambda x: x["id"])["id"]
            new_id = max_id + 1
        user_info = {
            "id": new_id,
            "email": email,
            "password": password,
            "role": role
        }
        users.append(user_info)
        with open("./data/users.json", "w") as file:
            json.dump(users, file, indent=4)
        return "User Added"
    
@app.route("/pizza", methods=["GET", "POST"])
def pizza():
    # if "login" not in session:
    #     return redirect(url_for("login"))
    form = PizzaOrder()
    if request.method == "GET":
        return render_template("pizzaorder.html", form=form)
    
@app.route("/logout/")
def logout():
    if "login" in session:
        session.pop("login")
    return redirect(url_for("login"))
    
if __name__ == "__main__":
    app.run(debug=True, port=8888)