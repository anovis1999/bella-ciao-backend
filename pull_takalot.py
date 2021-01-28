import config
import mongodb_api


#takalot per user
def get_all_takalot_board(user):
    try:
        takalot = []
        custom_user_query = {"user":user,"status": { "$in":["1","2"]}}
        mongodb = mongodb_api.mongodb(config.mongodb_address, config.db_name, config.collection_name)
        connection = mongodb.mongo_get_connection()
        json = mongodb.mongo_search_document(connection, custom_user_query)
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

#takalot per team
def get_all_team_takalot(team):
    try:
        takalot = []
        custom_team_query = {"team": team, "status": {"$in": ["1", "2"]}}
        mongodb = mongodb_api.mongodb(config.mongodb_address, config.db_name, config.collection_name)
        connection = mongodb.mongo_get_connection()
        json = mongodb.mongo_search_document(connection, custom_team_query)
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