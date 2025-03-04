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
                    #float int
                    parsed_movies.append({
                        'Title': row['Title'],
                        'Rating': float(row['Rating']),
                        'Year of release': int(row['Year of release'])
                    })
                if len(parsed_movies) == 0:
                    raise Exception('Database is empty!')
                return parsed_movies
        except FileNotFoundError:
            print('Can not access the database!')

        except Exception as e:
            print(f'The following error has occurred: {e}')

    #
    def list_movies(self):
        movies = self.get_movies()
        print(f'{len(movies)} movies in total\n')
        for movie in movies:
            name, rating, year = tuple(movie.values())
            print(f'{name}, rating: {rating}, year: {year}')



    def add_movie(self, title, year, rating, poster=0):
        with open(self.file_path, 'a', newline='') as file:
            fieldnames = ['Title', 'Rating', 'Year of release']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'Title': title, 'Rating': rating, 'Year of release': year})



    def delete_movie(self, index):
        movies = self.get_movies()
        movies.pop(index)
        with open(self.file_path, 'w') as file:
            fieldnames = ['Title', 'Rating', 'Year of release']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(movies)


    def update_movie(self, index, rating):
        movies = self.get_movies()
        movies[index]['Rating'] = rating
        with open(self.file_path, 'w') as file:
            fieldnames = ['Title', 'Rating', 'Year of release']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(movies)


# st = StorageCsv('data.csv')
# st.list_movies()
# st.update_movie(17, 10)
# st.list_movies()

