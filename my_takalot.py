import config
import mongodb_api

def get_all_takalot_board(user):
    try:
        takalot = []
        custom_query = {"user":user,"status": { "$in":["1","2"]}}
        mongodb = mongodb_api.mongodb(config.mongodb_address, config.db_name, config.collection_name)
        connection = mongodb.mongo_get_connection()
        json = mongodb.mongo_search_document(connection, custom_query)
        for document in json:
            takalot.append(document)
            print(document)
        if takalot == []:
            print("אין תקלות פתוחות או בטיפול :)")
            return "אין תקלות פתוחות או בטיפול :)"
        else:
            return str(takalot)
    except Exception as e:
        print(e)
        return e