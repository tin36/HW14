import pprint
import sqlite3


def get_database():
    '''Получаение кортежей из БД'''
    with sqlite3.connect("netflix.db") as con:
        cur = con.cursor()
        query = (
            f"SELECT * FROM netflix")
        result = cur.execute(query)
        db = cur.fetchall()
        return db


def get_film_in_base(word):
    '''Поиск фильмов по слову'''
    with sqlite3.connect("netflix.db") as con:
        cur = con.cursor()
        query = (
            f"SELECT show_id, MAX(release_year) FROM netflix WHERE title LIKE '%{word}%' ")
        result = cur.execute(query)
        test = cur.fetchall()

        for i in test:
            show_id = i[0]
            return show_id  # show_id


def movie_search(show_id):
    '''Получение словаря для вывода информации по фильму'''
    with sqlite3.connect("netflix.db") as con:
        lists_base = []
        cur = con.cursor()
        query = (
            f"SELECT show_id, title, country, release_year, listed_in, description FROM netflix WHERE show_id LIKE '%{show_id}%'")
        result = cur.execute(query)
        db = cur.fetchall()

        for i in db:

            if show_id == i[0]:
                dict = {"title": i[1],
                        "country": i[2],
                        "release_year": i[3],
                        "genre": i[4],
                        "description": i[5],
                        }
                return dict
            else:
                return 'Ничего не найдено'


def years_to_years(start, end):
    '''Получение фильмов из даипазона дат'''
    with sqlite3.connect("netflix.db") as con:
        movie = []
        cur = con.cursor()
        query = (
            f"SELECT show_id, title, country, release_year, listed_in, description FROM netflix WHERE release_year BETWEEN {start} and {end} LIMIT 100")
        result = cur.execute(query)
        db = cur.fetchall()

        return db

def list_years():
    '''Получение словаря для вывода информации по фильму'''
    with sqlite3.connect("netflix.db") as con:
        lists_base = []
        cur = con.cursor()
        query = (
            f"SELECT  release_year FROM netflix WHERE release_year  GROUP BY release_year ORDER BY release_year DESC ")
        result = cur.execute(query)
        db = cur.fetchall()
        return db


def rating_db():
    '''Получение рейтингов фильмов'''
    with sqlite3.connect("netflix.db") as con:
        cur = con.cursor()
        query = (
            f"SELECT rating FROM netflix GROUP BY rating")
        result = cur.execute(query)
        db = cur.fetchall()
        return db

def rating_movie_db():
    '''Получение пары: рейтинг/фильм'''
    with sqlite3.connect("netflix.db") as con:
        cur = con.cursor()
        query = (
            f"SELECT title, rating, description FROM netflix ")
        result = cur.execute(query)
        db = cur.fetchall()
        return db




print(rating_movie_db())