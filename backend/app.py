import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv() # Load environment variables from .env file

MONGO_URI=os.getenv("MONGO_URI") 

client=MongoClient(MONGO_URI) # Create a new client instance
db=client["phishing_sim"] # Select the database

from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)

@app.route('/hello/') #Prints "Hello Stranger!"
@app.route('/hello/<name>') #Prints "Hello <name>!"
def hello(name=None):
    return render_template('hello.html', name=name)

with app.test_request_context():
    print(url_for('hello'))

if __name__ == "__main__":
    app.run(debug=True)