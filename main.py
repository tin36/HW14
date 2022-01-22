import sqlite3
from utils import get_read_db, movie_search

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', )
def main_page():
    return render_template('index.html')

@app.route('/search/', )
def search():
    db = get_read_db()

    s = request.args.get('s', '')
    s = s.lower()
    m_search = movie_search(s)


    return render_template('search.html', m_search=m_search, db=db)

app.run(debug=True)