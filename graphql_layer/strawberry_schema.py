from strawberry import Schema

from graphql_layer.strawberry_mutation import Mutation
from graphql_layer.strawberry_query import Query

# Represents a GraphQL Schema; Contains the query and mutation endpoints available
schema: Schema = Schema(query=Query, mutation=Mutation)
