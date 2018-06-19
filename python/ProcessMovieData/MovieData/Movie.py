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

class Movie( object ):
    '''
    This class holds the data associated with a movie
    '''

    def __init__( self, data ):
        '''
        Constructor
        '''
        
        self.data = data
        
    def returnDataFields( self ):
        return dataMappings
    
    def storeData( self ):
        return

        