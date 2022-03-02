from os import getenv
import csv

path = getenv('FILEPATH')
data = []
f = open(path, 'r')
reader = csv.DictReader(f)

for line in reader:
    line["id"] = int(line["id"])
    line["price"] = float(line["price"])
    data.append(line)

f.close()
