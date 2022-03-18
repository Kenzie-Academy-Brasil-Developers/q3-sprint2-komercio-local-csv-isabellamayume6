from http import HTTPStatus
from os import getenv
import csv

from flask import jsonify, request
path = getenv('FILEPATH')


def read_all_products(page, per_page):
    data = []
    f = open(path, 'r')
    reader = csv.DictReader(f)
    for line in reader:
        line['id'] = int(line['id'])
        line['price'] = float(line['price'])
        data.append(line)
        result_data = []

    if page and per_page:
        page = int(page)
        per_page = int(per_page)

        result_data = data[page:(per_page+page)]
    else:
        result_data = data[0:3]
        f.close()
    return result_data


def read_id(product_id):
    ...
    path = getenv('FILEPATH')
    with open(path, 'r') as arquivo_csv:
        new_arquivo = csv.DictReader(arquivo_csv)
        for product in new_arquivo:
            if product['id'] == product_id:
                product['id'] = int(product['id'])
                product['price'] = float(product['price'])

                return jsonify(product), HTTPStatus.OK

    return {"error": f"product {product_id} not found"}, HTTPStatus.NOT_FOUND


def add_product():
    path = getenv('FILEPATH')
    fieldnames = ['id', 'name', 'price']
    data = []
    f = open(path, 'r')
    reader = csv.DictReader(f)

    for line in reader:
        line['id'] = int(line['id'])
        line['price'] = float(line['price'])
        data.append(line)

    f.close()
    new_data = request.get_json()

    expected = {'name', 'price'}
    received = set(new_data.keys())
    missing = received - expected

    name = new_data.get('name')
    price = new_data.get('price')

    if missing or (name == None or price == None):
        return {'error': 'missing  name or price'}, HTTPStatus.BAD_REQUEST
    new_id_product = data[-1]['id'] + 1
    new_product = {'id': new_id_product, 'name': name, 'price': float(price)}
    f = open(path, 'a')
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writerow(new_product)
    f.close()
    data.append(new_product)

    return new_product, HTTPStatus.CREATED


def update_product_id(product_id):
    ...
    path = getenv('FILEPATH')
    g = open(path, 'r')
    read = csv.DictReader(g)
    result = []
    data_update = request.get_json()
    name_update = data_update.get("name")
    price_update = data_update.get("price")
    for line in read:
        result.append(line)
    fieldnames = ['id', 'name', 'price']
    f = open(path, 'w')
    write = csv.DictWriter(f, fieldnames=fieldnames)
    write.writeheader()
    data_would_be_updated = {}
    for lines in result:
        if int(lines['id']) == product_id:
            data_would_be_updated = lines
        else:
            write.writerow(lines)
    if data_would_be_updated:
        data_would_be_updated['name'] = name_update
        data_would_be_updated['price'] = float(price_update)
        write.writerow(data_would_be_updated)
        return jsonify(data_would_be_updated), HTTPStatus.OK
    f.close()
    return {"error": f"product {product_id} not found"}, HTTPStatus.NOT_FOUND


def delete_product(product_id):
    path = getenv('FILEPATH')
    g = open(path, 'r')
    read = csv.DictReader(g)
    result = []

    for line in read:
        result.append(line)

    fieldnames = ['id', 'name', 'price']
    f = open(path, 'w')
    write = csv.DictWriter(f, fieldnames=fieldnames)

    write.writeheader()

    data_without_id_deleted = []
    for lines in result:
        if int(lines['id']) == product_id:
            data_without_id_deleted.append(lines)
        else:
            write.writerow(lines)
    f.close()
    if data_without_id_deleted:
        result_data = {}
        for line in data_without_id_deleted:
            line['id'] = int(line['id'])
            line['price'] = float(line['price'])
            result_data = line
        return jsonify(result_data), HTTPStatus.OK
    return {"error": f"product {product_id} not found"}, HTTPStatus.NOT_FOUND
