from flask import Flask
import redis

app = Flask(__name__)

r = redis.Redis(host='redis-svc', port=6379, decode_responses=True)

@app.route('/')
def hello_world():
    return 'Hello '

@app.route('/set/<key>/<data>')
def set(key,data):
    r.set(key,data )
    return 'Set Redis data {}:{}'.format(key,data)

@app.route('/get/<key>')
def get(key):
    data = r.get(key)
    return 'Get Redis data {}:{}'.format(key,data)

if __name__ == '__main__':
    app.run()