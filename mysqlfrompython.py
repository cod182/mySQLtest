import os
import datetime
import pymysql

# Get Username gtom cloud9 workspace

username = os.getenv('GITPOD_USER')

# CONNECT TO DATABASE
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:

        list_of_names = ['Jim', 'Bob']
        # Prepare a string with the same number of placeholders as in list_of_names
        format_strings = ','.join(['%s']*len(list_of_names))
        cursor.execute("DELETE FROM Friends WHERE name in ({});".format(format_strings), list_of_names)
        connection.commit()

        # # Delete Many
        # cursor.executemany("DELETE FROM Friends WHERE name = %s;", ['Bob', 'Jim']) 
        # connection.commit()
        
        # # Alternate Delete
        # cursor.execute("DELETE FROM Friends WHERE name = %s;", 'Bob') 
        # connection.commit()

        #  # Delete a row
        # cursor.execute("DELETE FROM Friends WHERE name = 'Bob';") 
        # connection.commit()

        # # Update many rows
        # rows = [(23, "Bob"),
        #         (56, 'Jim'),
        #         (100, 'James')]
        # cursor.executemany("UPDATE Friends SET age = %s WHERE name = %s;", rows)
        # connection.commit()

        # # Alternate Update a row
        # cursor.execute("UPDATE Friends SET age = %s WHERE name = %s;", (23, 'Bob'))
        # connection.commit()

        # # Update a row
        # cursor.execute("UPDATE Friends SET age = 22 WHERE name = 'Bob';")
        # connection.commit()

        # Inserting Many rows at once
        # rows = [("Bob", 21, "1990-02-06 23:04:56"),
        #         ("Jim", 31, "1993-02-06 20:04:56"),
        #         ("James", 111, "1910-02-06 18:04:56"),
        #         ("Fred", 61, "1962-05-02 12:04:56")]
        # cursor.executemany("INSERT INTO Friends VALUES (%s, %s, %s);", rows)
        # connection.commit()

        # row = ("Bob", 21, "1990-02-06 23:04:56")
        # # Inserting data using a cursor
        # cursor.execute("INSERT INTO Friends VALUES (%s, %s, %s);", row)
        # connection.commit()

        # Creating a new table usinga. cursor
        # cursor.execute("""CREATE TABLE IF NOT EXISTS
        #                 Friends(name char(20), age int, DOB datetime);""")

        # sql = "SELECT * FROM Genre;"
        # for row in cursor:
        #     print(row)
finally:
    # Close connection
    connection.close()
