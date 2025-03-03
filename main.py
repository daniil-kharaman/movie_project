from movie_app import MovieApp
from storage_json import StorageJson

storage = StorageJson('data.json')
movie_app = MovieApp(storage)
movie_app.run()