fsndp1
======

Python project to generate a list of movies with movie posters and links to their trailers.
-------------------------------------------------------------------------------------------

Starting with entertainment_center.py you will be asked for input in a terminal window - Do you want to see my favorite movies (type 'm'), or search for your favorite movies (type 's')?

If you search for your favorite, you will be given another option to input movie title keywords, for example, "star wars".

A search will be done using The Movie Database (TMDb)'s API.  As each matching movie is found, the terminal will output the name.  The most popular will be used to generate a browser window (in a new tab) displaying the title with a movie poster which is linked to a popout YouTube trailer video.

For more information on the API, see [TMDb API](https://www.themoviedb.org/documentation/api).

Control flow diagram
--------------------
A simple control flow structure to give you an idea how it works:

![structure diagram][diagram]

[diagram]: https://github.com/benuklove/fsndp1/blob/master/Simple_control_flow.png "Start at entertainment_center.py"

API Key
-------
You will need an API key to The Movie Database to access the API.  To obtain a key, follow these steps:

1. Register for and verify an [account](https://www.themoviedb.org/account/signup).
2. [Log into](https://www.themoviedb.org/login) your account.
3. Select the API section on left side of your account page.
4. Click on the link to generate a new API key and follow the instructions.
5. Put this key in the file tmdb.py for the variable 'key'.

Installation
------------
From the command line.  Make adjustments, if needed, for using an IDE. 

- Take a look at the next bullet, just in case you want to do that now.
1. Clone download this repository to your local machine's project directory.
2. Open a terminal window and cd into the project's directory.  
* If you haven't already, create a virtual environment for your project and activate it.
3. Make sure your you've installed proper dependencies (see requrements.txt).

Operation
---------
4. In a terminal at the project directory, type 'python entertainment_center.py'.  (without quotes of course)
5. Follow prompt.

Requirements
------------
Python 3 only
API key from The Movie Database (TMDb)
Package: requests

mention tmdbsimple




