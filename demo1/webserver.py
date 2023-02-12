from flask import Flask
import json

app = Flask(__name__)

quote_db = {
  'sunday': "Life is about making an impact, not making an income. \
  –Kevin Kruse",
  'monday': "Whatever the mind of man can conceive and believe, it can achieve. \
  –Napoleon Hill",
  'tuesday': "Strive not to be a success, but rather to be of value. \
  –Albert Einstein",
  'wednesday': "You miss 100% of the shots you don’t take. \
  –Wayne Gretzky",
  'thursday': "Every strike brings me closer to the next home run. \
  –Babe Ruth",
  'friday': "We become what we think about. \
  –Earl Nightingale",
  'saturday': "Life is what happens to you while you’re busy making other plans. \
  –John Lennon",
}

@app.route('/quote/<day_of_week>')
def quote_of_the_day(day_of_week):
  response = {"day": day_of_week, "quote": quote_db[day_of_week.lower()]}

  return json.dumps(response)