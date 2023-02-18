from flask import Flask
from strawberry.flask.views import GraphQLView

from graphql_layer.strawberry_schema import schema

app = Flask(__name__)


app.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view("graphql_view", schema=schema)
)


if __name__ == "__main__":
    app.run(port=5000)
