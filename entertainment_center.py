import fresh_tomatoes
import mediaxx

toy_story = mediaxx.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")
#print(toy_story.storyline)
red_dead = mediaxx.Movie("Red Dead Redemption",
                     "A story of how the west was won",
                     "http://media.rockstargames.com/rockstargames/img/global/news/upload/actual_1467740579.jpg",
                     "https://www.youtube.com/watch?v=AUXGW6sWYDY")
#print(avatar.storyline)
#avatar.show_trailer()                     

DBZ = mediaxx.Movie("DBZ",
                    "Trucks against all it all",
                    "https://upload.wikimedia.org/wikipedia/en/7/73/CoverhistoryTrunks.jpg",
                    "https://www.youtube.com/watch?v=c-UCyrqaA3g")

Rudo = mediaxx.Movie("Rudo y Cursi",
                      "A story about love and futbol!!!!",
                      "http://www.gstatic.com/tv/thumb/movies/75786/75786_aa.jpg",
                      "https://www.youtube.com/watch?v=fKZAWvs9qpY")

#print(DB.storyline)
#DB.show_trailer()

Monty = mediaxx.Movie("Monty Python and The Holy Grail",
                             "one of the best comedies ever",
                             "http://lsc.mit.edu/schedule/2014.2q/poster-montypythonandtheholygrail.jpg",
                             "https://www.youtube.com/watch?v=urRkGvhXc8w")


#print(Monty.storyline)
#Monty.show_trailer()

Baseketball = mediaxx.Movie("BASEketball",
                      "your life is spinning out of control",
                      "http://www.gstatic.com/tv/thumb/movieposters/21409/p21409_p_v8_aa.jpg",
                      "https://www.youtube.com/watch?v=INXAe5I42CM")
#print(Gohan.storyline)
#Gohan.show_trailer()
movies = [toy_story, red_dead, DBZ, Rudo, Monty, Baseketball]

#fresh_tomatoes.open_movies_page(movies)
print(mediaxx.Movie.VALID_RATINGS)
