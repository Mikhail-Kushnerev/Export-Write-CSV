# import csv, sqlite3

# # from .models import Category

# con = sqlite3.connect("db.sqlite3")
# cur = con.cursor()
# # cur.execute("CREATE TABLE content_category (id, name, slug);")

# # path = "D:/Final/api_yamdb/static/data/category.csv"

# with open(
#     'D:/Final/api_yamdb/api_yamdb/static/data/category.csv',
#     'r',
#     encoding='utf-8'
# ) as csvfiles:
#     reader = csv.DictReader(csvfiles)
#     created = [(i['id'], i['name'], i['slug']) if i else 1 for i in reader]
# cur.executemany("INSERT INTO rewiews_categories (id, name, slug) VALUES (?, ?, ?);", created)
# con.commit()
# con.close()
