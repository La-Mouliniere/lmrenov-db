import os
from dotenv import load_dotenv

from client import Client
from bikes_data import bikes, Bike


load_dotenv("stack.env")

API_TOKEN = os.environ.get("API_TOKEN")
FASTAPI_URL = "http://localhost:9441"
COLLECTION_NAME = "Bikes"


def main():
    client = Client(FASTAPI_URL, API_TOKEN)
    client.create_collection(COLLECTION_NAME)

    # for bike in bikes:
    #     # print(bike.model_dump(mode="json"))
    #     client.create_document(COLLECTION_NAME, bike.model_dump(mode="json"))

    # print("List of bikes:")
    # documents = client.get_documents(COLLECTION_NAME)
    # for doc in documents:
    #     print(doc)

    json_bike = client.get_document(COLLECTION_NAME, "4")
    bike = Bike.model_validate(json_bike)
    print(bike)



if __name__ == "__main__":
    main()