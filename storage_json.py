from istorage import IStorage
import json


class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path


    def get_movies(self):
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
            print('Can not access the database!')
        except json.decoder.JSONDecodeError:
            print('Database is empty!')
        except Exception as e:
            print(f'The following error has occurred: {e}')


    def list_movies(self, movies):
        print(f'{len(movies)} movies in total\n')
        for movie in movies:
            name, rating, year = tuple(movie.values())
            print(f'{name}, rating: {rating}, year: {year}')


    def add_movie(self, title, year, rating, movies, poster=0):
        with open(self.file_path, 'w') as file:
            movies.append({
                'Title': title,
                'Rating': rating,
                'Year of release': year
            })
            file.write(json.dumps(movies))


    def delete_movie(self, index, movies):
        with open(self.file_path, 'w') as file:
            movies.pop(index)
            file.write(json.dumps(movies))


    def update_movie(self, index, rating, movies):
        with open(self.file_path, 'w') as file:
            movies[index]['Rating'] = rating
            file.write(json.dumps(movies))


json_storage = StorageJson('data.json')
movies = json_storage.get_movies()
json_storage.list_movies(movies)
json_storage.update_movie(17, movies=movies, rating=8)
json_storage.list_movies(movies)