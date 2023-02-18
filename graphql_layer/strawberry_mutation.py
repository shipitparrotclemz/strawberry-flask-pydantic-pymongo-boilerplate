import strawberry

from graphql_layer.pydantic_models.pydantic_types import (
    CreateFarmerMutationResponse,
    InputStrawberryFarmer,
)
from graphql_layer.resolvers.resolvers import resolve_create_farmer
from graphql_layer.strawberry_models.strawberry_input_type import (
    GraphQLInputStrawberryFarmer,
)
from graphql_layer.strawberry_models.strawberry_output_types import (
    GraphQLCreateFarmerMutationResponse,
)


@strawberry.type
class Mutation:
    """
    Contains endpoints which mutate the state of the server.

    Some examples include:
    - endpoints which passes data to the server, to be saved in a database
    """

    @strawberry.mutation
    def create_farmer(
        self, info, farmer: GraphQLInputStrawberryFarmer
    ) -> GraphQLCreateFarmerMutationResponse:
        """
        A mutation endpoint which returns a string
        """
        # Use the `StrawberryTypeFromPydantic.to_pydantic()` method on the input strawberry model to convert it to a pydantic model
        input_farmer: InputStrawberryFarmer = farmer.to_pydantic()
        pydantic_mutation_response: CreateFarmerMutationResponse = (
            resolve_create_farmer(input_farmer)
        )
        # Use the `StrawberryTypeFromPydantic.from_pydantic()` method on the output model to convert it to a strawberry model
        strawberry_mutation_response: GraphQLCreateFarmerMutationResponse = (
            GraphQLCreateFarmerMutationResponse.from_pydantic(
                pydantic_mutation_response
            )
        )
        return strawberry_mutation_response
