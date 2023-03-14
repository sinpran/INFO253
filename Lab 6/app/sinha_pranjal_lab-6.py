from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@db:5432/27055041_db"
db = SQLAlchemy(app)

hashset = {'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'}

class Quotes(db.Model):
    day = db.Column(db.String(20), primary_key=True)
    quote = db.Column(db.String(1000))

    def to_dict(self):
        return {
            'day': self.day,
            'quote': self.quote
        }

@app.route("/")
@app.route("/<day>", methods=['GET'])
def get_by_id(day=None):
    if day == None:
        try:
            quotes = Quotes.query.all() # Queries all records in that model/table - SELECT *
            return jsonify([quote.to_dict() for quote in quotes]), 200
        except:
            return {}, 204
    day = day.lower().strip(" ")
    if day not in hashset:
        return {}, 400
    quote = Quotes.query.filter_by(day=day).first() # filter_by allows us to add filters to our Queries - SELECT * FROM cat WHERE ....
    if quote:
        return jsonify(quote.to_dict()), 200
    else:
        return jsonify({'error': 'Quote not found'}), 204

@app.route("/", methods=['POST'])
def add_quote():
    data = request.get_json()
    if 'day' not in data or 'quote' not in data:
        return {}, 400
    day = data.get('day')
    day = day.lower().strip(" ")
    if day not in hashset:
        return {}, 400
    new_quote = Quotes(day=day, quote=data['quote'])
    print(Quotes.query.filter_by(day=day))
    if Quotes.query.filter_by(day=day).first():
        return jsonify({'error': 'Quote already exists'}), 400
    db.session.add(new_quote) # Allows us to add/post new rows to the table
    db.session.commit() # Ensures that the data is actually written to the table - ACID properties anyone?
    return jsonify(new_quote.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)