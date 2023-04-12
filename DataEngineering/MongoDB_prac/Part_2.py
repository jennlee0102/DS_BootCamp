from openaq import OpenAQ

api = OpenAQ()

"""
get_results
"""

def get_results():
    # Import data from OpenAQ
    _, body = api.measurements(city='Los Angeles', parameter='pm25')

    # append TODO (datetime, value) in tuple to results
    # body info:
    # https://api.openaq.org/v1/measurements?city=Los%20Angeles&parameter=pm25

    results = [(x["value"], x["date"]["local"]) for x in body["results"]]
    
    return results

"""
Part 2.2 MONGODB SETUP
"""
from pymongo import MongoClient

# Input MongoDB connection info.
HOST = 'cluster0.f0bf1fa.mongodb.net'
USER = 'wodms28104'
PASSWORD = 'Eun3574168!'
DATABASE_NAME = 'WHALE-PROJECT'
COLLECTION_NAME = 'OpenAQ'
MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority"

# Check if the body gained from OpenAQ is entered in MongoDB.
# check if the database exists
if DATABASE_NAME in client.list_database_names():
    print(f"{DATABASE_NAME} exists")
else:
    print(f"No, there is no {db_name}")

# Check if collection exists
if COLLECTION_NAME in db.list_collection_names():
    print("{COLLECTION_NAME} exists")
else:
    print("{COLLECTION_NAME} does not exist")
