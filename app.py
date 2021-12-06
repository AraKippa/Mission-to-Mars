from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping
app = Flask(__name__,template_folder='template')
# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)
#Define the route for the HTML page
@app.route("/")
#Function to find Mars in our Mongo db
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)
# Defines the route Flask will use
@app.route("/scrape")
#Defines what it will do while there
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
#Redirect after scrape to / to see the updated content
   return redirect('/', code=302)
#This line tells Flask to run
if __name__ == "__main__":
   app.run()
