from tmdb_app.cli import get_movies


def main():
    data = get_movies()

    movies = data.get("results", [])

    for movie in movies:
        print(f"{movie['title']}:")

        for key, value in movie.items():
            print(f"\t{key}: {value}")

        print("-" * 100)


if __name__ == "__main__":
    main()