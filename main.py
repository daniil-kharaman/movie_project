from movie_app import MovieApp
from storage.storage_json import StorageJson

storage = StorageJson('data/data.json')
# storage = StorageCsv('data/data.csv')
movie_app = MovieApp(storage)
movie_app.run()