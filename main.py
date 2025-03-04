from movie_app import MovieApp
from storage_json import StorageJson
from storage_csv import StorageCsv

storage = StorageCsv('data.csv')
movie_app = MovieApp(storage)
movie_app.run()