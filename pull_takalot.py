import config
import mongodb_api


def get_takala(takala_id):
    try:
        mongo_connection = mongodb_api.Mongodb(config.mongodb_address, config.db_name, config.collection_name)
    except Exception as e:
        print(str(e))
        return str(e)
    return mongo_connection.mongo_search_document({"takala_id": takala_id})[0]


# takalot per user
def get_all_takalot_board(user):
    try:
        takalot = []
        custom_user_query = {"compUser": user}
        mongodb = mongodb_api.Mongodb(config.mongodb_address, config.db_name, config.collection_name)
        json = mongodb.mongo_search_document(custom_user_query)
        print(json)
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


# takalot per team
def get_all_team_takalot(team):
    try:
        takalot = []
        custom_team_query = {"team": team, "status": {"$in": ["1", "2"]}}
        mongodb = mongodb_api.Mongodb(config.mongodb_address, config.db_name, config.collection_name)
        json = mongodb.mongo_search_document(custom_team_query)
        for document in json:
            takalot.append(document)
            print(document)
        if takalot == []:
            print("אין תקלות פתוחות או בטיפול עבור הצוות :)")
            return "אין תקלות פתוחות או בטיפול עבור הצוות :)"
        else:
            return str(takalot)

    except Exception as e:
        print(e)
        return e
