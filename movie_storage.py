import json
from main import error_colour

# movies_python = [
#         {
#             'Title': 'The Shawshank Redemption',
#             'Rating': 10,
#             'Year of release': 2000
#         },
#
#         {
#             'Title': 'Pulp Fiction',
#             'Rating': 10,
#             'Year of release': 1999
#         },
#
#         {
#             'Title': 'The Room',
#             'Rating': 10,
#             'Year of release': 2012
#         },
#
#         {
#             'Title': 'Star Wars: Episode V',
#             'Rating': 8.7,
#             'Year of release': 1995
#         }
#     ]

def get_movies():
    """
    Returns a list of dictionaries that
    contains the movies information in the database.

    The function loads the information from the JSON
    file and returns the data.
    """

    try:
        with open('data.json', 'r') as file:
            return json.loads(file.read())
    except FileNotFoundError:
        print(error_colour('Can not access the database!'))
    except json.decoder.JSONDecodeError:
        print(error_colour('Database is empty!'))
    except Exception as e:
        #changed error message here and in all other exceptions as well
        print(error_colour(f'The following error has occurred: {e}'))


def save_movies(movies):
    """Gets all your movies as an argument and saves them to the JSON file."""
    #TODO add exception
    with open('data.json', 'w') as file:
        file.write(json.dumps(movies))




def add_movie(title, year, rating, movies):
    """
    Adds a movie to the movies database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """
    # movies = get_movies()

    with open('data.json', 'w') as file:
        movies.append({
            'Title': title,
            'Rating': rating,
            'Year of release': year
        })
        file.write(json.dumps(movies))





def delete_movie(index):
    """
    Deletes a movie from the movies database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = get_movies()

    with open('data.json', 'w') as file:
        movies.pop(index)
        file.write(json.dumps(movies))


def update_movie(index, rating):
    """
    Updates a movie from the movies database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = get_movies()

    with open('data.json', 'w') as file:
        movies[index]['Rating'] = rating
        file.write(json.dumps(movies))
