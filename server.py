from flask import Flask

from flask import Flask, request, jsonify, render_template

from api.models.redis import Mem

from api.models.mysql import DB

from api.routes import load_route

import os

app = Flask(__name__)

app.register_blueprint(load_route())



@app.route('/')
def docs():
    print('sending docs')
    return render_template('swaggerui.html')

@app.route('/health')
def health():
    config = {
        'user': 'root',
        'password': open(os.environ['MYSQL_ROOT_PASSWORD_FILE']).read().rstrip('\n'),
        'host':  os.environ['HOST_MYSQL'],
        'database': 'Params',
        'charset':'utf8mb4'
        }
    # return jsonify(config)
    test = DB(config).test_connect()
    dbs = DB(config).list_db()
    return jsonify({"SQL":test,"dbs":dbs})

def create_app():
    return app.run(debug=True)

if __name__ == '__main__':
    init = create_app()
