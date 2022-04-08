import os, csv
import sqlite3
from pprint import pprint

table_name = 'salse_backends_productgroup'

con = sqlite3.connect("db.sqlite3")
cur = con.cursor()
cur.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (id, title, slug);")

path = os.path.abspath(r'table_management/static/data/groups.csv')

with open(
    path,
    'r',
    encoding='utf-8'
) as csvfiles:
    reader = csv.DictReader(
        csvfiles,
        delimiter=';',
        quotechar=','
    )
    created = [
        (
            i['id'],
            i['title'],
            i['slug']
        ) if i else 1 for i in reader
    ]
pprint(created)
cur.executemany(
    "INSERT INTO salse_backends_productgroup (id, title, slug) VALUES (?, ?, ?);",
    created
)
con.commit()
con.close()
