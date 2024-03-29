""" Main script """

from etl import get_movies_and_writers_tuple, transform, load


def main():
    """ Manage function """
    movies, writers = get_movies_and_writers_tuple('db.sqlite')
    result = transform(movies, writers)
    load(result)


if __name__ == '__main__':
    main()
