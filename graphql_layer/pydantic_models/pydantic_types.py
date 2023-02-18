from enum import Enum
from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field, validator

from mongo_layer.models.insert_result import InsertResult


class FarmerRole(str, Enum):
    quality_manager = "Quality Manager"
    data_analyst = "Data Analyst"
    pest_and_disease_control = "Pest and Disease Control"
    cultivation_expert = "Cultivation Expert"
    customer_support = "Customer Support"
    manpower_scheduler = "Manpower Scheduler"
    grower = "Grower"


class InputStrawberryFarmer(BaseModel):
    name: str
    age: int
    role: FarmerRole


class InputFarmerNameFilter(BaseModel):
    name: str


class InputFarmerIdFilter(BaseModel):
    id: str


class OutputStrawberryFarmer(BaseModel):
    id: str = Field(alias="_id")
    name: str
    age: int
    role: FarmerRole

    @validator("id", pre=True)
    def cast_object_id_to_str_id(cls, v):
        """
        Mongo gives us an ObjectId, but we want to return a string
        Cast it to a str here
        """
        if isinstance(v, ObjectId):
            return str(v)
        else:
            return v


class CreateFarmerMutationResponse(BaseModel):
    id: Optional[str]
    success: bool

    """
    id can be Optional, if the insert was not successful
    """

    @staticmethod
    def from_insert_result(
        insert_result: InsertResult,
    ) -> "CreateFarmerMutationResponse":
        """
        Creates a CreateFarmerMutationResponse from a mongo InsertResult
        """
        return CreateFarmerMutationResponse(
            id=insert_result.id, success=insert_result.success
        )