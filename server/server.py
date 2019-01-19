import os

from flask import Flask

os.environ['FLASK_DEBUG'] = "1" # DO NOT USE IN PRODUCTION

app = Flask(__name__)

@app.route("/hello/")
def hello():
    return "Hello World!"

@app.route("/test/")
def test():
    return "test"

if __name__ == '__main__':
    app.run()