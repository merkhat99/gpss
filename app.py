from flask import Flask, jsonify, request
import requests
from main import get_info_by_ip

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    ip = request.remote_addr
    get_info_by_ip(ip=ip)
    return jsonify({'ip': request.remote_addr})


if __name__ == '__main__':
    app.run()
