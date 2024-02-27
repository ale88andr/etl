""" Module with finctions for transforming data """

import json


def transform(movies: list, writers: list):
    """ Funcion parsing data """
    resultset, writers = [], [dict(w) for w in writers]

    for movie in movies:
        actors_ids = movie['actors_ids'].split(',')
        actors_names = movie['actors_names'].split(',')

        writers_ids = movie['writer'] or [w['id'] for w in
                                          json.loads(movie['writers'])]
        movie_writers = list(filter(lambda w: w['id'] in writers_ids, writers))

        resultset.append({
            'id': movie['id'],
            'genre': movie['genre'],
            'title': movie['title'],
            'director': drop_na(movie['director']),
            'description': movie['plot'],
            'imdb_rating': float(
                drop_na(movie['imdb_rating'], is_numeral=True)
            ),
            'actors': [{'id': actors_ids[i], 'name': actors_names[i]}
                       for i in range(len(actors_ids))],
            'actors_names': ', '.join(actors_names),
            'writers': movie_writers,
            'writers_names': ', '.join(map(lambda w: w['name'], movie_writers))
        })

    return resultset


def drop_na(target: str, is_numeral: bool = False):
    """ Function for replace 'N/A' to None or 0 """
    if target == 'N/A':
        return 0 if is_numeral else None

    return target
