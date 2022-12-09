import getopt
import sys
import csv
import mysql.connector

VERBOSE = False
INPUT_FILE = ''
TABLE = ''

print('ARGV      :', sys.argv[1:])

options, remainder = getopt.getopt(sys.argv[1:], 'i:t:', ['input=','table='])
print('OPTIONS   :', options)
try:
    for opt, arg in options:
        if opt in ('-v', '--VERBOSE ='):
            VERBOSE = True
        elif opt in ('-t', '--table'):
            TABLE = arg
        elif opt in ('-i', '--input'):
            INPUT_FILE = arg
except:
    print("Please indicate the input CSV (-i) and the table (-t)")

# connecting to the database
dataBase = mysql.connector.connect(
                     host = "127.0.0.1",
                     user = "root",
                     password = "fonz",
                     database = "world" )
# preparing a cursor object
cursorObject = dataBase.cursor()
with open(INPUT_FILE) as CSV_FILE:
    CSV_READER = csv.reader( x.replace('\0','') for x in CSV_FILE)
    headers = [x.strip() for x in next(CSV_READER)]
    for row in CSV_READER:
        if row:
            d = dict(zip(headers, map(str.strip, row)))
            insert_query = "INSERT INTO " + TABLE + " VALUES ("
            for i in range(len(row)-1):
                insert_query += ("'" + row[i] + "',")
            insert_query +=("'" + row[len(row)-1] + "'")
            insert_query += ");"
            print(insert_query)
            QUERY = insert_query
            cursorObject.execute(QUERY)
            myresult = cursorObject.fetchall()
# Commit and disconnect
dataBase.commit()
dataBase.close()
