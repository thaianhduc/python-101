# Import the library and create an alias. Look the same as namespace in C#
import azure.cosmos.cosmos_client as cosmos_client

print(cosmos_client)
# Config for cosmos database. This is a dictionary in python
'''
Working with CosmosDB requires
    ENDPOINT: The URI identified the cosmos server.
    MASTER_KEY: Authorization key, just like username/password in SQL.
    DATABASE: The name of the database.
    COLLECTION: Or CONTAINER name.
Operations are per collection in Cosmos.
'''
config = {
    'ENDPOINT':'https://tad-python.documents.azure.com:443/',
    'MASTER_KEY':'SGg2vIcxvAJO2lE3vieHJ7iFEiI6Wruqc5DF1rYE1kGa9AldFQE0LWYb9bJHt5DlWL06pChyKiio7KDumqwhwg==',
    'DATABASE':'',
    'COLLECTION':''
}
# Prompt users for database name and collection
config['DATABASE'] = input("Database: ")
config['COLLECTION'] = input("Collection: ")

print(config)

# 1. Initialize the client that can talk to the server
client = cosmos_client.CosmosClient(
    url_connection=config['ENDPOINT'], 
    auth={
        'masterKey':config['MASTER_KEY']
        })

# 2. Create a database
db = client.CreateDatabase({'id':config['DATABASE']})

print(db)

# 3. Create a collection/container
collection = client.CreateContainer(
        db['_self'],
        {'id':config['COLLECTION']})

print(collection)
# 3. Create a collection/container
