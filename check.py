import sys, pickle
from HoneyBadgerBFT.commoncoin.boldyreva import *


input_filename = sys.argv[1]
input_file = open(input_filename, 'r')
env = pickle.load(input_file)

print "start checking"
if check(env['n'], env['k'], env['h'], env['PK'], env['SKs'], env['sigs']):
    print 'pass'
else :
    print 'fail'
