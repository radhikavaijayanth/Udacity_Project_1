# Udacity_Project_1 - Movie Trailer Website
# Description
- The Movie Trailer Website project consists of server-side code to store a list of movies titles, along with its respective box art imagery,storyline,genre,release date,IMDb rating and movie trailer website. 
- Before the web page appears, a dropdown popup with options for the users to choose the sorting method to display the movies in the web page is shown.
- Based on the option chosen by the user, the order in which the movies have to be displayed is got.
- The data is served as a web page allowing visitors to review the movies and watch the trailers.
# Installation
- Python 2.x is required to run this project. 
- Download the zip file of the project.
- Unzip it and save them in a folder location.
- This project consists of the following files:
    - entertainment_center.py - Stores the details of the movie objects
    - media.py - Stores the class definition of class Movie with it's data members and member function.
    - fresh_tomatoes.py - This has the code to render the movie details in a web browser.
- Open terminal in Linux/Mac and command prompt in Windows
- Move to the directory which has the project files
- Type python entertainment_center.py
# Usage
- After you execute the program using the above command the following happens:
- A dropdown popup listing the sorting option appears
  - Alphabetical - Sorts the movies in the alphabetical order of their titles.
  - None - No sorting is applied
  - IMDb - Sorts the movies in the reverse oder of IMDb rating (highest to lowest)
  - If no option is selected from the dropdown it is sorted in the alphabetical order of movie titles
- Once you choose the option, close the dropdown popup by clicking it's close button on the left top corner.
- After you close the dropdown popup, the web bage is rendered on the browser with the movies contents.
- The movies will be displayed in the order that was chosen by the user with it's poster image,title,storyline,release date,genre and IMDb rating.
- When the user clicks on the movie poster image he can watch the movie's youtube trailer.
# Improvements done to the project
- A dropdown menu for the user to choose the sort option was created and the web page is rendered accordingly.
- In addition to title and poster image,storyline,release date,genre and IMDb rating are also displayed.
# Extra Notes
- This program uses Tkinter module that is there in python versions 2.x


