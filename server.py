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