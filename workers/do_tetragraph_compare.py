from lib import *

samples = {
	'wikipedia',
	'eileen',
	'hal',
	'tim'
}
tetragraph_compare_total = 0

for sample in samples:
	tetragraph = tetragraph_freq( get_en_sample( sample ) )
	tetragraph_compare_value = tetragraph_compare( tetragraph )
	tetragraph_compare_total += tetragraph_compare_value
	print tetragraph_compare_value

tetragraph_compare_value = tetragraph_compare_total / len(samples)

print ''
print len(samples)
print tetragraph_compare_value
#print 1 / tetragraph_compare_value

print ''
print ''

samples = range(2)
tetragraph_compare_total = 0

for sample in samples:
	tetragraph = tetragraph_freq( get_sample( '\\nonsense\\' + str(sample) + '.txt' ) )
	tetragraph_compare_value = tetragraph_compare( tetragraph )
	tetragraph_compare_total += tetragraph_compare_value
	print tetragraph_compare_value

tetragraph_compare_value = tetragraph_compare_total / len(samples)

print ''
print len(samples)
print tetragraph_compare_value
#print 1 / tetragraph_compare_value