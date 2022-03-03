from os import getenv
import csv

# listando os produtos do csv
path = getenv('FILEPATH')
data = []
f = open(path, 'r')
reader = csv.DictReader(f)

for line in reader:
    line['id'] = int(line['id'])
    line['price'] = float(line['price'])
    data.append(line)

f.close()

# lendo o id e comparando para retornar


def read_id(product_id):
    ...
    path = getenv('FILEPATH')
    with open(path, 'r') as arquivo_csv:
        new_arquivo = csv.DictReader(arquivo_csv)
        for product in new_arquivo:
            if product['id'] == product_id:
                product['id'] = int(product['id'])
                f.close()
                return product

    f.close()
    return 'Not Found'

# criando outro produto


def add_product(name, price):
    path = getenv('FILEPATH')
    fieldnames = ['id', 'name', 'price']
    new_id_product = data[-1]['id'] + 1
    new_product = {'id': new_id_product, 'name': name, 'price': float(price)}
    f = open(path, 'a')
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writerow(new_product)
    f.close()
    data.append(new_product)

    return new_product
