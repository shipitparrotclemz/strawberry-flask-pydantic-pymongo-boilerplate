from pymongo import MongoClient

from mongo_layer.strawberry_farmer_service import (
    StrawberryFarmerDAO,
    StrawberryFarmerMongoDAOImpl,
)
from settings import MONGO_URL

strawberry_farmer_dao: StrawberryFarmerDAO = StrawberryFarmerMongoDAOImpl(
    mongo_client=MongoClient(MONGO_URL),
    database_name="strawberry_farmers",
    collection_name="strawberry_farmers",
)
