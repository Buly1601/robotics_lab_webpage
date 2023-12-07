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


@app.route("/projects", methods=["POST", "GET"])
def projects():
    """
    This section will host projects made in the lab.
    Each project will be modified only by the admin.
    TODO
    - database
    """
    items = [
        {
            'image': './static/img/admin_logo.jpg',
            'alt': 'Norway',
            'title': 'Lorem Ipsum',
            'description': '1Praesent tincidunt sed tellus ut rutrum. Sed vitae justo condimentum, porta lectus vitae, ultricies congue gravida diam non fringilla.'
        },
        {
            'image': './static/img/admin_logo.jpg',
            'alt': 'Norway',
            'title': 'Lorem Ipsum',
            'description': '2Praesent tincidunt sed tellus ut rutrum. Sed vitae justo condimentum, porta lectus vitae, ultricies congue gravida diam non fringilla.'
        },
        {
            'image': './static/img/admin_logo.jpg',
            'alt': 'Norway',
            'title': 'Lorem Ipsum',
            'description': '3Praesent tincidunt sed tellus ut rutrum. Sed vitae justo condimentum, porta lectus vitae, ultricies congue gravida diam non fringilla.'
        },
        {
            'image': './static/img/admin_logo.jpg',
            'alt': 'Norway',
            'title': 'Lorem Ipsum',
            'description': '1Praesent tincidunt sed tellus ut rutrum. Sed vitae justo condimentum, porta lectus vitae, ultricies congue gravida diam non fringilla.'
        },
        {
            'image': './static/img/admin_logo.jpg',
            'alt': 'Norway',
            'title': 'Lorem Ipsum',
            'description': '2Praesent tincidunt sed tellus ut rutrum. Sed vitae justo condimentum, porta lectus vitae, ultricies congue gravida diam non fringilla.'
        },
        {
            'image': './static/img/admin_logo.jpg',
            'alt': 'Norway',
            'title': 'Lorem Ipsum',
            'description': '3Praesent tincidunt sed tellus ut rutrum. Sed vitae justo condimentum, porta lectus vitae, ultricies congue gravida diam non fringilla.'
        }
    ]
    
    if request.method == "GET":
        return render_template("projects.html", title="Poyectos realizados en el laboratorio", url=os.getenv("URL"), items=items)
    