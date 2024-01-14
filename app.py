from flask import Flask

from databases.db import db_session
from resources.routes import initialize_routes

from flask_restful import Api
from flask_cors import CORS

from flask_marshmallow import Marshmallow


app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

ma = Marshmallow(app)


from databases.db import init_db

init_db()
initialize_routes(api)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == "__main__":
    app.run(debug=True)
