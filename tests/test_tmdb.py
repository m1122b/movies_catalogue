
import sys
sys.path.append('../')

import tmdb_client
from unittest.mock import Mock


def test_get_poster_url_uses_default_size():
    # Przygotowanie danych
    poster_api_path = "/some-poster-path"
    expected_default_size = 'w342'
    # Wywołanie kodu, który testujemy
    poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)
    # Porównanie wyników
    assert expected_default_size in poster_url


def test_get_poster_url_uses_default_size_second():
    # Przygotowanie danych
    poster_api_path = '/some-poster-path'
    expected_default_size = 'w342'
    # Wywołanie kodu, który testujemy
    poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)
    # Porównanie wyników
    assert poster_url == 'https://image.tmdb.org/t/p/w342/some-poster-path'


def test_get_movies_list_type_popular():
    movies_list = tmdb_client.get_movies_list(list_type="popular")
    assert movies_list is not None


def test_get_movies_list(monkeypatch):
    # Lista, którą będzie zwracać przysłonięte "zapytanie do API"
    mock_movies_list = ['Movie 1', 'Movie 2', 'Movie 3']
    requests_mock = Mock()
    # Wynik wywołania zapytania do API
    r = requests_mock.return_value
    # Przysłaniamy wynik wywołania metody .json()
    r.json.return_value = mock_movies_list
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
    movies_list = tmdb_client.get_movies_list(list_type="popular")
    assert movies_list == mock_movies_list


def test_get_single_movie():
    movie_id = '508947'
    single_movie = tmdb_client.get_single_movie(movie_id)
    assert single_movie is not None


def test_get_movie_images():
    movie_id = '508947'
    single_movie = tmdb_client.get_movie_images(movie_id)
    assert single_movie is not None


def test_get_single_movie_cast():
    movie_id = '508947'
    single_movie = tmdb_client.get_single_movie_cast(movie_id)
    assert single_movie is not None


