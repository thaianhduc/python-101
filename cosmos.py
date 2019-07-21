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
    'ENDPOINT':'',
    'MASTER_KEY':'',
    'DATABASE':'',
    'COLLECTION':''
}

# Initialize the client that can talk to the server
client = cosmos_client.CosmosClient(
    url_connection=config['ENDPOINT'], 
    auth={
        'masterKey':config['MASTER_KEY']
        })

# Create database
db = client.CreateDatabase({'id':config['DATABASE']})

# Create collection/container
collection = client.CreateContainer(
        db['_self'],
        {'id':con['COLLECTION']})

