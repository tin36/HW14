import sqlite3

con = sqlite3.connect("netflix.db")
cur = con.cursor()
sqlite_query = ("SELECT * FROM netflix")  # TODO измените код запроса
result = cur.execute(sqlite_query)
test = cur.fetchall()
con.close()
for i in test:
    print(i)
