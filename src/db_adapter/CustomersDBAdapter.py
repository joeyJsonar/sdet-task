from .DBAdapter import DBAdapter


class CustomersDBAdapter(DBAdapter):
    def __init__(self):
        super(CustomersDBAdapter, self).__init__()
        self.collection = self.db.customers

    def get_all_ids(self):
        return [d['_id'] for d in self.collection.find({}, {"_id": 1})]

    def get_customer(self, id):
        return self.collection.find_one({"_id": id})
