
from flask import Flask, render_template
import tmdb_client

app = Flask(__name__)


"""
@app.route('/')
def homepage():
    return render_template("index.html")
"""


@app.route('/')
def homepage():
    how_many_movies = 8
    movies = tmdb_client.get_movies(how_many_movies)
    print(movies)
    return render_template("homepage.html", movies=movies)


@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}


@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    print(details)
    how_many = 4
    cast = tmdb_client.get_single_movie_cast(movie_id)[:how_many]
    print(cast)
    return render_template("movie_details.html", movie=details, cast=cast)


@app.context_processor
def utility_processor():
    def tmdb_image_backdrop(path, size):
        return tmdb_client.get_backdrop_path(path, size)
    return {"tmdb_image_backdrop": tmdb_image_backdrop}



if __name__ == '__main__':
    app.run(debug=True)

