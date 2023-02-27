# Import the Flask module
from flask import Flask, request, Response, jsonify
import json

# Create a Flask application object
app = Flask(__name__)

# Define a route for the root URL
@app.route("/add/<num1>/<num2>", methods = ["GET"])
def add(num1, num2):
    try:
        answer = str(float(num1) + float(num2))
    except ValueError:
        answer = "Not a number"
    return jsonify({"answer" : [answer]})

@app.route("/sub", methods = ["POST"])
def sub():
    num1 = request.form.get('num1')
    num2 = request.form.get('num2')
    try:
        answer = str(float(num1) - float(num2))
    except ValueError:
        answer = "Not a number"
    return jsonify({"answer" : [answer]})

@app.route("/mul", methods = ["POST"])
def mul():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    try:
        answer = str(float(num1) * float(num2))
    except ValueError:
        answer = "Not a number"
    return jsonify({"answer" : [answer]})


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)