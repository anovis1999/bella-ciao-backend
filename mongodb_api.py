import pymongo


class Mongodb:
    def __init__(self, client_address, db_name, collection_name):
        self.client_address = client_address
        self.db_name = db_name
        self.collection_name = collection_name
        self.connection = None
        self.client = None

    def _connect_to_db(self):
        try:
            self.client = pymongo.MongoClient(self.client_address)
            db = self.client[self.db_name]
            self.connection = db[self.collection_name]

        except Exception as e:
            raise ValueError("there was an error connecting to the db. check the credentials. ", e)

    def mongo_insert_document(self, document):
        self._connect_to_db()
        if type(document) == list:
            inserted_file = self.connection.insert_many(document)
        else:
            inserted_file = self.connection.insert_one(document)
        self.client.close()
        return inserted_file

    def mongo_search_document(self, document):
        self._connect_to_db()
        searched_document = self.connection.find(document)
        self.client.close()
        return searched_document

    def mongo_delete_document(self, document):
        self._connect_to_db()
        deleted_document = self.connection.delete_one(document)
        self.client.close()
        return deleted_document

    def mongo_update_document(self, old_document, new_document):
        self._connect_to_db()
        new_document = {"$set": new_document}
        updated_document = self.connection.update_one(old_document, new_document)
        self.client.close()
        return updated_document
