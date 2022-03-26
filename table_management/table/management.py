import os, csv
import sqlite3

con = sqlite3.connect("db.sqlite3")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS products (id_product, name, category, units, weight);")

path = os.path.abspath(r'table_management\static\data\products.csv')

with open(
    path,
    'r',
    encoding='utf-8'
) as csvfiles:
    reader = csv.DictReader(
        csvfiles,
        # delimiter=';',
        # quotechar=','
    )
    created = [
        (
            i['id_product'],
            i['name'],
            i['category'],
            i['units'],
            i['weight']
        ) if i else 1 for i in reader
    ]
cur.executemany(
    "INSERT INTO products (id_product, name, category, units, weight) VALUES (?, ?, ?, ?, ?);",
    created
)
con.commit()
con.close()
