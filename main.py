import sqlite3
from utils import get_database, get_film_in_base, movie_search

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
    # else:
    #     s = s
    #     show_id = get_film_in_base(s)
    #     m_search = movie_search(show_id)
    return render_template('search.html', m_search=m_search, db=db, s=s)


@app.route('/movie/<title>', )
def movie(title):
    db = get_database()
    for i in db:
        if title == i[2]:
            show_id = get_film_in_base(i[2])
            m_search = movie_search(show_id)

    return render_template('movie.html', m_search=m_search)

if __name__ == "__main__":
    app.run(debug=True)
