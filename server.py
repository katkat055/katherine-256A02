from flask import Flask, redirect, render_template, request, session, url_for
from CreateUser import CreateUser

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
    form = CreateUser()
    if request.method == "GET":
        return render_template("createuser.html", form=form)
    
    
if __name__ == "__main__":
    app.run(debug=True, port=8888)