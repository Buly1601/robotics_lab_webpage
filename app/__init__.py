from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title="Página principal LA208", url=os.getenv("URL"))

@app.route("/admin",  methods=["POST","GET"])
def admin():
    """
    This section will be for admins.
    Admins will have the power to :
    - add / remove projects from the DB
    - have direct access to the student DB
    """
    if request.method == "GET":
        # render the template
        return render_template("admin.html", title="Administradores LA208", url=os.getenv("URL"))
    elif request.method == "POST":
        pass
    else:
        return "INVALID", 501
