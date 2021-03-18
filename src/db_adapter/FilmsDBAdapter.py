from .DBAdapter import DBAdapter
from .CustomersDBAdapter import CustomersDBAdapter

class FilmsDBAdapter(DBAdapter):
    def __init__(self):
        super(FilmsDBAdapter, self).__init__()
        self.collection = self.db.films

    def get_all(self):
        return list(
            self.collection.find({}, {"Title": 1, "Category": 1, "Description": 1, "Rating": 1, "Rental Duration": 1})
        )

    def get_film(self, id):
        film = self.collection.find_one({"_id": id})
        customers = CustomersDBAdapter()
        customer_ids_cursor = customers.collection.aggregate([
            {
                "$unwind": "$Rentals"
            },
            {
                "$match": {
                    "Rentals.filmId": id
                }
            },
            {
                "$group": {
                    "_id": "$_id"
                }
            }
        ])
        customer_ids = [d['_id'] for d in customer_ids_cursor]

        film['customer_ids'] = customer_ids
        return film
