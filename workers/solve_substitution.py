from lib import *
import time

"""
	This file contains the functions to solve a substitution cipher
"""


def do_solve2( input ):
	key = [i for i in 'zyxwvutsrqponmlkjihgfedcba'.upper()]
	plaintext = decrypt_message(key, input)
	print plaintext
	tetragraph = tetragraph_freq( plaintext )
	print tetragraph_compare( tetragraph )

def do_solve( input ):

	#do_solve2( input )

	ciphertext = funcs.upper_alpha_only( input )
	best_proximity = 1000;
	best_key = funcs.generate_key()


	

	for k in range(10):
		## This code will be executed in a thread
		print 'new key'
		# first try key as-is
		key = funcs.generate_key()
		#key = [i for i in 'zyxwvutsrqponmlkjihgfedcba'.upper()]
		plaintext = decrypt_message( key, ciphertext )
		tetragraph = funcs.tetragraph_freq( plaintext )
		proximity_to_english = funcs.tetragraph_compare( tetragraph )
		#print proximity_to_english
		should_continue = True

		#print key

		if proximity_to_english < best_proximity:
			best_proximity = proximity_to_english
			best_key = key[:]

		# now try swapping

		while should_continue:
			old_key = key[:]
			start_time = time.time()
			for i in range(26):
				for j in range(i+1, 26):
					key_to_try = key[:]
					tmp = key_to_try[j]
					key_to_try[j] = key_to_try[i]
					key_to_try[i] = tmp

					plaintext = decrypt_message( key_to_try, ciphertext )
					tetragraph = funcs.tetragraph_freq( plaintext )
					new_proximity_to_english = funcs.tetragraph_compare( tetragraph )

					if new_proximity_to_english < 0.2
						# this is close so lets do some more stuff

					if new_proximity_to_english < proximity_to_english:
						# this key is better
						key = key_to_try
						proximity_to_english = new_proximity_to_english
			#print time.time() - start_time, "seconds"
			should_continue = ( old_key != key )
			if proximity_to_english < best_proximity:
				best_proximity = proximity_to_english
				best_key = key
				if best_proximity < 0.2:
					print decrypt_message( best_key, input )
			print proximity_to_english
		print best_proximity


	print decrypt_message( best_key, input )


	



def decrypt_message( key, ciphertext ):
	key_map = funcs.create_decryption_mapping(key)
	plaintext = ''
	for char in ciphertext:
		if char in key_map:
			plaintext += key_map[char]
		elif char.upper() in key_map:
			plaintext += key_map[char.upper()].lower()
		else:
			plaintext += char
	return plaintext