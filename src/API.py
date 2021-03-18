from flask import Flask, jsonify

from .db_adapter.CustomersDBAdapter import CustomersDBAdapter
from .db_adapter.FilmsDBAdapter import FilmsDBAdapter

app = Flask(__name__)


# 1. Display a list of all customers
@app.route("/customers/_all")
def get_all_customer_ids():
    customers = CustomersDBAdapter()
    return jsonify(customers.get_all_ids())


# 2. Customer information. Covers both 2.a and 2.b.
@app.route("/customers/<int:id>")
def get_customer(id):
    customers = CustomersDBAdapter()
    return jsonify(customers.get_customer(id))


# 3. Display a list of all the available films, with the next information
@app.route("/films/_all")
def get_all_films():
    films = FilmsDBAdapter()
    return jsonify(films.get_all())


# 4. Allow the user to select a film and get:
#   List of all customers who rented it
#   All the details of the film
@app.route("/films/<int:id>")
def get_film(id):
    films = FilmsDBAdapter()
    return jsonify(films.get_film(id))
