
from random import choices, choice
import requests


PAYLOAD = {'api_key': 'de232542034b3603e0d8b59a43a78c8f'}


def get_popular_movies():
    url = 'https://api.themoviedb.org/3/movie/popular'
    r = requests.get(url, params=PAYLOAD)
    return r.json()


def get_movies_list(list_type):
    url = f"https://api.themoviedb.org/3/movie/{list_type}"
    r = requests.get(url, params=PAYLOAD)
    r.raise_for_status()
    return r.json()


def get_poster_url(poster_api_path, size = 'w342'):
    base_url = 'https://image.tmdb.org/t/p/'
    return f"{base_url}{size}{poster_api_path}"


def get_movies(how_many=8, list_type='popular'):
    data = choices(get_movies_list(list_type)['results'], k=how_many)
    return data


def get_single_movie(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    r = requests.get(url, params=PAYLOAD)
    return r.json()


def get_backdrop_path(backdrop_api_path, size = 'w780'):
    base_url = 'https://image.tmdb.org/t/p/'
    return f"{base_url}{size}{backdrop_api_path}"


def get_single_movie_cast(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    r = requests.get(url, params=PAYLOAD)
    return r.json()['cast']


def get_movie_images(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    r = requests.get(url, params=PAYLOAD)
    return r.json()






if __name__ == '__main__':
    
    data = get_popular_movies()
    
    print(len(data['results']))
    print(data['results'])
    

    path = get_poster_url('/1g0dhYtq4irTY1GPXvft6k4YLjm.jpg')
    print(path)

    print(get_backdrop_path('/dK12GIdhGP6NPGFssK2Fh265jyr.jpg'))

    print("/")

    print(get_movie_images(928999)['backdrops'])

    print(get_movies())






