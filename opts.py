from email import header
import getopt
import sys
import csv


VERBOSE = False
INPUT_FILE = ''

print('ARGV      :', sys.argv[1:])

options, remainder = getopt.getopt(sys.argv[1:], 'f:o:v:i:', ['input=', 'verbose=',
                                                            'version=','file=',])
print('OPTIONS   :', options)

for opt, arg in options:
    if opt in ('-v', '--VERBOSE ='):
        VERBOSE = True
    elif opt in ('-i', '--input'):
        INPUT_FILE = arg
   



with open(INPUT_FILE) as CSV_FILE:
    CSV_READER = csv.reader( x.replace('\0','') for x in CSV_FILE)
    
    headers = [x.strip() for x in next(CSV_READER)]
    table = input("Which table should the data be added to?: ")
    """
    table_query = "CREATE TABLE employee ("
    for i in range(len(headers)-1):
        table_query += (headers[i] + " VARCHAR(20) ")
    table_query += (headers[len(headers)-1] + "VARCHAR(20))")
    print("Table creation query is " + table_query)
    accept = input("Accept query?")
    if accept in ('Yes', 'yes', 'y', 'Y'):
        pass
    else:
        print("Enter alternate query")
        table_query = input("Please enter alternate query: ")

    
    print(table_query)
    """

    for row in CSV_READER:
        if row:
            d = dict(zip(headers, map(str.strip, row)))
            insert_query = "INSERT INTO " + table + " VALUES "
            
            for i in range(len(row)-1):
                insert_query += ("'" + row[i] + "',")
            insert_query +=("'" + row[len(row)-1] + "'")
                
            print(insert_query)



