import strawberry

from graphql_layer.pydantic_models.strawberry_farmers import (
    FarmerRole,
    StrawberryFarmer,
)
from graphql_layer.strawberry_models.graphql_models import (
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
        strawberry_farmer: StrawberryFarmer = StrawberryFarmer(
            name="Patrick", age=25, role=FarmerRole.grower
        )
        # Use the strawberry type's from_pydantic method to convert the pydantic model to a strawberry type
        graphql_strawberry_farmer: GraphQLStrawberryFarmer = (
            GraphQLStrawberryFarmer.from_pydantic(strawberry_farmer)
        )

        return graphql_strawberry_farmer
