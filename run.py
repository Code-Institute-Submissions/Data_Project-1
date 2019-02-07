import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://root:R00tUser@ds249128.mlab.com:49128/data_project"
app.config["MONGO_DBNAME"] = "data_project"

mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template("recipes.html", recipes = mongo.db.recipes.find())



if __name__ == '__main__':
    app.run(host = os.getenv('IP'), port = int(os.getenv('PORT')), debug = True)


