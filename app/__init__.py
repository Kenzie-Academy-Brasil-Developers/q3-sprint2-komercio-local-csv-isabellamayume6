from http.client import NOT_FOUND
from flask import Flask, jsonify, request
from http import HTTPStatus
from .products import delete_product, read_all_products, read_id, add_product

app = Flask(__name__)


@app.get('/products')
def allproducts():
    ...
    data = read_all_products()
    return jsonify(data), HTTPStatus.OK


@app.get('/products/<product_id>')
def read_id_product(product_id):
    args = read_id(product_id)

    if args == 'Not Found':

        return {'error': 'product not found'}, HTTPStatus.NOT_FOUND
    return jsonify(args), HTTPStatus.OK


@app.post('/products')
def create_product():
    new_data = request.get_json()

    expected = {'name', 'price'}
    received = set(new_data.keys())
    missing = received - expected

    name = new_data.get('name')
    price = new_data.get('price')

    if missing or (name == None or price == None):
        return {'error': 'missing  name or price'}, HTTPStatus.BAD_REQUEST
    return add_product(name, price), HTTPStatus.CREATED


@app.delete('/products/<int:product_id>')
def delete_products(product_id):
    args = delete_product(product_id)

    if args == 'Not Found':
        return {'error': 'product not found'}, HTTPStatus.BAD_REQUEST

    return jsonify(args), HTTPStatus.OK
