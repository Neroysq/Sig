from HoneyBadgerBFT.commoncoin import *
import cPickle as pickle
import sys, math, time

log_filename = 'gen.log'
log_file = open(log_filename, 'w')

plan = {
'n': [3, 6, 10, 30, 60, 100, 300, 600, 1000, 3000, 6000, 10000, 30000, 60000, 1000000],
'fk': [0.6, 2./3., 0.7, 0.75, 0.8, 0.85]
}

for n in plan['n'] :
	for fk in plan['fk'] :
		k = (int)(math.ceil(n * fk))
		output_filename = 'sig-' + str(n) + '-' + str(k)
		output_file = open(output_filename, 'w')
		start_time = time.time()
		print "Generating: (%s, %s)" % (n, k)
		output = boldyreva.gen(n, k, 'hi')
		pickle.dump(output, output_file)
		#print >>output_file, output
		duration = time.time() - start_time
		print 'Completed in %s seconds' % (duration)
		log_file.write(str(n) + ' ' + str(k) + ' ' + str(duration) + '\n')
		output_file.close()

#output_filename = 'test.txt'
#output_file = open(output_filename, 'w')

#output = {
#'n':10,
#'k':6,
#'m':"hi",
#'sigs':boldyreva.gen(10, 6, "hi")
#}
#print >>output_file, output

print "OK"
