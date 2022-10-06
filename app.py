# importing librearies to use when making the db connection and building the API
from audioop import add
from cProfile import run
from flask import Flask, request
from dbhelpers import run_statement
import json

# calling the Flask function which will return a value that I will be used for my API
app = Flask(__name__)

@app.post('/api/restaurant')
def add_restaurant():
    name = request.json.get('name')
    address = request.json.get('address')
    phone_num = request.json.get('phone_num')
    image_url = request.json.get('image_url')

    id = run_statement('CALL insert_restaurant(?,?,?,?)',[name, address, phone_num, image_url])

    if(type(id) == list):
        id_json = json.dumps(id, default=str)
        return id_json
    else:
        return "Sorry."

@app.get('/api/restaurant')
def get_all_restaurants():
    restaurants = run_statement("CALL get_all_restaurants()")
    if(type(restaurants) == list):
        restaurants_json = json.dumps(restaurants, default=str)
        return restaurants_json
    else:
        return "Sorry, something has gone wrong."

@app.delete('/api/restaurant')
def delete_restaurant():
    id = request.json.get('id')

    id = run_statement('CALL delete_restaurant(?)',[id])

    if(type(id) == list):
        id_json = json.dumps(id, default=str)
        return id_json
    else:
        return "Sorry."

# starting our application flask server with debug mode turned on
app.run(debug=True)