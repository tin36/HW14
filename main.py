import sqlite3
from utils import get_database, get_film_in_base, movie_search, list_years, years_to_years, rating_db, rating_movie_db, \
    genre, genre_list, genres

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', )
def main_page():
    return render_template('index.html')


@app.route('/search/', )
def search():
    db = get_database()

    s = request.args.get('s', '')
    s = s.lower()

    show_id = get_film_in_base(s)
    m_search = movie_search(show_id)
    return render_template('search.html', m_search=m_search, db=db, s=s)


@app.route('/movie/<title>', )
def movie(title):
    db = get_database()
    for i in db:
        if title == i[2]:
            show_id = get_film_in_base(i[2])
            m_search = movie_search(show_id)

    return render_template('movie.html', m_search=m_search)


@app.route('/movies/', )
def movie_all():
    list_year = list_years()
    return render_template('movie_all.html', list_year=list_year)


@app.route('/movies/<start>', )
def movie_start(start):
    list_year = list_years()

    return render_template('movie_start.html', list_year=list_year, start=start)


@app.route('/movies/<start>/<end>', )
def years_movie(start, end):
    # s = request.args.get('s', '')
    # end = request.args.get('end', '')
    # list_year = list_years()
    movie = years_to_years(start, end)
    number_list = []
    movies = []
    for i in movie:
        dict = {"title": i[1],
                "release_year": i[3]}
        movies.append(dict)
    for i in range(100):
        number_list.append(i)

    return render_template('year.html', movie=movie, start=start, end=end, number_list=number_list, movies=movies)


# @app.route('/movies/<start>/<end>', )
# def years_movie(start, end):
#     # s = request.args.get('s', '')
#     # end = request.args.get('end', '')
#     # list_year = list_years()
#     movie = years_to_years(start, end)
#     number_list = []
#     movies = []
#     for i in movie:
#         dict = {"title": i[1],
#                 "release_year": i[3]}
#         movies.append(dict)
#     for i in range(100):
#         number_list.append(i)
#
#     return render_template('year.html', movie=movie, start=start, end=end, number_list=number_list, movies=movies)
#

@app.route('/rating/')
def category():
    return render_template('rating.html')


@app.route('/rating/<type>')
def rating(type):
    rating_movie = rating_movie_db()
    movie_list = []
    for i in rating_movie:
        if type == 'children':
            if i[1] == 'G':
                dict = {
                    "title": i[0],
                    "rating": i[1],
                    "description": i[2]
                }
                movie_list.append(dict)
        if type == 'family':
            if i[1] == 'G' or i[1] == 'PG-13' or i[1] == 'PG':
                dict = {
                    "title": i[0],
                    "rating": i[1],
                    "description": i[2]
                }
                movie_list.append(dict)
        if type == 'adult':
            if i[1] == 'R' or i[1] == 'NC-17':
                dict = {
                    "title": i[0],
                    "rating": i[1],
                    "description": i[2]
                }
                movie_list.append(dict)
    return render_template('rating.html', movie_list=movie_list)


@app.route('/genre/')
def genre_list_():
    genre = genres()

    return render_template('genre.html', genre=genre)


@app.route('/genre/<type>')
def genre_on_type(type):
    movie = genre(type)
    movie_list = []
    for i in movie:
        dict = {
            "title": i[0],
            "rating": i[1],
            "description": i[2]
        }
        movie_list.append(dict)
    return render_template('genre.html', movie_list=movie_list)


if __name__ == "__main__":
    app.run(debug=True)
