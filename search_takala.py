import config
import mongodb_api


def search_takala_in_mongo(id):
    try:
        mongodb = mongodb_api.Mongodb(config.mongodb_address, config.db_name, config.collection_name)
        return mongodb.mongo_search_document({"id": str(id)})
    except Exception as e:
        print(e)
        return "מזהה התקלה שהכנסת אינו קיים"
