
# importing module

from getopt import getopt
import cx_Oracle


 
# Create a table in Oracle database
try:
 
    con = cx_Oracle.connect('SYSTEM/1@localhost:1521/xe')
    print(con.version)
 
    # Now execute the sqlquery
    cursor = con.cursor()
 
    # Creating a table 
    
    #cursor.execute(
    #    "create table employee(empid integer primary key, name varchar2(30), salary number(10, 2))")
    cursor.execute("select * from employee")

    row = cursor.fetchone()
    print(row)

    print("Selection successful.")
 
except cx_Oracle.DatabaseError as e:
    print("There is a problem with Oracle", e)
 
# by writing finally if any error occurs
# then also we can close the all database operation
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()