from abc import ABC, abstractmethod


class IStorage(ABC):
    @abstractmethod
    def get_movies(self):

        """
        Returns a list of dictionaries that
        contains the movies information in the database.

        The function loads the information from the JSON
        file and returns the data.
        """

        pass


    @abstractmethod
    def list_movies(self, movies):

        """Prints all movies from the database"""

        pass


    @abstractmethod
    def add_movie(self, title, year, rating, poster, movies):

        """
        Adds a movie to the movies database.
        Loads the information from the JSON file, add the movie,
        and saves it. The function doesn't need to validate the input.
        """

        pass


    @abstractmethod
    def delete_movie(self, index, movies):

        """
        Deletes a movie from the movies database.
        Loads the information from the JSON file, deletes the movie,
        and saves it. The function doesn't need to validate the input.
        """

        pass


    @abstractmethod
    def update_movie(self, title, rating, movies):

        """
        Updates a movie from the movies database.
        Loads the information from the JSON file, updates the movie,
        and saves it. The function doesn't need to validate the input.
        """

        pass
