from typing import List, Optional

from graphql_layer.pydantic_models.pydantic_types import (
    CreateFarmerMutationResponse,
    InputStrawberryFarmer,
    OutputStrawberryFarmer,
)
from mongo_layer.models.insert_result import InsertResult
from mongo_layer.mongo_services import strawberry_farmer_dao


def resolve_create_farmer(
    input_strawberry_farmer: InputStrawberryFarmer,
) -> CreateFarmerMutationResponse:
    """
    A mutation resolver which creates a farmer in Mongo
    """
    insert_result: InsertResult = strawberry_farmer_dao.create_farmer(
        input_strawberry_farmer
    )
    mutation_response: CreateFarmerMutationResponse = (
        CreateFarmerMutationResponse.from_insert_result(insert_result)
    )
    return mutation_response


def resolve_find_farmers_by_name(
    name: str,
) -> List[OutputStrawberryFarmer]:
    """
    A query resolver which finds farmers by name
    """
    farmers: List[OutputStrawberryFarmer] = strawberry_farmer_dao.find_farmers(name)
    return farmers


def resolve_find_farmer_by_id(id: str) -> Optional[OutputStrawberryFarmer]:
    """
    A query resolver which finds farmers by name
    """
    farmer: Optional[OutputStrawberryFarmer] = strawberry_farmer_dao.find_farmer(id)
    return farmer
