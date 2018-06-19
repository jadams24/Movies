import json
import MovieData
import os
import requests
from ConfigurationSettings import ConfigurationSettings

def getMovieData( movieList, cfg ):
    
#    urlBase = 'http://www.omdbapi.com/?t='
#    apiKey = '&apikey=6e689c60'
    # get base URL & API key from cfg object
    urlBase = cfg.getOmdbBaseUrl()
    apiKey = cfg.getOmdbApiKey()

    # get the json fields from the call to OMDB that 
    # will be used to store the data returned from OMDB
    movieJsonFields = cfg.getMovieJsonFields()    
    personJsonFields = cfg.getPersonJsonFields()
    
    # initialize dictionaries     
    movieData = {}
    personData = {}
    
    for movie in movieList.keys():
        movie = movie.replace("_", "+")
        movie = movie.replace(".mp4", "")
        urlApiCall = urlBase.format(movie, apiKey)
        print(urlApiCall)
        
        resp = requests.get(urlApiCall)
    
    
#    resp = requests.get('http://www.omdbapi.com/?t=The+Wild+Bunch&y=1969&apikey=6e689c60')
    
        if resp.status_code != 200:
            # This means something went wrong.
            # raise ApiError('GET /tasks/ {}'.format(resp.status_code))
            print('error: %s' % resp.status_code)
            return
            
        t = json.loads(resp.content)
        keys = list(t.keys())
        for key in keys:
            if key in movieJsonFields:
                # current key is part of the json field to store
                # so add key and it's value to movieData dictionary
                movieData[key] = t[key]
            elif key in personJsonFields:
                # add key and it's value to personData dictionary
                personData[key] = t[key]
            
        print(movieData)
        
        # create movie object & store it in a list
        
        # create person object & store it in a list


def fileRead( cfg ):
    print('fileRead')
    
    dirlist = {}
        
    # reads a directory and then prints out all 
    # files in that directory and all sub-directories.
    start_path = cfg.getMovieLocation()
#    start_path = '/home/melkor/Videos' # current directory

    for path, dirs, files in os.walk(start_path):
        for filename in files:
            if filename.find(".mp4"):
                print os.path.join(path,filename)
                dirlist[filename] = os.path.join(path,filename)
    
    return dirlist

def main():
    print "Hello World 2"
    
    print(os.getcwd())
    
        # set the cfg object
    cfg = ConfigurationSettings()
       
    movieList = fileRead( cfg )
    getMovieData( movieList, cfg )

#    fileRead2()

if __name__ == '__main__':
    main()

    print("Hello World 1")





