'''
Created on May 30, 2018

@author: jadams24
'''

# data field mappings
dataMappings = {
    'Title':'title',
    'Plot':'plot',
    'Released':'release_year',
    'Rated':'rating',
    'Runtime':'runtime'
}

jsonFields = [
    'Title', 
    'Plot', 
    'Released', 
    'Rated', 
    'Runtime'
]

class Movie(object):
    '''
    This class holds the data associated with a movie
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
        
    def returnDataFields(self):
        return dataMappings
        