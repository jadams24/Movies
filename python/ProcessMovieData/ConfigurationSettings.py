#---------------------------------------------------
# ConfigurationSettings.py
#---------------------------------------------------

import json
import os
import unittest

CONFIG_JSON_FILE = 'Settings/settings.json'

class ConfigurationSettings:

	def __init__( self ):
		currentPath = os.path.dirname(os.path.realpath(__file__))

		path = os.path.join(currentPath, CONFIG_JSON_FILE)
		print(path)
 
		f = open(path, 'r')
		self.data = json.load(f)

	#---------------------------------------------------
	# value accessors
	#---------------------------------------------------

	def getMovieLocation( self ):
		return self.data["MovieFileLocation"]

	def getOmdbApiKey( self ):
		return self.data["Omdb"]["ApiKey"]

	def getOmdbBaseUrl( self ):
		return self.data["Omdb"]["UrlBase"]
	
	def getMovieJsonFields( self ):
		return self.data["Omdb"]["MovieJsonFields"]
	
	def getPersonJsonFields( self ):
		return self.data["Omdb"]["PersonJsonFields"]
	
	def getDataMapping( self, table ):
		return self.data["Database"]["DataMappings"][table]
	
	def getDataTables( self ):
		tables = self.data["Database"]["DataMappings"]
		return tables.keys()

#---------------------------------------------------
# ConfigurationFileTestCase
#---------------------------------------------------

class ConfigurationFileTestCase( unittest.TestCase ):

	def setUp( self ):
		print("in setup")

	def tearDown( self ):
		print("in tearDown")

	def runTest( self ):
		''' Testing ConfigurationFile module'''

		#---------------------------------------------------
		# test the simple accessor methods
		#---------------------------------------------------


#---------------------------------------------------
# main()
#---------------------------------------------------

if __name__ == '__main__':

	unittest.TextTestRunner().run( ConfigurationFileTestCase() )