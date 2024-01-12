from flask import Flask

# from util import init_config
from databases.db import initialize_db
from resources.routes import initialize_routes

from flask_restful import Api
from flask_cors import CORS, cross_origin

from flask_marshmallow import Marshmallow


import os

app = Flask(__name__)
CORS(app)
api = Api(app)

ma = Marshmallow(app)


MONGO_HOST = os.environ["MONGO_HOST"]


app.config["MONGODB_SETTINGS"] = {"host": f"mongodb://{MONGO_HOST}/tasks"}
initialize_db(app)
initialize_routes(api)

if __name__ == "__main__":
    app.run(debug=True)
