from abc import ABC, abstractmethod


class IStorage(ABC):
    @abstractmethod
    def get_movies(self):

        """
        Returns a list of dictionaries that
        contains the movies information in the database.

        The function loads the information from the
        file and returns the data.
        """

        pass


    @abstractmethod
    def list_movies(self):

        """
        Getter function. Returns a list of dictionaries that
        contains the movies information.
        """

        pass


    @abstractmethod
    def add_movie(self, title, year, rating, poster):

        """
        Adds a movie to the movies database.
        Loads the information from the file, add the movie,
        and saves it. The function doesn't need to validate the input.
        """

        pass


    @abstractmethod
    def delete_movie(self, index):

        """
        Deletes a movie from the movies database.
        Loads the information from the file, deletes the movie,
        and saves it. The function doesn't need to validate the input.
        """

        pass


    @abstractmethod
    def update_movie(self, title, rating):

        """
        Updates a movie from the movies database.
        Loads the information from the file, updates the movie,
        and saves it. The function doesn't need to validate the input.
        """

        pass
