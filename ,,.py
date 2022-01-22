import sqlite3

def get_database():
    '''Получаение кортежей из БД'''
    with sqlite3.connect("netflix.db") as con:
        lists_base = []
        cur = con.cursor()
        query = (
            f"SELECT * FROM netflix")
        result = cur.execute(query)
        db = cur.fetchall()
        return db

print(get_database())