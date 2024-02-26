""" Main script """

from etl import get_movies_and_writers_tuple, parse_data


def main():
    """ Main function """
    movies, writers = get_movies_and_writers_tuple('db.sqlite')
    result = parse_data(movies, writers)

    print(result)


if __name__ == '__main__':
    main()
