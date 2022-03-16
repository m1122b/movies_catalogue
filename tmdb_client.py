
from random import choices
import requests


def get_popular_movies():
    payload = {'api_key': 'de232542034b3603e0d8b59a43a78c8f', 'language': 'en-US', 'page': '1'}
    url = 'https://api.themoviedb.org/3/movie/popular'
    r = requests.get(url, params=payload)
    return r.json()


def get_poster_url(poster_api_path, size = 'w342'):
    base_url = 'https://image.tmdb.org/t/p/'
    return f"{base_url}{size}{poster_api_path}"


def get_movies(how_many):
    data = choices(get_popular_movies()['results'], k=how_many)
    return data


if __name__ == '__main__':
    
    data = get_popular_movies()
    
    print(len(data['results']))
    print(data['results'])
    

    path = get_poster_url('/1g0dhYtq4irTY1GPXvft6k4YLjm.jpg')
    print(path)
    






