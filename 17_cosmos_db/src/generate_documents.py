import sys; print(sys.executable)
import json
from azure.cosmos import CosmosClient, PartitionKey
from constants import COSMOS_URL, COSMOS_KEY, DB_ID, CONTAINER_ID, PARTITION_KEY, FILMS_PATH


def create_cosmos_db_container(url, key, db_id, container_id, partition_key):
    # connect to an existing cosmos instance
    client = CosmosClient(url, credential=key)

    # create a db for film reviews
    database = client.create_database_if_not_exists(id=db_id)
    print(f"Database created: {db_id}")

    # create a container to store film items
    # and a partition key to separate film items
    container = database.create_container_if_not_exists(
        id=container_id,
        partition_key=PartitionKey(path=partition_key)
    )
    print(f"Container created: {container_id}")

    return container

def connect_cosmos_db_container(url, key, db_id, container_id):
    client = CosmosClient(url, credential=key)

    database = client.get_database_client(db_id)

    container = database.get_container_client(container_id)

    return container    

def insert_documents(container):
    # connect to the json file 
    with open(FILMS_PATH, "r", encoding="utf-8") as f:
        films = json.load(f)
    print(films)
    # insert film items to the container
    for film in films:
        container.upsert_item(film)
        print(f"Film inserted: {film['title']}")

if __name__ == "__main__":

    # film_container = create_cosmos_db_container(COSMOS_URL, COSMOS_KEY, DB_ID, CONTAINER_ID, PARTITION_KEY)
    print(COSMOS_URL)
    film_container = connect_cosmos_db_container(COSMOS_URL, COSMOS_KEY, DB_ID, CONTAINER_ID)


    insert_documents(film_container)
    