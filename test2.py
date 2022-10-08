import mysql.connector as mysql

#Variables
host = "localhost"
user = "root"
password = ""

try:
    db = mysql.connect(host=host, user=user, password="", database="cars")
    print("connected")
except:
    print("error")

command_handler = db.cursor(buffered=True)  #???

#Disaplying one row of data
command_handler.execute("select name from Ford")
record = command_handler.fetchone()
#print(record)

#Filtering the rows of data returned
print("*****************Filtering the rows of data returned****************")
command_handler.execute(" SELECT * from Ford WHERE name = 'Ford Focus'")
records = command_handler.fetchall()

for record in records:
    print(record)

#Filtering the rows of data based on similarity of words; Similar to Google sugest
print("***************Filtering data that is similar to a keyword provided**************")
command_handler.execute("SELECT * FROM Ford WHERE name LIKE '%mus%'") # '%mus%' anythig that has'mus' in it
records = command_handler.fetchall()

for record in records:
    print(record)

#Sort rows, by name, ASCENDING
print("************Sorting data based off name: ****************")
command_handler.execute("SELECT * from Ford ORDER BY name")
records = command_handler.fetchall()
for record in records:
    print(record)

#Sort rows, by id, DESCENDING
print("**************Sorting ID data in descending order************")
command_handler.execute("SELECT * from Ford ORDER BY id DESC")
records = command_handler.fetchall()

for record in records:
    print(record)

# #Sorting data in descending order
# print("///////////DELETING RECORD////////////")
# command_handler.execute("DELETE FROM Ford WHERE name = 'mustang'")
# db.commit()
# print(command_handler.rowcount, "Record(s) Deleted")

# #Delete an entire table
# print("-------------Deleting an entire table-----------")
# command_handler.execute("DROP TABLE dummy")
# print("Table deleted")

#Deletig a table only if it exsists// COMES WITH AN ERROR HANDLING IN IT
print("Deleting a table if it exsists")
command_handler.execute("DROP TABLE IF EXISTS DUMMY")
print("done")

#UPDATING THE ROW!!!!!
print("^^^^^^^^Updating records in a table^^^^^^")
print("Updating exsisting records in a table")
command_handler.execute("UPDATE Ford SET engine_size='5L' WHERE engine_size='3L' AND name='Ford Focus'")
db.commit()
print("Records Updated!")


#Limiting the records to a specifeid number of results
print("!!!!!!!!!!!!!!!Limiting how many results are returned")
command_handler.execute("SELECT * FROM Ford LIMIT 3")
records = command_handler.fetchall()

for record in records:
    print(record)
