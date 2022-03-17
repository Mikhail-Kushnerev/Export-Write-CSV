import csv, sqlite3


con = sqlite3.connect("db.sqlite3")
cur = con.cursor()
cur.execute("CREATE TABLE ttable (id, RollNo, Class, First_Name, Last_Name);")

path = "D:/Final/Export-Write-CSV/table_management/static/data/table.csv"

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
            i['RollNo'],
            i['id'],
            i['Class'],
            i['First_Name'],
            i['Last_Name']
        ) if i else 1 for i in reader
    ]
cur.executemany(
    "INSERT INTO ttable (RollNo, id, Class, First_Name, Last_Name) VALUES (?, ?, ?, ?, ?);",
    created
)
con.commit()
con.close()
