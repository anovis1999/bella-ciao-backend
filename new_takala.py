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
        my_mongodb = mongodb_api.mongodb(config.mongodb_address, config.db_name, config.collection_name)
        conn = my_mongodb.mongo_get_connection()
        my_mongodb.mongo_insert_document(conn, jsonable_encoder(params))

        return True
    except Exception as e:
        print(e)
        return False
