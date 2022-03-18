from flask import Flask, jsonify, request
from http import HTTPStatus
from .products import delete_product, read_all_products, read_id, add_product, update_product_id

app = Flask(__name__)


@app.get('/products')
def allproducts():
    ...
    args = list(dict(request.args.items()).values())
    page = 0
    per_page = 0
    if args:
        [page, per_page] = args

    return jsonify(read_all_products(page, per_page)), HTTPStatus.OK


@app.get('/products/<product_id>')
def read_id_product(product_id):

    return read_id(product_id)


@app.post('/products')
def create_product():

    return add_product()


@app.patch('/products/<int:product_id>')
def update_products(product_id):

    return update_product_id(product_id)


@app.delete('/products/<int:product_id>')
def delete_products(product_id):

    return delete_product(product_id)
