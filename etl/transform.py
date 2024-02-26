""" Module with finctions for transforming data """

import json


def transform(movies: list, writers: list):
    """ Funcion parsing data """
    movies_resultset = []
    writers = [{'id': w['id'], 'name': w['name']} for w in writers]

    for movie in movies:
        actors_ids = movie['actors_ids'].split(',')
        actors_names = movie['actors_names'].split(',')
        actors = [{'id': actors_ids[i], 'name': actors_names[i]} for i in range(len(actors_ids))]
        writers_ids = [movie['writer']] if movie['writer'] else [w['id'] for w in json.loads(movie['writers'])]
        movie_writers = list(filter(lambda w: w['id'] in writers_ids, writers))
        movies_resultset.append({
            'id': movie['id'],
            'genre': movie['genre'],
            'title': movie['title'],
            'director': drop_na(movie['director']),
            'description': movie['plot'],
            'imdb_rating': float(
                drop_na(movie['imdb_rating'], is_numeral=True)
            ),
            'actors': actors,
            'actors_names': ', '.join(actors_names),
            'writers': movie_writers,
            'writers_names': ', '.join(map(lambda w: w['name'], movie_writers))
        })

    return movies_resultset


def drop_na(target: str, is_numeral: bool = False):
    """ Function for replace 'N/A' to None """
    if target == 'N/A':
        return 0 if is_numeral else None

    return target
