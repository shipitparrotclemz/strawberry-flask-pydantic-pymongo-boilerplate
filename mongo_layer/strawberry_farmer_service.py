from abc import ABC
from typing import Optional, List, Dict, Any

from bson import ObjectId
from pymongo import MongoClient
from pymongo.cursor import Cursor
from pymongo.database import Database
from pymongo.results import InsertOneResult
from graphql_layer.pydantic_models.pydantic_types import (
    OutputStrawberryFarmer,
    InputStrawberryFarmer,
)
from mongo_layer.models.insert_result import InsertResult


class StrawberryFarmerDAO(ABC):
    """
    Represents an Abstract Data Access Object for Strawberry Farmers
    We abstract it here, so that we have the freedom to include more implementations for this
    """

    def create_farmer(self, farmer: InputStrawberryFarmer) -> InsertResult:
        """
        Creates a farmer in the database
        :param farmer: An input farmer
        :return: return a boolean indicating if the insert was successful
        """
        raise NotImplementedError

    def find_farmer(self, id: str) -> Optional[OutputStrawberryFarmer]:
        """
        Finds a farmer in the database by id
        :param id: The id of the farmer
        :return: return a StrawberryFarmer if found, else None
        """
        raise NotImplementedError

    def find_farmers(self, name: str) -> List[OutputStrawberryFarmer]:
        """
        Finds farmers in the database by name
        - We can have farmers with the same name
        :param name: The name of the farmer
        :return: return a StrawberryFarmer if found, else None
        """
        raise NotImplementedError


class StrawberryFarmerMongoDAOImpl(StrawberryFarmerDAO):
    def __init__(
        self, mongo_client: MongoClient[Dict[str, Any]], database_name: str, collection_name: str
    ):
        self.mongo_client: MongoClient[Dict[str, Any]] = mongo_client
        self.database: Database[Dict[str, Any]] = self.mongo_client[database_name]
        self.collection = self.database[collection_name]
        # ensure the indexes necessary to support the queries are present
        self.ensure_indexes()

    """
    Represents a MongoDB implementation of the StrawberryFarmerDAO
    """

    def ensure_indexes(self) -> None:
        """
        Ensures that the indexes are created for the collection
        """
        self.collection.create_index([("name", 1), ("_id", 1)])

    def create_farmer(self, farmer: InputStrawberryFarmer) -> InsertResult:
        """
        Creates a farmer in the database
        :param farmer: An input farmer
        :return: return an InsertResult indicating the id of the new document, and the success of the insert
        """
        insert_one_result: InsertOneResult = self.collection.insert_one(farmer.dict())
        insert_success: bool = insert_one_result.acknowledged
        insert_id: Optional[str] = (
            str(insert_one_result.inserted_id) if insert_success else None
        )
        return InsertResult(
            id=insert_id,
            success=insert_one_result.acknowledged,
        )

    def find_farmer(self, id: str) -> Optional[OutputStrawberryFarmer]:
        """
        Finds a farmer in the database by id
        :param id: The id of the farmer
        :return: return a StrawberryFarmer if found, else None
        """
        raw_farmer: Optional[Dict[str, Any]] = self.collection.find_one(
            {"_id": ObjectId(id)}
        )
        farmer: Optional[OutputStrawberryFarmer] = (
            OutputStrawberryFarmer.parse_obj(raw_farmer) if raw_farmer else None
        )
        return farmer

    def find_farmers(self, name: str) -> List[OutputStrawberryFarmer]:
        """
        Finds farmers in the database by name
        - We can have farmers with the same name
        :param name: The name of the farmer
        :return: return a StrawberryFarmer if found, else None
        """
        raw_farmer_cursor: Cursor[Dict[str, Any]] = self.collection.find({"name": name})
        farmers: List[OutputStrawberryFarmer] = [
            OutputStrawberryFarmer.parse_obj(raw_farmer)
            for raw_farmer in raw_farmer_cursor
        ]
        return farmers
