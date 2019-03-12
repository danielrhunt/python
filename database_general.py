'''learning DATABASES in Python'''
'''most databases are organized like a dictionary in that they map from keys to values
the biggest difference is that databases are stored on disk
we use SQLite here because it's built into Python
SQLite is also designed to be embedded into other applications, and provide database support within an application'''

'''the primary data structures in a database are TABLES, ROWS, and COLUMNS
the formal relationship between these are RELATION (between tables), TUPLES (between rows?), and ATTRIBUTES (i.e. column headers)'''

#an example of creating a database file, and a table named "Tracks" with two columns
import sqlite3

conn = sqlite3.connect("music.sqlite")  #creates file called "music.sqlite" (or if exists, makes connection)
cur = conn.cursor()     #cursor is like "open" to a file...this basically opens the database

cur.execute("DROP TABLE IF EXISTS Tracks")  #removes Tracks table from the database (if it exists)
cur.execute("CREATE TABLE Tracks (title TEXT, plays INTEGER)")  #creates tables called Tracks, with two attributes "title" (text) and "plays" (an integer)

'''with the table now created, can put data into table using SQL INSERT operation
the SQL INSERT command indicates which table you are using, and then defines a new row by listing the fields you want to include
this is followed by the VALUES you want to place in the new row(s), which are specified by question marks ("?")
this indicates the actual values are passed in as a tuple(s)
again begin by making connection to the database and obtaining the cursor
you can then execute SQL commands using the cursor'''

import sqlite3
conn = sqlite3.connect("music.sqlite")  #creates file called "music.sqlite" (or if exists, makes connection)
handle = conn.cursor()     #cursor is like "open" to a file...this basically opens the database
handle.execute("DROP TABLE IF EXISTS Tracks")  #removes Tracks table from the database (if it exists)
handle.execute("CREATE TABLE Tracks (title TEXT, plays INTEGER)")

handle.execute("INSERT INTO Tracks (title, plays) VALUES (?, ?)", ("Thunderstruck", 20))
handle.execute("INSERT INTO Tracks (title, plays) VALUES (?, ?)", ("Everlong", 121))
conn.commit()   #this forces the data to be written to the database

print("Tracks:")    #only printing this to have a label above what should appear from the database
handle.execute("SELECT title, plays FROM Tracks")   #indicate the columns you want, and the table from which you're retrieving data
'''after executing SELECT, you can now loop through the cursor (handle) using a FOR statement'''
for row in handle:  #you have to write this loop to print out what's contained in the database
    print(row)

handle.execute("DELETE FROM Tracks WHERE plays < 200")
'''the DELETE clause here shows use of WHERE clause, which allows us to express selection criteria to apply conditions only to those rows that match condition'''
handle.close()

'''when we create a table, we indicate the names and types of the columns:
CREATE TABLE Contracts (vendor TEXT, amount INTEGER)
to insert a row into a table, we use the SQL INSERT command:
INSERT INTO Contracts (vendor, amount) VALUES ("IBM", 400000)
the SQL SELECT command is used to retrieve rows and columns from a database
the SELECT statement lets you specify which columns you want to retrieve,
    and the WHERE clause to select which rows you want to see
    it also allows an option ORDER BY clause to control the sorting of the returned rows
        SELECT * FROM Contracts WHERE vendor = "IBM"
    using the * symbol indicates that you want the database to return ALL of the columns for each row that matches the WHERE clause
    further, you can request the returned rows be sorted by one of the fields:
        SELECT vendor, amount FROM Contracts ORDER BY vendor
        SELECT vendor, amount from Contracts ORDER BY amount WHERE vendor = "IBM" --> not sure if that will work'''

'''when we DELETE a table, we need a WHERE clause on a SQL DELETE statement
    the WHERE clause determines which rows are to be deleted:
        DELETE FROM Contracts WHERE vendor = "IBM"'''

'''it is also possible to UPDATE a column or columns within one or more rows using the SQL UPDATE statement:
        UPDATE Contracts SET amount = 300000 WHERE vendor = "IBM"
    the update statement specifies a table and then a list of field(s) and values to change after the set keyword
    and then an optional WHERE clause to select rows that are to be updated
    a single UPDATE statement will change all the rows that match the WHERE clause
    if a WHERE clause is not specified, it performs the update on all the rows in the table'''
