from flask import Blueprint

from api.controllers.params import get,set

params = Blueprint('params', __name__)


params.route('/<key>')(get)
params.route('/<key>/<value>')(set)