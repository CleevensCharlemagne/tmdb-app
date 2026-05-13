import requests

def fetch_movie(categorie):
    api_key = '8190b66afc8c8d44a678007b06d5925b'
    url = f'https://api.themoviedb.org/3/movie/{categorie}?api_key={api_key}'

    response = requests.get(url)
    response.raise_for_status()

    return response.json()
