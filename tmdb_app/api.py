import requests
import os

def fetch_movie(categorie):
    api_key = os.getenv("TMDB_API_KEY")
    url = f'https://api.themoviedb.org/3/movie/{categorie}?api_key={api_key}'

    response = requests.get(url)
    response.raise_for_status()

    return response.json()
