import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv() # Load environment variables from .env file

MONGO_URI = os.getenv("MONGO_URI") 

client = MongoClient(MONGO_URI) # Create a new client instance
db = client["phishing_sim"] # Select the database

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/log-click', methods=['GET','POST'])
def log_click():
    data = request.json
    email = data.get("email")
    collection = db["emails"]
    if email:
        collection.insert_one({"email" : email})
        return jsonify({"message" : "Email collected successfully"}) , 201
    else:
        return jsonify({"error" : "Email is required"}), 400



if __name__ == "__main__":
    app.run(debug=True)