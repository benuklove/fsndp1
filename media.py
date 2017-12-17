"""This module defines the class Movie.
Used by tmdb.py and my_favorites.py
"""

import webbrowser


class Movie:
    """Defines the Movie class for instantiating multiple movies.
    It requires three arguments: movie_title, poster_image,
    trailer_youtube.  These are the instance variables.
    The Movie class also has one method, show_trailer, that will open
    a web browser to show trailer_youtube.
    """
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
