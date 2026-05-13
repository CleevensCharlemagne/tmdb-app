import argparse
from tmdb_app.api import fetch_movie


CATEGORIES = {
    "playing": "now_playing",
    "popular": "popular",
    "top": "top_rated",
    "upcoming": "upcoming"
}


def get_movies():
    parser = argparse.ArgumentParser(
        prog="tmdb-app",
        description="TMDB CLI App"
    )

    parser.add_argument(
        "--type",
        choices=CATEGORIES.keys(),
        required=True,
        help="Movie category"
    )

    args = parser.parse_args()

    return fetch_movie(CATEGORIES[args.type])