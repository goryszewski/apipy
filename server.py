from flask import Flask

from flask import Flask, request, jsonify, render_template

from api.models.redis import Mem

from api.routes import load_route

app = Flask(__name__)

app.register_blueprint(load_route())

@app.route('/')
def main():
    return "API"

@app.route('/docs')
def docs():
    print('sending docs')
    return render_template('swaggerui.html')

@app.route('/test')
def test():
    return "test"

def create_app():
    return app.run(debug=True)

if __name__ == '__main__':
    init = create_app()
