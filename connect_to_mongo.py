from pymongo import MongoClient

def connect_to_mongo(database, collection):

    """
    Opens a connection to a specified Mongo DB location

    Input Parameters:
    database: name of database to connect to or create (str)
    collection: name of collection to connect to or create (str)

    Returns:
    The connection object for the database without a collection specified
    The connection object for a specific Mongo location (database & collection)
    """

    client = MongoClient()
    db = client[database]
    mongo_loc = db[collection]
    return db, mongo_loc
