import config
import mongodb_api


def change_takala_status(takala_id, wanted_status, current_status):
    try:
        old_takala = {"id": takala_id, "status": config.status[current_status]}
        new_takala = {"id": takala_id, "status": config.status[wanted_status]}

        mongodb = mongodb_api.mongodb(config.mongodb_address, config.db_name, config.collection_name)
        connection = mongodb.mongo_get_connection()
        json = mongodb.mongo_update_document(connection, old_takala, new_takala)
        return "סטטוס התקלה השתנה מ: {0} ל {1}".format(current_status,wanted_status)
    except Exception as e:
        print(e)
        return e