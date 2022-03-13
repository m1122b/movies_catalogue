
from flask import Flask, render_template


app = Flask(__name__)


"""
@app.route('/')
def homepage():
    return render_template("index.html")
"""


@app.route('/')
def homepage():
    movies = ['Czerwona nota', 'Projekt Adam', 'Matka/Android', 'Czarnobyl 1986']
    for i in range(1):
        movies = movies + movies
    return render_template("homepage.html", movies=movies)


if __name__ == '__main__':
    app.run(debug=True)

