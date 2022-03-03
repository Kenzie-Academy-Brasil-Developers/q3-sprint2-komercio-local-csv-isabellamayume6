from os import getenv
import csv

# listando os produtos do csv
path = getenv('FILEPATH')


def read_all_products():
    data = []
    f = open(path, 'r')
    reader = csv.DictReader(f)

    for line in reader:
        line['id'] = int(line['id'])
        line['price'] = float(line['price'])
        data.append(line)

    f.close()
    return data

# lendo o id e comparando para retornar


def read_id(product_id):
    ...
    path = getenv('FILEPATH')
    with open(path, 'r') as arquivo_csv:
        new_arquivo = csv.DictReader(arquivo_csv)
        for product in new_arquivo:
            if product['id'] == product_id:
                product['id'] = int(product['id'])
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
    print(product_id)
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

    data_without_id_deleted = {}
    for line in result:
        if int(line['id']) == product_id:
            for line in result:
                line['id'] = int(line['id'])
                line['price'] = float(line['price'])
            data_without_id_deleted = line
        else:
            write.writerow(line)
    f.close()
    if data_without_id_deleted:
        return data_without_id_deleted
    return 'Not Found'
