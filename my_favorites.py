"""This module makes available a harshly truncated list of my favorite
movies.  It does this through the use of the media.py module, and
making a list of those Movie objects.  Used by entertainment_center.py
"""

import media


holy_grail = media.Movie("Monty Python and the Holy Grail",
                         "https://upload.wikimedia.org/wikipedia/en/0/08/Monty"
                         "-Python-1975-poster.png",
                         "https://www.youtube.com/watch?v=LG1PlkURjxE",
                         )

naked_gun = media.Movie("Naked Gun",
                        "https://upload.wikimedia.org/wikipedia/en/6/68/"
                        "Nakedguntrilogy.jpg",
                        "https://www.youtube.com/watch?v=PACTQutbow4",)

hot_shots = media.Movie("Hot Shots",
                        "https://upload.wikimedia.org/wikipedia/en/b/b5/"
                        "Hot_Shots_2.jpg",
                        "https://www.youtube.com/watch?v=jGpOLb_PwYU",)


movies = [holy_grail, naked_gun, hot_shots]
