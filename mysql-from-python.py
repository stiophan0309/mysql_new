import os
import datetime
import pymysql

# Get username from cloud9 workspace
# (modify this variable if running on another environment)

username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

try:
    with connection.cursor() as cursor:
        rows = cursor.execute("DELETE FROM Friends WHERE name = 'Bob';",)
        connection.commit()
finally:
    #Close the connection, regardless of whether above was successful
    connection.close()