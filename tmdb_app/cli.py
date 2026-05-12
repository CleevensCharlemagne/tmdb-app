import argparse
from tmdb_app.api import fetch_movie


def get_movies():
    parser = argparse.ArgumentParser(
        prog="tmdb-app",
        description="TMDB CLI App"
    )

    parser.add_argument(
        "--type",
        choices=["popular", "top_rated", "upcoming", "playing"],
        required=True,
        help="Movie category"
    )

    args = parser.parse_args()

    if args.type == "playing":
        return fetch_movie('now_playing')
    elif args.type == "popular":
        return fetch_movie('popular')
    elif args.type == "top_rated":
        return fetch_movie('top_rated')
    elif args.type == "upcoming":
        return fetch_movie('upcoming')
    else:
        return None

