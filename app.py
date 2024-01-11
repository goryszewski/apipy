from flask import Flask
from databases.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)
api = Api(app)

app.config["MONGODB_SETTINGS"] = {"host": "mongodb://mongo/tasks"}
initialize_db(app)
initialize_routes(api)

app.run(debug=True)
