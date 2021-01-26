import pymongo

class mongodb:
    def __init__(self,client_address,db_name,collection_name):
        self.client_address=client_address
        self.db_name=db_name
        self.collection_name=collection_name

    def mongo_get_connection(self):
        try:
            client = pymongo.MongoClient(self.client_address)
            db = client[self.db_name]
            connection = db[self.collection_name]
        except Exception as e:
            print(e)
            return e
        return connection

    def mongo_insert_single_document(self,connection,document):
        try:
            inserted_file = connection.insert_one(document)
        except Exception as e:
            print(e)
            return e
        return inserted_file

    def mongo_search_document(self,connection,document):
        try:
            searched_document = connection.find(document)
        except Exception as e:
            print(e)
            return e
        return searched_document

    def mongo_delete_document(self,connection,document):
        try:
            deleted_document = connection.delete_one(document)
        except Exception as e:
            print(e)
            return e
        return deleted_document

    def mongo_update_document(self,connection,old_document,new_document):
        try:
            new_document = {"$set":new_document}
            updated_document = connection.update_one(old_document,new_document)
        except Exception as e:
            print(e)
            return e
        return updated_document


# json = {"id":"12341244"}

#example how to get connection#

# base_con = mongodb("mongodb://localhost:27017/","bella-ciao","takalot")
# con = base_con.mongo_get_connection()

#example how to index#

# x = base_con.mongo_insert_single_document(con,json)
# print(x)

#example how to search and read from mongo#

# x = base_con.mongo_search_document(con,json)
# for doc in x:
#     print(doc)

# x = base_con.mongo_update_document(con,json,{"id":"12345"})
# print(x)
