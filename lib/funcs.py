import string
import os
import json

"""
Statistics
"""






"""
	General cryptography functions
"""

def get_letter_dict():
	"""
		Returns a dictionary with uppercaser letter keys and 0 as the elements
	"""
	return {
		'A': 0,
		'B': 0,
		'C': 0,
		'D': 0,
		'E': 0,
		'F': 0,
		'G': 0,
		'H': 0,
		'I': 0,
		'J': 0,
		'K': 0,
		'L': 0,
		'M': 0,
		'N': 0,
		'O': 0,
		'P': 0,
		'Q': 0,
		'R': 0,
		'S': 0,
		'T': 0,
		'U': 0,
		'V': 0,
		'W': 0,
		'X': 0,
		'Y': 0,
		'Z': 0
	}

def letter_count( text ):
	"""
		Performs a frequency analysis and returns a dictionary of letter => count
	"""
	chars = string.ascii_uppercase
	text = text.upper()
	result = get_letter_dict()
	for char in chars:
		result[char] = text.count(char)
	return result

def letter_freq( text ):
	"""
		Performs a frequency analysis and returns a dictionary of letter => percentage
	"""
	chars = string.ascii_uppercase
	text = text.upper()
	result = get_letter_dict()
	total = 0
	for char in chars:
		count = text.count(char)
		result[char] = count
		total += count
	if total != 0:
		for char in chars:
			result[char] = (result[char]*10000 / total) / float(100)
	return result

"""
	IO functions
"""

def get_resource( file_path ):
	base_dir = get_base_dir()
	file_path = os.path.join( base_dir, file_path )
	return open(file_path).read()

def set_resource( file_path, data ):
	base_dir = get_base_dir()
	file_path = os.path.join( base_dir, file_path )
	f = open(file_path, 'w')
	f.write(data)
	f.close()

def resource_exists( file_path ):
	base_dir = get_base_dir()
	file_path = os.path.join( base_dir, file_path )
	return os.path.exists( file_path )

def get_sample( file_path ):
	return get_resource( 'samples\\' + file_path )

def get_data( file_path, ext = '.txt' ):
	return get_resource( 'data\\' + file_path + ext )

def set_data( file_path, data, ext = '.txt' ):
	return set_resource( 'data\\' + file_path + ext, data )

def data_exists( file_path, ext = '.txt' ):
	return resource_exists( 'data\\' + file_path + ext )

def get_en_sample( sample_name = 'mississippi', ext = '.txt' ):
	return get_sample( 'en\\' + sample_name + ext )

def get_base_dir():
	return 'D:\\Projects\\EPQ\\adfgvx_solver\\res\\'
	if '__file__' in globals():
		return os.path.dirname(__file__)
	else:
		return 'D:\\Projects\\EPQ\\adfgvx_solver\\res\\'
