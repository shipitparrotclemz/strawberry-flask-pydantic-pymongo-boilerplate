import strawberry

from graphql_layer.pydantic_models.pydantic_types import (
    InputStrawberryFarmer,
    InputFarmerNameFilter,
    InputFarmerIdFilter,
    FarmerRole,
)

"""
Pass in `is_input` = True to the pydantic model decorator, to tell strawberry that this is an input type
"""

strawberry.enum(FarmerRole, name="GraphQLFarmerRole")


@strawberry.experimental.pydantic.type(
    model=InputStrawberryFarmer, is_input=True, all_fields=True
)
class GraphQLInputStrawberryFarmer:
    ...


@strawberry.experimental.pydantic.type(
    model=InputFarmerNameFilter, is_input=True, all_fields=True
)
class GraphQLInputFarmerNameFilter:
    ...


@strawberry.experimental.pydantic.type(
    model=InputFarmerIdFilter, is_input=True, all_fields=True
)
class GraphQLInputFarmerIdFilter:
    ...
