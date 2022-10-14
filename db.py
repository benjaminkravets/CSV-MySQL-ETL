
# importing required library
import mysql.connector
   
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

cursorObject.execute(query)
 
myresult = cursorObject.fetchall()
 
for x in myresult:
    print(x)
 
# disconnecting from server
dataBase.close()