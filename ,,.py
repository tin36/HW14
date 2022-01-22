import sqlite3
words = 'love'
with sqlite3.connect('netflix.db') as connection:
    cursor = connection.cursor()

    query = """
    SELECT title 
    FROM netflix
    WHERE title LIKE '%{words}%'
    """
    db = cursor.execute(query)

    for i in db:
        print(i)