from email import header
import getopt
import sys
import csv
from unittest import result

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


with open(INPUT_FILE) as CSV_FILE:
    CSV_READER = csv.reader( x.replace('\0','') for x in CSV_FILE)
    headers = [x.strip() for x in next(CSV_READER)]
    print(headers)
    for row in CSV_READER:
        if row:
            d = dict(zip(headers, map(str.strip, row)))
            query = "INSERT INTO EMPLOYEES VALUES "
            for i in range(len(row)):
                query += ("'" + row[i] + "',")
            print(query)



