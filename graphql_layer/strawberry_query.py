from typing import List, Optional

import strawberry
from graphql_layer.pydantic_models.pydantic_types import (
    InputFarmerNameFilter,
    OutputStrawberryFarmer,
    InputFarmerIdFilter,
    FarmerRole,
)
from graphql_layer.resolvers.resolvers import (
    resolve_find_farmers_by_name,
    resolve_find_farmer_by_id,
)
from graphql_layer.strawberry_models.strawberry_input_type import (
    GraphQLInputFarmerIdFilter,
    GraphQLInputFarmerNameFilter,
)
from graphql_layer.strawberry_models.strawberry_output_types import (
    GraphQLStrawberryFarmer,
)


@strawberry.type
class Query:
    """
    This Query class contains all query endpoints available to the client.

    We place endpoints under Query, if the endpoint is intended to return data to the client, without changing
    the state of the server.

    E.G an endpoint which fetches a list of users from the database; e.g mongo, would be placed under Query.
    """

    """
    A simple endpoint that returns a dummy string "Hello World!"
    """

    @strawberry.field
    def hello(self, info) -> str:
        """
        We can return a string here, as strawberry has a built-in String type
        """
        return "Hello World!"

    @strawberry.field
    def get_sample_farmer(self, info) -> GraphQLStrawberryFarmer:
        """
        Returns an output GraphQL Output Type, which is a strawberry type, with a pydantic model as its base
        """
        strawberry_farmer: OutputStrawberryFarmer = OutputStrawberryFarmer(
            name="Patrick", age=25, role=FarmerRole.grower
        )
        # Use the strawberry type's from_pydantic method to convert the pydantic model to a strawberry type
        graphql_strawberry_farmer: GraphQLStrawberryFarmer = (
            GraphQLStrawberryFarmer.from_pydantic(strawberry_farmer)
        )

        return graphql_strawberry_farmer

    @strawberry.field
    def get_farmers_by_name(
        self, info, input_filter: GraphQLInputFarmerNameFilter
    ) -> List[GraphQLStrawberryFarmer]:
        """
        Returns a list of strawberry farmers, sharing the input name
        """
        pydantic_input_filter: InputFarmerNameFilter = input_filter.to_pydantic()
        farmer_name: str = pydantic_input_filter.name
        pydantic_farmers: List[OutputStrawberryFarmer] = resolve_find_farmers_by_name(
            farmer_name
        )
        strawberry_farmers: List[GraphQLStrawberryFarmer] = [
            GraphQLStrawberryFarmer.from_pydantic(pydantic_farmer)
            for pydantic_farmer in pydantic_farmers
        ]
        return strawberry_farmers

    @strawberry.field
    def get_farmer_by_id(
        self, info, input_filter: GraphQLInputFarmerIdFilter
    ) -> Optional[GraphQLStrawberryFarmer]:
        """
        Searches for a single strawberry farmer, sharing the input id
        """
        pydantic_input_filter: InputFarmerIdFilter = input_filter.to_pydantic()
        farmer_id: str = pydantic_input_filter.id
        pydantic_farmer: Optional[OutputStrawberryFarmer] = resolve_find_farmer_by_id(
            farmer_id
        )
        strawberry_farmer: Optional[GraphQLStrawberryFarmer] = (
            GraphQLStrawberryFarmer.from_pydantic(pydantic_farmer)
            if pydantic_farmer
            else None
        )
        return strawberry_farmer
