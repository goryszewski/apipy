from flask import Blueprint

from api.routes.params import params
route = Blueprint('Default',__name__)

def load_route():
    route.register_blueprint(params,url_prefix="/params")
    return route