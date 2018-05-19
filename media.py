import tmdbsimple


class Movie():
    """ This class fetches and stores movie information using the TMDb API. """

    # Assign API key for TMDb API // Please use your API key!
    tmdbsimple.API_KEY = '1263dbac5a813170b2f4bc9c8e9fb168'

    # Initialize the Movie class
    def __init__(self, movie_id):
        self.id = movie_id

    def fetch_title(self, movie_id):
        """
        Get the title for a specific movie id.
        Args:
            movie_id:(int) User specified movie id from entertainment_center.py
        Returns:
            A string that contains the movie title.
        """
        movie = tmdbsimple.Movies(movie_id)
        request = movie.info()

        return movie.title

    def fetch_story(self, movie_id):
        """
        Get the story for a specific movie id.
        Args:
            movie_id:(int) User specified movie id from entertainment_center.py
        Returns:
            A string that contains the movie story.
        """
        movie = tmdbsimple.Movies(movie_id)
        request = movie.info()

        return movie.overview

    def fetch_poster(self, movie_id):
        """
        Get the poster link for a specific movie id.
        Args:
            movie_id:(int) User specified movie id from entertainment_center.py
        Returns:
            A string that contains the movie poster link.
        """
        movie = tmdbsimple.Movies(movie_id)
        request = movie.info()

        poster = 'https://image.tmdb.org/t/p/w342/' + movie.poster_path
        return poster

    def fetch_trailer(self, movie_id):
        """
        Get the trailer key for a specific movie id.
        Args:
            movie_id:(int) User specified movie id from entertainment_center.py
        Returns:
            A string that contains the movie youtube key.
        """
        movie = tmdbsimple.Movies(movie_id)
        request = movie.videos()
        trailer = movie.results[0]['key']

        return trailer
