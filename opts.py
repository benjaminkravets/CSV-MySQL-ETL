import getopt
import sys
import csv

VERSION = '1.0'
VERBOSE = False
INPUT_FILE = ''

print('ARGV      :', sys.argv[1:])

options, remainder = getopt.getopt(sys.argv[1:], 'f:o:v:', ['output=', 'verbose=',
                                                            'version=','file=',])
print('OPTIONS   :', options)

for opt, arg in options:
    if opt in ('-v', '--VERBOSE ='):
        VERBOSE = True
    elif opt == '--version':
        VERSION = arg
    elif opt in ('-f', '--file'):
        INPUT_FILE = arg

with open(INPUT_FILE, 'r') as USER_CSV:
    READER = csv.reader(USER_CSV, delimiter=' ', quotechar='|')
    for row in READER:
        print(row)





