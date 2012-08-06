import json
import re
import funcs

"""
	Data loaders/generators
"""
class Crypt_Data_Loader():
	is_cached = False
	result    = {}
	raw_data  = ''

	@classmethod
	def get( cls ):
		if cls.is_cached is False:
			cls.load()
		return cls.result

	@classmethod
	def load( cls ):
		file_path = cls.__name__
		if funcs.data_exists( file_path ) is False:
			cls.dump()
		cls.raw_data = funcs.get_data( file_path )
		cls.result   = cls.parse()
		cls.is_cached = True

	@classmethod
	def dump( cls ):
		result = cls.generate()
		funcs.set_data( cls.__name__, json.dumps( result ) )


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
		return funcs.letter_count( funcs.get_en_sample() )

class En_Letter_Freq( Crypt_Data_Loader ):
	@classmethod
	def generate( cls ):
		return funcs.letter_freq( funcs.get_en_sample() )

class En_Tetragraph_Count( Crypt_Data_Loader ):
	@classmethod
	def generate( cls ):
		return funcs.tetragraph_count( funcs.get_en_sample() )

class En_Tetragraph_Freq( Crypt_Data_Loader ):
	@classmethod
	def generate( cls ):
		return funcs.tetragraph_freq( funcs.get_en_sample() )







