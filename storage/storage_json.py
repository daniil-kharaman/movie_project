from storage.istorage import IStorage
import json


class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path
        self._movies = self.get_movies()


    def get_movies(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print('Can not access the database!')
        except json.decoder.JSONDecodeError:
            print('Database is empty!')
        except Exception as e:
            print(f'The following error has occurred: {e}')


    @property
    def list_movies(self):
        return self._movies


    """
    Should I anyway check if I can access file here? Because I check it in get_movies function and if file was not
    found the class will be not instantiated.
    
    And should I validate parameters here as well? Because I validate them in movie_app.py. And only if they are valid 
    they are given over to these functions.
    """

    def add_movie(self, title, year, rating, poster):
        try:
            with open(self.file_path, 'w') as file:
                self._movies.append({
                    'Title': title,
                    'Rating': float(rating),
                    'Year': int(year),
                    'Poster': poster
                })
                file.write(json.dumps(self._movies))
        except FileNotFoundError:
            print('Can not access the database!')
        except Exception as e:
            print(f'The following error has occurred: {e}')


    def delete_movie(self, index):
        try:
            with open(self.file_path, 'w') as file:
                self._movies.pop(index)
                file.write(json.dumps(self._movies))
        except FileNotFoundError:
            print('Can not access the database!')
        except Exception as e:
            print(f'The following error has occurred: {e}')


    def update_movie(self, index, rating):
        try:
            with open(self.file_path, 'w') as file:
                self._movies[index]['Rating'] = rating
                file.write(json.dumps(self._movies))
        except FileNotFoundError:
            print('Can not access the database!')
        except Exception as e:
            print(f'The following error has occurred: {e}')
