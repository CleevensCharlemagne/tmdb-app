from tmdb_app.cli import get_movies


def main():
    movies = get_movies()['results']

    for movie in movies:
        print(f'{movie['title']} :')

        for info, data in movie.items():
            print(f'\t{info} : {data}')

        print("-"*200)

if __name__ == '__main__':
    main()
