import fresh_tomatoes
import media


toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")
# print(toy_story.storyline)
# toy_story.show_trailer()

school_of_rock = media.Movie("School of Rock",
                             "Using rock music to learn",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

holy_grail = media.Movie("Monty Python and the Holy Grail",
                         "Another film completely different than some of the other films which aren't\
                          quite the same as this on is",
                         "https://upload.wikimedia.org/wikipedia/en/0/08/Monty-Python-1975-poster.png",
                         "https://www.youtube.com/watch?v=LG1PlkURjxE"
                         )

spaceballs = media.Movie("Spaceballs",
                         "Once upon a time warp in deep space, the struggle between the nice & the rotten goes on...",
                         "https://upload.wikimedia.org/wikipedia/en/4/45/Spaceballs.jpg",
                         "https://www.youtube.com/watch?v=RUnhzwnn_Q0")

naked_gun = media.Movie("Naked Gun",
                        "From the files of Police Squad",
                        "https://upload.wikimedia.org/wikipedia/en/6/68/Nakedguntrilogy.jpg",
                        "https://www.youtube.com/watch?v=PACTQutbow4")

hot_shots = media.Movie("Hot Shots",
                        "Unprecedented! Uncut! Under ten dollars! The mother of all movies!",
                        "https://upload.wikimedia.org/wikipedia/en/b/b5/Hot_Shots_2.jpg",
                        "https://www.youtube.com/watch?v=jGpOLb_PwYU")


movies = [holy_grail, spaceballs, naked_gun, hot_shots]

fresh_tomatoes.open_movies_page(movies)
