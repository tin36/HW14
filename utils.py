import pprint
import sqlite3
import json


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


def genre(listed):
    '''Получение списка фильмов, по заданному жанру'''
    with sqlite3.connect("netflix.db") as con:
        cur = con.cursor()
        query = (
            f"SELECT title, rating, description FROM netflix WHERE listed_in LIKE '%{listed}%'ORDER BY release_year DESC LIMIT 10")
        result = cur.execute(query)
        db = cur.fetchall()
        return db


def genre_list():
    '''Получение списка с жанрами'''
    with sqlite3.connect("netflix.db") as con:
        cur = con.cursor()
        query = (
            f"SELECT listed_in FROM netflix GROUP BY listed_in")
        result = cur.execute(query)
        db = cur.fetchall()
        return db


def genres():
    '''Разделяем строку с несколькими жанрами, удаляем дубликаты'''
    s = genre_list()
    genre_new = []
    for i in s:
        p = i[0].split(', ')
        for z in p:
            genre_new.append(z)
    genres = list(set(genre_new))
    return genres


def cast(name_one, name_two):
    '''Поиск актеров, которые играли больше двух раз с парой актеров из аргументов'''
    with sqlite3.connect("netflix.db") as con:
        cur = con.cursor()
        query = (
            f"SELECT netflix.cast FROM netflix WHERE netflix.cast LIKE '%{name_one}%' OR '%{name_two}%'")
        result = cur.execute(query)
        db = cur.fetchall()
        list_cast = []
        list_friends = []
        for i in db:
            p = i[0].split(', ')
            for z in p:
                list_cast.append(z)
        for i in list_cast:
            if list_cast.count(i) > 2:
                if i not in list_friends:
                    list_friends.append(i)
        list_friends.remove(name_one)
        list_friends.remove(name_two)
        return list_friends


def type_movie(type_film, year, genre):
    '''Поиск фильов по критериям'''
    with sqlite3.connect("netflix.db") as con:
        dict = {}
        cur = con.cursor()
        query = (
            f"SELECT title, description "
            f"FROM netflix "
            f"WHERE type = '{type_film}' AND release_year = '{year}' AND listed_in "
            f"LIKE '%{genre}%'")
        result = cur.execute(query)
        db = cur.fetchall()
        for i in db:
            dict[i[0]] = i[1]
        dict_json = json.dumps(dict)


        return dict_json


# Проверка функций из шагов 5 и 6, домашнего задания
print(cast('Jack Black', 'Dustin Hoffman'))
print(type_movie('TV Show', '2019', 'Action'))
