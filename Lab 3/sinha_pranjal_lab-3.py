from flask import Flask, request, Response, jsonify
import json

app = Flask(__name__)

hashset = {'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'}

def get_data_from_file():
    file = open('quotes.json')
    data = json.load(file)
    file.close()
    return data

def get_result(day, quotes=None):
    if quotes is None:
        quotes = get_data_from_file()
    if day is not None:
        result = {key: value for key, value in quotes.items()
                  if key == day}
    else:
        return jsonify({
            "error": "Invalid Request - No Day Parameter"
        }), 400
    if result == {}:
        return {}, 204
    return jsonify(result), 200

@app.route("/")
def get_all():
    data = get_data_from_file()
    if data == {}:
        return {}, 204
    return jsonify(data), 200

@app.route("/<day>", methods=['GET'])
def get_by_id(day):
    if day == None:
        return {}, 400
    day = day.lower()
    day = " ".join(day.split())
    if day not in hashset:
        return {}, 400
    return get_result(day)

@app.route("/", methods=['POST'])
def add_quote():
    data = request.get_json()
    if 'day' not in data or 'quote' not in data:
        return {}, 400
    day = data.get('day').lower()
    day = " ".join(day.split())
    if day not in hashset:
        return {}, 400
    quote = data.get('quote')
    quote = " ".join(quote.split())
    quote_data = get_data_from_file()
    if day in quote_data:
        return {}, 400
    quote_data[day] = quote
    with open('quotes.json', 'w') as f:
        json.dump(quote_data, f)
    return jsonify({
        day : quote
    }), 201

@app.route("/<day>", methods=["PUT", "DELETE"])
def update(day):
    statusCode = 400
    if day == None:
        return {}, statusCode
    day = day.lower()
    day = " ".join(day.split())
    if day not in hashset:
            return {}, statusCode
    quote_data = get_data_from_file()
    if request.method == "PUT":
        if day in quote_data:
            statusCode = 200
        else:
            statusCode = 201
        quote = request.get_json().get("quote", "invalid")
        if quote == "invalid":
            return {}, 400
        quote = " ".join(quote.split())
        quote_data[day] = quote
        with open("quotes.json", "w") as f:
            json.dump(quote_data, f)
        return jsonify({
            day : quote
        }), statusCode
    if request.method == "DELETE":
        if day in quote_data:
            statusCode = 200
        else:
            return {}, 404
        del quote_data[day]
        with open("quotes.json", "w") as f:
            json.dump(quote_data, f)
        return {}, statusCode

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)