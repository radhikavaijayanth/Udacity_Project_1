"""Contains movie details to be displayed on a website."""

import media
import fresh_tomatoes

""" Creates six Movie objects, instantiates these objects with title, storyline,
    poster image link, video trailer link,release date,
    genre and imdb rating out of 10. """

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that comes to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        "July 22, 1995",
                        "Fantasy",
                        8)
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ",
                     "December 18, 2009",
                     "Science Fiction",
                     7)
foftf = media.Movie("Fate of the Furious",
                    " A story of a man with amazing car racing skills",
                    "https://upload.wikimedia.org/wikipedia/en/2/2d/The_Fate_of_The_Furious_Theatrical_Poster.jpg",
                    "https://www.youtube.com/watch?v=JwMKRevYa_M",
                    "April 14, 2017",
                    "Crime Thriller",
                    6)
school_of_rock = media.Movie("School of Rock",
                             "Story about an overly enthusiastic guitarist Dewey Finn",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc",
                             "September 24, 2003",
                             "Musical Commedy",
                             5)
ratatouille = media.Movie("Ratatouille",
                          "A story of a rat which aspires to become a chef ",
                          "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk",
                          "June 29, 2007",
                          "Drama",
                          10)
hunger_games = media.Movie("Hunger Games",
                           "A story of a girl who plays the hunger game",
                           "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=4S9a5V9ODuY",
                           "March 23, 2012",
                           "Science Fiction",
                           9)


# Stores the 6 movies objects in a list 
movies = [toy_story,avatar,foftf,school_of_rock,ratatouille,hunger_games]

# This functions takes the  movie list as input and renders the output in a web browser
fresh_tomatoes.open_movies_page(movies)



