SDET Task 2021
================

# Setup And Usage
1. Install mongodb
2. Install python 3.6+
3. Create virtual environment as documented [here](https://docs.python.org/3/library/venv.html)
4. Install dependencies: `./venv/bin/pip install -r requirements.txt`
5. Set mongo credentials at `src/db_adapter/DBAdapter.py`.
5. Run API server: `env FLASK_APP=src/API.py ./venv/bin/flask run`

# Routes
1. `GET localhost:5000/customers/_all`
   * Display a list of all customers ids
2. `GET localhost:5000/customers/<id>`, where id is customer id
   * Customer information.
3. `GET localhost:5000/films/_all`
   * Display a list of all the available films.
4. `GET localhost:5000/films/<id>`
   * Allow the user to select a film and get:
     - List of all customers who rented it in `customer_ids` field.
     - All the details of the film
    
