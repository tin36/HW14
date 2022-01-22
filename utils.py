import pprint
import sqlite3

def get_read_db():
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()

        query = """
        SELECT * 
        FROM netflix
        """
        db = cursor.execute(query)
        return db

def get_db_id(id):

    for i in get_read_db():
        if id == i[0]:

            dict = {"title": i[2],
                    "country": i[5],
                    "release_year": i[7],
                    "genre": i[11],
                    "description": i[12],
                }
            return dict

def movie_search(word):
    '''поиск фильмма по названию'''

    db = get_read_db()
    for i in db:
        if word in i[2]:
            dict = {"title": i[2],
                    "country": i[5],
                    "release_year": i[7],
                    "genre": i[11],
                    "description": i[12],
                    }
            return dict
