from flask import Blueprint

from api.controllers.params import get,set,lista

params = Blueprint('params', __name__)

params.route('/')(lista)
params.route('/<key>')(get)
params.route('/<key>/<value>')(set)
