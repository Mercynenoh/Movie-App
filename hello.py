from flask import Flask, render_template
from model import db

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', name='Mercy', age='23')

@app.route('/acronyms')
def acronyms():
    acronym = db[0]
    return render_template('acronym.html', acronym= acronym)

if __name__ == '__main__':
    app.run(debug = True)