#import dependencies
#first we use flask to render a template, redirect it to another url, and create a URL 
#The second line says we'll use PyMongo to interact with our Mongo database.
#The third line says that to use the scraping code, we will convert from Jupyter notebook to Python.
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

#set up flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
# app.config["MONGO_URI"] tells Python that our app will connect to Mongo using a URI, a uniform 
# resource identifier similar to a URL.
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mars_app'
mongo = PyMongo(app)

# Define the route for the HTML page

@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

# Set up the scraping route.. will essentially be the button of the web application. its the one that will
#scrape updated data when we tell it to from the homepage of our web app 

@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scraping.scrape_all()
    mars.update_one({}, {"$set":mars_data}, upsert=True)
    return redirect('/', code=302)

# Tell flask to run 
if __name__ == '__main__':
    app.run()
    