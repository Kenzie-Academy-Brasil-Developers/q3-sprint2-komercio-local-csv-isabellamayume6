from http import HTTPStatus
from os import getenv
import csv

from flask import jsonify

# listando os produtos do csv
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
    print(result_data)
    return result_data

# lendo o id e comparando para retornar:


def read_id(product_id):
    ...
    path = getenv('FILEPATH')
    with open(path, 'r') as arquivo_csv:
        new_arquivo = csv.DictReader(arquivo_csv)
        for product in new_arquivo:
            if product['id'] == product_id:
                product['id'] = int(product['id'])
                product['price'] = float(product['price'])

                return product

    return 'Not Found'

# criando outro produto


def add_product(name, price):
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
    new_id_product = data[-1]['id'] + 1
    new_product = {'id': new_id_product, 'name': name, 'price': float(price)}
    f = open(path, 'a')
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writerow(new_product)
    f.close()
    data.append(new_product)

    return new_product

# editando o item

# deletando o produto


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
        print(data_without_id_deleted)
        result_data = {}
        for line in data_without_id_deleted:
            line['id'] = int(line['id'])
            line['price'] = float(line['price'])
            result_data = line
        print(result_data)
        return result_data
    return 'Not Found'
