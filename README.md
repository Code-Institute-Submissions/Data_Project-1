# Data Centric Development Project

## An Online CookBook

The online CookBook application requires users to log in individually to access the recipes on the database. On successful log in,
the user is presented with a search page with drop-down menus so a search can be refined using the set criteria of cuisine-style,
author of the recipe, ingredients and allergens. The results of the search are displayed in a table format, ordered by the number
of views each recipe has received. An individual recipe can be chosen from the table and full details displayed to the user.
The user has options to add a new recipe to the database, as well as updating or deleting existing recipes on the database.

Wireframes for this application can be accessed [here](/Data-Project-wireframes.pdf)

### Technologies Used

[HMTL5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
   * Used to define the web application.

[Materialize CSS](http://archives.materializecss.com/0.100.2/)
   * A modern responsive front-end framework based on Material Design, used to apply styles and
      colours to, and provide a responsive layout for the web application.

[jQuery](https://jquery.com/)
   * Javascript library used to target specific HTML elements with javascript functions.

[Python](https://www.python.org/)
   * Used to code the application's logic and data processing needs.

[Flask](http://flask.pocoo.org/)
   * A web framework used with Python programming language.

[MongoDB](https://www.mongodb.com/)
   * An open-source, non-relational, document-oriented database to store all the recipes for the application.

### Testing

__Manual Testing__

Upon loading the CookBook application, the user is, initially, presented with a Welcome / Sign in page, where they are invited
to log in to access the main application. A test is performed to ensure log in is not possible if the name entry field is left blank.
Successful log in results in the main search page of the application being displayed, with a personalised greeting, using the name provided by 
the user at log in.

The Search page has drop-down menus and three option buttons presented to the user.
    1. The Find Recipe button will return a list of all the recipes contained in the database displayed on the Results page.
    This list can be refined by the user, with selection(s) being made from the drop-down menus supplied for cuisine-style, author of the recipe,
    ingredients and allergens.
    2. The Add Recipe button directs the user to a form, with which the user can add a recipe of their choosing to the database. The input 
    fields for the form are tested to ensure they cannot be left blank and in the case of the ingredients list, any blank entries are 
    processed in the Python code so as not to added to the database. The instructions for the recipe are converted to a json string for
    storage in the database. The allergen fields are processed in the Python code so they can be correctly added to the database. A check is 
    made on the search criteria of cuisine-style, author, ingredients and allergens and if they do not exist in the database, then they are
    added at this time so the drop-down menus for searching for recipes remain up to date allowing recipes to be found. The MongoDB
    database used for this project is provided by https://mlab.com/, which allows easy checking of the correct addition of test recipes
    from the Add Recipe form. A message is diplayed to indicate the successful addition of a recipe to the database.
    3. The Sign Out button clears the name provided by the user at log in from the session cookie and returns the user back to the Welcome /
    Sign in page.
    
The Results page displays the results of the search for a recipe made by the user. The results are displayed in a table format, ranked in 
order of the number of views each recipe has received, thus placing the most viewed, most popular recipes at the top of ths list. Each 
individual recipe can be selected to view full details of that recipe on the Recipe page. A New Search button directs the user back to the Search
page, where the user can start a new search with different criteria, add a recipe or sign out of the application all together.

The Recipe page displays full details of the chosen recipe, as requested by the user. Three option buttons are presented to the user.
    1. The Edit Recipe button directs the user to the form used to add a recipe, populated with the current recipe's details and allows the user
    to change any fields that the user feels will improve the current recipe. Testing is performed by selecting a test recipe added previously,
    changing, or adding extra fields, and checking the correct update has taken place on https://mlab.com/. A message is displayed to indicate 
    the successful update of the chosen recipe.
    2. The Delete Recipe button allows the user to remove the chosen recipe from the database. Testing is performed by deleting a test recipe
    and checking the recipe has been removed from the database on https://mlab.com/. A message is diplayed to indicate the successful removal
    of the recipe from the database.
    3. The Back to Results button returns the user to the previous results page, where a different recipe can be chosen or a new search 
    performed.
    
__Automated Testing__

Tests have been written to prove the correct operation of the Flask views and routes. Typing 'python3 tests.py' in the command line
runs the tests.

### Deployment

The CookBook application is deployed on Heroku here https://gd-cookbook.herokuapp.com/
    