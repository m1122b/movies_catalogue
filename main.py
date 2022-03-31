
from random import choice
from flask import Flask, render_template, request
import tmdb_client

app = Flask(__name__)


"""
@app.route('/')
def homepage():
    return render_template("index.html")
"""


@app.route('/')
def homepage():
    list_types = [{'id' : 'popular', 'label': 'Najczęściej oglądane'},
                    {'id' :'now_playing', 'label' : 'W kinach'},  
                    {'id' : 'top_rated', 'label' : 'Najwyżej oceniane'}, 
                    {'id' : 'upcoming', 'label' : 'Premiery'}]
    selected_list = request.args.get('list_type', 'popular')
    print(f"Selected list: {selected_list}")
    if selected_list != 'now_playing' and selected_list != 'popular' and selected_list != 'top_rated' and selected_list != 'upcoming':
        selected_list = 'popular'
    print(f"Selected list: {selected_list}")

    how_many_movies = 8
    movies = tmdb_client.get_movies(how_many_movies, list_type=selected_list)
    print(movies)
    return render_template("homepage.html", movies=movies, current_list=selected_list, list_types=list_types)


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
    movie_images = tmdb_client.get_movie_images(movie_id)
    selected_backdrop = choice(movie_images['backdrops'])
    print(selected_backdrop)
    return render_template("movie_details.html", movie=details, cast=cast, selected_backdrop=selected_backdrop)


@app.context_processor
def utility_processor():
    def tmdb_image_backdrop(path, size):
        return tmdb_client.get_backdrop_path(path, size)
    return {"tmdb_image_backdrop": tmdb_image_backdrop}



if __name__ == '__main__':
    app.run(debug=True)

