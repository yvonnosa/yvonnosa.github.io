# views.py

from flask import render_template

from app import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/create')
def create():
    return render_template("create.html")

@app.route('/view')
def view():
    return render_template("view.html")

    
@app.route('/edit')
def edit():
    return render_template("edit.html")
    
  







    