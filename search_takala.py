import config
import mongodb_api

def search_takala_in_mongo(id):
    mongodb = mongodb_api.mongodb(config.mongodb_address, config.db_name, config.collection_name)
    connection = mongodb.mongo_get_connection()
    json = mongodb.mongo_search_document(connection, {"id": str(id)})
    for doc in json:
        document = doc
        print(document)
    return str(document)