""" This files contains the class definition of Movie class
    with it's data members and a member function """
import webbrowser # This statements imports webbrowser packge from the python standard library
class Movie() :
    """ This class is used to store movie details.
    Attributes:
        title: A string which has the title of the movie.
        storyline: A string which has the basic plot of the movie.
        poster_image_url: A string which has the URL of the movie poster.
        trailer_youtube_url: A string which has the URL of the movie trailer.
        release_date: A string which has the release date of the movie.
        genre : A string which has the genre of the movie.
        imdb_rating : A string which has the IMDb rating for the movie.  
    """
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, movie_release_date, movie_genre,
                 movie_imdb_rating):
        """ This constructor initialises the instance variables of class Movie """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = movie_release_date
        self.genre = movie_genre
        self.imdb_rating = movie_imdb_rating
        
    def show_trailer(self):
        """ This function opens the movie's youtube trailer on a web browser """
        webbrowser.open(self.trailer_youtube_url)
        
        
        
