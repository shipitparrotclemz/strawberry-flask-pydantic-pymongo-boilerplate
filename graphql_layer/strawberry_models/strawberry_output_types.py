import strawberry
from graphql_layer.pydantic_models.pydantic_types import (
    CreateFarmerMutationResponse,
    FarmerRole,
    StrawberryFarmer,
)

"""
Create a strawberry output type with Pydantic Model StrawberryFarmers
Make it have the same fields as StrawberryFarmers by setting all_fields=True to the pydantic model decorator
"""

"""
Remember to register your enums if you wish to use them as graphql input / output types
Register them, by calling the strawberry.type class function here, with FarmerRole

This gives us the added benefit of keeping FarmerRole a service-level class, and only recognise it as a strawberry model here
"""
strawberry.enum(FarmerRole, name="GraphQLFarmerRole")


@strawberry.experimental.pydantic.type(model=StrawberryFarmer, all_fields=True)
class GraphQLStrawberryFarmer:
    ...


@strawberry.experimental.pydantic.type(
    model=CreateFarmerMutationResponse, all_fields=True
)
class GraphQLCreateFarmerMutationResponse:
    ...
