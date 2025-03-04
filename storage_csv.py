from istorage import IStorage
import csv


class StorageCsv(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path


    def get_movies(self):
        try:
            with open(self.file_path, 'r') as file:
                reader = csv.DictReader(file)
                parsed_movies = []
                for row in reader:
                    parsed_movies.append({
                        'Title': row['Title'],
                        'Rating': float(row['Rating']),
                        'Year': int(row['Year']),
                        'Poster': row['Poster']
                    })
                if len(parsed_movies) == 0:
                    raise Exception('Database is empty!')
                return parsed_movies
        except FileNotFoundError:
            print('Can not access the database!')
        except Exception as e:
            print(f'The following error has occurred: {e}')


    def list_movies(self):
        movies = self.get_movies()
        print(f'{len(movies)} movies in total\n')
        for movie in movies:
            name, rating, year, poster = tuple(movie.values())
            print(f'{name}, rating: {rating}, year: {year}, poster: {poster}')


    def add_movie(self, title, year, rating, poster):
        with open(self.file_path, 'a', newline='') as file:
            fieldnames = ['Title', 'Rating', 'Year', 'Poster']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'Title': title, 'Rating': rating, 'Year': year, 'Poster': poster})


    def delete_movie(self, index):
        movies = self.get_movies()
        movies.pop(index)
        with open(self.file_path, 'w') as file:
            fieldnames = ['Title', 'Rating', 'Year', 'Poster']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(movies)


    def update_movie(self, index, rating):
        movies = self.get_movies()
        movies[index]['Rating'] = rating
        with open(self.file_path, 'w') as file:
            fieldnames = ['Title', 'Rating', 'Year', 'Poster']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(movies)
