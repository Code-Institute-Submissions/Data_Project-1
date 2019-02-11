import os
import env
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = os.getenv("SECRET", "secret123string")
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["MONGO_DBNAME"] = os.getenv("MONGO_DBNAME")

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
    return render_template("search.html", categories = mongo.db.categories.find())

@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html")
    
@app.route('/insert_recipe', methods = ["POST"])
def insert_recipe():
    ingredientsList = []
    ingredientItems = request.form.getlist("ingredient_name")
    ingredientQty = request.form.getlist("quantity")
    i = 0
    while i < len(ingredientItems):
        ingredient = {"ingredient_name": ingredientItems[i], "quantity": ingredientQty[i]}
        ingredientsList.append(ingredient)
        i +=1
    if request.form.get("allergens") == "on":
        allergens = True
        allergen_name = request.form["allergen_name"]
    else:
        allergens = False
        allergen_name = ""
    new_recipe = {
        "recipe_name": request.form["recipe_name"],
        "style_name": request.form["style_name"],
        "author_name": request.form["author_name"],
        "ingredients": ingredientsList,
        "instructions": request.form["instructions"],
        "allergens": allergens,
        "allergen_name": allergen_name,
        "views": "0"
    }
    mongo.db.recipes.insert_one(new_recipe)
    return redirect(url_for("search"))
      
@app.route('/recipe')
def recipe():
    """Display an individual recipe"""
    selected = mongo.db.recipes.find_one({"recipe_name": "test recipe"})
    return render_template("recipes.html", recipe = selected)

@app.route('/logout')
def logout():
    """Log player out of CookBook and return to sign in page"""
    session.pop("username", None)
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(host = os.getenv('IP'), port = int(os.getenv('PORT')), debug = True)
    