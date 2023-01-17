from flask import Flask, render_template
from vsearch import search4letters

app = Flask(__name__)


@app.route('/search4', methods=['POST'])
def hello() -> str:
    return 'Hello world from Flask!'


@app.route('/search4')
def do_search() -> str:
    return str(search4letters('life, the universe, and everything', 'aeiou'))


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')




app.run()
