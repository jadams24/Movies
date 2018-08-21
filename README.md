# Movies

This is the source, database scripts, models, etc, plus source code for a web site that serves as a media server.

Also, includes support scripts for gleaning the movie files and getting data on them.

This project involves taking DVDs I own and converting them to *.mp4 format. The python scripts parse the movie titles from the file name and using the REST api from the Open Movie Database web site, the python code retrieves the data for the movie. The data is then stored in a local MySql database.

Ultimately a web site will reside on the same server as the MySql database and provide a media server so I can watch the movies straight from the server and not have to deal with the DVDs.

This is in the preliminary stages and is supposed to be used as a personal media server (07/04/18).
