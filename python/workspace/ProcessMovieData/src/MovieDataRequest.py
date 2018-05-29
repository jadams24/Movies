import json
import os
import requests

def getMovieData():
    resp = requests.get('http://www.omdbapi.com/?t=The+Wild+Bunch&y=1969&apikey=6e689c60')
    
    if resp.status_code != 200:
        # This means something went wrong.
        # raise ApiError('GET /tasks/ {}'.format(resp.status_code))
        print('error: %s' % resp.status_code)
        
    t = json.loads(resp.content)
    keys = list(t.keys())
#    for item in resp.json():
#        print(item['Title'], item['Plot'])
    for key in keys:
    #There is state is field of database
        print(key, t[key])

def fileRead():
    print('fileRead')
    
    dirlist = os.listdir("/home/melkor/Videos/movies")
    for f in dirlist:
        print(f)
        
def main():
    print "Hello World 2"
    
    getMovieData()
    fileRead()

if __name__ == '__main__':
    main()

    print("Hello World 1")





