import strawberry


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
        return "Hello World!"