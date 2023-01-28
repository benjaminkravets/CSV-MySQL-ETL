import getopt
import sys
import csv
import mysql.connector

"""Script to take a CSV file and generate insertion statements for a MySQL database"""

VERBOSE = False
INPUT_FILE = ''
TABLE = ''

# preparing a cursor object

with open("TQQQ.csv") as CSV_FILE:
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
            
            
# Commit and disconnect
