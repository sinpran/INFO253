# Import the Flask module
from flask import Flask

# Create a Flask application object
app = Flask(__name__)

# Define a route for the root URL
@app.route("/add/<num1>/<num2>", methods = ["GET"])
def add(num1, num2):
    try:
        return str(float(num1) + float(num2))
    except ValueError:
        return "Not a number"

@app.route("/sub/<num1>/<num2>", methods = ["GET"])
def sub(num1, num2):
    try:
        return str(float(num1) - float(num2))
    except ValueError:
        return "Not a number"

@app.route("/mul/<num1>/<num2>", methods = ["POST"])
def mul(num1, num2):
    try:
        return str(float(num1) * float(num2))
    except ValueError:
        return "Not a number"

@app.route("/div/<num1>/<num2>", methods = ["POST"])
def div(num1, num2):
    try:
        return str(float(num1) / float(num2))
    except ValueError:
        return "Not a number"
    except ZeroDivisionError:
        return "Can't divide by ZERO"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)