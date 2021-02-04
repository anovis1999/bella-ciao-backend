import mongodb_api
import config
from fastapi.encoders import jsonable_encoder


def check_user_exists(user_name):
    mongo = mongodb_api.Mongodb(config.mongodb_address, config.db_name, config.clients_collection_name)
    exists = False
    try:
        print(mongo.mongo_search_document({"user_name": user_name})[0])
        exists = True
    finally:
        return exists


def add_new_user(user_data):
    my_mongodb = mongodb_api.Mongodb(config.mongodb_address, config.db_name, config.clients_collection_name)
    try:
        my_mongodb.mongo_insert_document(jsonable_encoder(user_data))
        return "Successfully added."
    except Exception as e:
        print(e)
        return "could not add new takala! reason: " + str(e)


def get_user(user_name):
    mongo = mongodb_api.Mongodb(config.mongodb_address, config.db_name, config.clients_collection_name)
    try:
        user_data = mongo.mongo_search_document({"user_name": user_name})[0]
        print(user_data)
        user_data.pop("_id")
        return user_data
    except Exception as e:
        print(e)
        return "user not exists!"
