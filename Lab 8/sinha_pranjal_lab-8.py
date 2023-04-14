from flask import Flask, request, Response, jsonify
import json
import pymongo

app = Flask(__name__)

hashset = {'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'}

def mongoConnection():
    try:
        # change your <username> and <password> below to connect to the database
        client = pymongo.MongoClient("mongodb+srv://<username>:<password>@<your clister ip>")
        db = client["test"] # Name of your database
        col = db["testCol"] # Name of your collection
        return col
    except:
        return Exception('Error connecting to DB')

@app.route("/<day>", methods=['GET'])
def get(day):
    try:
        col = mongoConnection()
    except:
        return {"error": "Error connecting to DB"}, 400
    day = day.lower()
    try:
        task = col.find_one({"day" : day})
        if task is None:
            return {}, 404
        return {task["day"] : task["quote"]}, 200
    except:
        return {"error": "Something went wrong"}, 400
    

@app.route("/", methods=['POST'])
def add_quote():
    try:
        col = mongoConnection()
    except:
        return {"error": "Error connecting to DB"}, 400
    
    try:
        params = request.get_json()
        day = params['day'].lower().strip()
        if day not in hashset:
            return {}, 400
        quote = params['quote']
        record = {
            "day" : day,
            "quote" : quote
        }
        try:
            res = col.insert_one(record)
            return {}, 201
        except:
            raise Exception('Insertion Failed')
    except:
        return {"error": "Something went wrong"}, 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)