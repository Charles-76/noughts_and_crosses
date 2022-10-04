def get_database():
    from pymongo import MongoClient
    import pymongo

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://timsullivan:PHerCkzwT7W7p2IS@cluster1.7fxnkoo.mongodb.net/test"

    client = MongoClient(CONNECTION_STRING)
    
    # Create the database for our example (we will use the same database throughout the tutorial
    return client['mongodbVSCodePlaygroundDB']
    
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":    
    
    # Get the database
    dbname = get_database()



