import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo

app = Flask(__name__)
app.secret_key = os.getenv("SECRET", "secret123string")
app.config["MONGO_URI"] = "mongodb://root:R00tUser@ds249128.mlab.com:49128/data_project"
app.config["MONGO_DBNAME"] = "data_project"

mongo = PyMongo(app)

@app.route('/', methods = ["GET", "POST"])
def index():
    """Welcome / Sign in page"""
    if request.method == "POST":
        session["username"] = request.form["username"]
    if "username" in session:
        return redirect(url_for("search", username = session["username"]))
    return render_template("index.html")
    
@app.route('/search')
def search():
    return render_template("search.html")
    
@app.route('/recipe')
def recipe():
    """Display an individual recipe"""
    return render_template("recipes.html", recipes = mongo.db.recipes.find())


if __name__ == '__main__':
    app.run(host = os.getenv('IP'), port = int(os.getenv('PORT')), debug = True)


