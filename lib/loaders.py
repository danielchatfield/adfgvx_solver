from funcs import *
import json
import re

"""
	Data loaders/generators
"""
class Crypt_Data_Loader():
	is_cached = False
	result    = {}
	raw_data  = ''

	@classmethod
	def get( cls ):
		if not cls.is_cached:
			cls.load()
		return cls.result

	@classmethod
	def load( cls ):
		file_path = cls.__name__
		if not data_exists( file_path ):
			cls.dump()
		cls.raw_data = get_data( file_path )
		cls.result   = cls.parse()

	@classmethod
	def dump( cls ):
		result = cls.generate()
		set_data( cls.__name__, json.dumps( result ) )


	@classmethod
	def generate( cls ):
		return {}

	@classmethod
	def parse( cls ):
		return json.loads( cls.raw_data )

	@classmethod
	def flush( cls ):
		cls.dump()
		cls.load()
		return cls.get()

class En_Letter_Count( Crypt_Data_Loader ):
	@classmethod
	def generate( cls ):
		return letter_count( get_en_sample() )

class En_Letter_Freq( Crypt_Data_Loader ):
	@classmethod
	def generate( cls ):
		return letter_freq( get_en_sample() )

class En_Tetragraph_Count( Crypt_Data_Loader ):
	@classmethod
	def generate( cls ):
		text = re.sub(r'\W+', '', get_en_sample() ).upper()
		text = re.sub(r'\d+', '', text)
		result = {}
		for i in range( len(text) - 4 ):
			tetra = text[i:i+4]
			if tetra not in result:
				result[tetra] = 0
			result[tetra] += 1
		return result

class En_Tetragraph_Freq( Crypt_Data_Loader ):
	@classmethod
	def generate( cls ):
		text = re.sub(r'\W+', '', get_en_sample() ).upper()
		text = re.sub(r'\d+', '', text)
		result = {}
		total = len(text) - 4
		for i in range( len(text) - 4 ):
			tetra = text[i:i+4]
			if tetra not in result:
				result[tetra] = 0
			result[tetra] += 1

		for tetra in result:
			result[tetra] = (result[tetra]*100*10000000 / total) / float(10000000)

		return result







