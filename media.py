import tmdbsimple


class Movie():
    """ The Movie class fetches and stores movie information using the TMDb API. """

    # Assign API key for TMDb API // Please use your API key!
    tmdbsimple.API_KEY = '1263dbac5a813170b2f4bc9c8e9fb168'

    def __init__(self, movie_id):
        self.id = movie_id

    # Functions to fetch movie title, story overview,
    # poster image, youtube key

    def fetch_title(self, movie_id):
        movie = tmdbsimple.Movies(movie_id)
        request = movie.info()

        return movie.title

    def fetch_story(self, movie_id):
        movie = tmdbsimple.Movies(movie_id)
        request = movie.info()

        return movie.overview

    def fetch_poster(self, movie_id):
        movie = tmdbsimple.Movies(movie_id)
        request = movie.info()

        poster = 'https://image.tmdb.org/t/p/w342/' + movie.poster_path
        return poster

    def fetch_trailer(self, movie_id):
        movie = tmdbsimple.Movies(movie_id)
        request = movie.videos()
        trailer = movie.results[0]['key']

        return trailer
