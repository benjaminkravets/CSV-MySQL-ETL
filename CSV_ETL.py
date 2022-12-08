from email import header
import getopt
import sys
import csv
import mysql.connector
from os import listdir



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
   

# connecting to the database
dataBase = mysql.connector.connect(
                     host = "127.0.0.1",
                     user = "root",
                     password = "fonz",
                     database = "world" )
   
# preparing a cursor object
cursorObject = dataBase.cursor()
   
# selecting query
query = "SELECT ID FROM CITY"
query += " LIMIT 10"
print(query)

#cursorObject.execute(query)
 
#myresult = cursorObject.fetchall()
 
#for x in myresult:
#    print(x)
 
# disconnecting from server
dataBase.close()




with open(INPUT_FILE) as CSV_FILE:
    CSV_READER = csv.reader( x.replace('\0','') for x in CSV_FILE)
    
    headers = [x.strip() for x in next(CSV_READER)]
    table = input("Which table should the data be added to?: ")


    for row in CSV_READER:
        if row:
            d = dict(zip(headers, map(str.strip, row)))
            insert_query = "INSERT INTO " + table + " VALUES "
            
            for i in range(len(row)-1):
                insert_query += ("'" + row[i] + "',")
            insert_query +=("'" + row[len(row)-1] + "'")
                
            print(insert_query)




