import mysql.connector as mysql

#variables
host = "localhost"
user = "root"
password = ""

#connecting to mysql, not a db in mysql
try:
    db = mysql.connect(host = host, user = user, password = password)
    print("Successful")
except Exception as e:
    print(e)
    print("Failed to connect")

#1.creating a db
try:
    command_handler = db.cursor()                   #creating var command handler to avoid repeatative typing of d.cursor()class cursor
    command_handler.execute("CREATE DATABASE cars") #cursor Allows Python code to execute MySQL command in a database session
    print(" Cars database has been created") 
except Exception as e:
    print(e)

#2.viewing all databases
try:
    command_handler.execute("SHOW DATABASES")
    print("Theseare the available databases")
    for database in command_handler:
        print(database)
except Exception as e:
    print("Coudlnt show all dbs")
    print(e)

#connect to exsisting db
try:
    db1 = mysql.connect(host = host, user = user, password = password, database="cars")
    print("Connected to cars db")
except Exception as e:
    print("Didnt connect to casr db")
    print(e)

#3.creating tables in a db
try:
    command_handler = db1.cursor()
    command_handler.execute("CREATE TABLE Ford (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), engine_size VARCHAR(255))")
    print("TABLE created successfully")
except Exception as e:
    print("Table couldnt be be created")
    print(e)

#4.showing all tables in db
try:
    command_handler.execute("SHOW TABLES")
    for table in command_handler:
        print(table)
    print("Showing all tables in DB")
except Exception as e:
    print(e)
    print("ERROR")

#5.Adding data into the table
try:
    query = "INSERT INTO Ford(name, engine_size) VALUES(%s, %s)"
    query_vals = ("Ford Focus", "1.8L")
    command_handler.execute(query, query_vals)
    db1.commit() #save the changes
    print(command_handler.rowcount, "record inserted")
except Exception as e:
    print(e)

#6.Adding multiple data into the table
try:
    query = "INSERT INTO Ford(name, engine_size) VALUES(%s, %s)"
    query_vals = [
    ("Mustang", "1.8L"),
    ("Ford fiesta", "2.8L")
    ]
    command_handler.executemany(query, query_vals)
    db1.commit() #save the changes
    print(command_handler.rowcount, "record inserted")
except Exception as e:
    print(e)

#7.Display all recorsds from a selected table
try:
    command_handler.execute("SELECT * from Ford")
    records = command_handler.fetchall()
    print("Display records")
    for record in records:
        print(record)
except Exception as e:
    print(e)

#8.Dislpayin columns from table select
command_handler.execute("SELECT name from Ford")
records = command_handler.fetchall()
print("Displaying names from table : Ford")
for record in records:
    print(record)
