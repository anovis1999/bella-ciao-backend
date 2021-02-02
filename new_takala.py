import hashlib
from fastapi.encoders import jsonable_encoder
import time
import mongodb_api
import config


def get_random_takala_id():
    hash = hashlib.sha1()
    hash.update(str(time.time()).encode("utf-8"))
    return hash.hexdigest()[:10]


def add_takala(params):
    try:
        my_mongodb = mongodb_api.Mongodb(config.mongodb_address, config.db_name, config.collection_name)
        my_mongodb.mongo_insert_document(jsonable_encoder(params))
        return "Successfully added."

    except Exception as e:
        print(e)
        return "could not add new takala! reason: " + str(e)


def update_messages(old_document, new_docunent):
    try:
        my_mongodb = mongodb_api.Mongodb(config.mongodb_address, config.db_name, config.collection_name)
        my_mongodb.mongo_update_document(old_document, new_docunent)
        return "successfully updated messages."
    except Exception as e:
        return "could not update messages!"
