import media
import fresh_tomatoes

warcraft = media.Movie(68735)

thor_ragnarok = media.Movie(284053)

logan = media.Movie(263115)

matrix = media.Movie(603)

interstellar = media.Movie(157336)

john_wick = media.Movie(245891)

movies = [warcraft, thor_ragnarok, logan, matrix, interstellar, john_wick]
fresh_tomatoes.open_movies_page(movies)
