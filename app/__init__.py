from http.client import NOT_FOUND
from flask import Flask,jsonify, request
from http import HTTPStatus
from .products import  data

app = Flask(__name__)

@app.get('/products')
def products():
    ...
    return jsonify(data), HTTPStatus.OK
