""" Module with finctions for transforming data """

def parse_data(movies: list, writers: list):
    """ Funcion parsing data """
    movies_resultset = []

    for movie in movies:
        movies_resultset.append({
            'id': movie['id'],
            'genre': movie['genre'],
            'director': drop_na(movie['director']),
            'description': movie['plot'],
            'imdb_rating': float(drop_na(movie['imdb_rating'], is_numeral=True)),
            'actors_ids': movie['actors_ids'].split(','),
            'actors_names': movie['actors_names'].split(','),
        })

    return movies_resultset


def drop_na(target: str, is_numeral: bool = False):
    """ Function for replace 'N/A' to None """
    if target == 'N/A':
        return 0 if is_numeral else None

    return target
