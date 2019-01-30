import os

from flask import Flask
from flask import render_template
from flask_pymongo import PyMongo

os.environ['FLASK_DEBUG'] = "1" # DO NOT USE IN PRODUCTION

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/dev_data"
mongo = PyMongo(app)

@app.route("/hello/")
def hello():
    import datetime
    post = {"author": "Ryan",
         "text": "This is a test of the server's post system",
         "tags": ["mongodb", "python", "pymongo"],
         "date": datetime.datetime.utcnow()}
    posts = mongo.db.data
    posts.insert_one(post)
    return "Hello World!"

@app.route("/test/")
def test():
    return "test"

@app.route("/data/first/")
def getFirst():
    dataFirst = mongo.db.data.find_one()
    return dataFirst["name"]

@app.route("/data/")
def home_page():
    online_users = mongo.db.data
    return render_template("user.html",
        online_users=online_users)

if __name__ == '__main__':
    app.run()

    # i am a comment