'''
Created on May 30, 2018

@author: root
'''

# data field mappings
dataMappings = {
    'FirstName':'first_name',
    'LastName':'last_name'
}

jsonFields = ['Actor', 'Writer', 'Director']

class PersonObj(object):
    '''
    This class holds the data associated with a person, e.g. actor, director, writer, etc.
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        