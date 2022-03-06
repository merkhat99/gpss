from flask import Flask, jsonify, request
import requests
from main import get_info_by_ip

app = Flask(__name__)
app.secret_key = '464820Ms'


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    ip = request.remote_addr
    get_info_by_ip(ip=ip)
    return jsonify({'ip': request.remote_addr})


@app.route('/test')
def hello_world():
    ip_addr = request.remote_addr
    return '<h1> Your IP address is:' + ip_addr


@app.route('/client')
def client():
    ip_addr = request.environ['REMOTE_ADDR']
    return '<h1> Your IP address is:' + ip_addr


@app.route('/clients')
def proxy_client():
    ip_addr = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    return '<h1> Your IP address is:' + ip_addr


if __name__ == '__main__':
    app.run()
