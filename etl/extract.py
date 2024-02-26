""" Module with finctions for extracting data from database """

import sqlite3


WRITERS_QUERY = """SELECT * FROM writers;"""

ALL_QUERY = """
SELECT
m.*,
w.name,
GROUP_CONCAT(a.name) AS actors_names,
GROUP_CONCAT(a.id) AS actors_ids
FROM movies m
JOIN movie_actors ma ON m.id = ma.movie_id
JOIN actors a ON ma.actor_id = a.id
LEFT JOIN writers w ON m.writer = w.id
GROUP BY m.id;
"""


def create_connection(db_name: str):
    """Function returning db connection."""
    return sqlite3.connect(db_name)


def retrive_data(conn: sqlite3.Cursor, query: str):
    """Function extracting data."""
    conn.row_factory = sqlite3.Row
    return conn.execute(query)


def get_movies_and_writers_tuple(db_name: str):
    """Function returning tuple of movies and writes."""
    dbc = create_connection(db_name)
    movies = retrive_data(dbc, ALL_QUERY)
    writers = retrive_data(dbc, WRITERS_QUERY)

    return movies, writers


def print_result(data):
    """Function printing data."""
    for row in data:
        print(*row, sep=' | ')
        print(row.keys())


if __name__ == '__main__':
    connection = create_connection('db.sqlite')
    moovies = retrive_data(connection, ALL_QUERY)
    writers = retrive_data(connection, WRITERS_QUERY)

    print_result(moovies)
    print_result(writers)
