import mysql.connector as mysql

try:
    db = mysql.connect(host="localhost", user="root", password="", database = "college" )
    print("Database ready.")
except Exception as e:
    print(e)
    print("Not Connected!")

command_handler = db.cursor(buffered = True)

def student_session(username):
    
    while 1:
        print("")
        print("Student's Menu")
        print("")
        print("1. View register")
        print("2. Download register")
        print("3. Logout")
        user_option = input(str("Option : "))

        if user_option == "1":
            print("Display register")
            username = (str(username),)
            command_handler.execute("SELECT date, username, status FROM attendance WHERE username = %s", username) 
            records = command_handler.fetchall()
            for record in records:
                print("!")
                print(record)
        
        elif user_option == "2":
            print("Downloading Register...")
            username = (str(username),)
            command_handler.execute("SELECT date, username, status FROM attendance WHERE username = %s", username) 
            records = command_handler.fetchall()
            with open("register.text", "a") as f:
                for record in records:
                    f.write(str(record)+"\n")
            f.close()
            print("All records saved")
            print("Check the project folder")

        
        elif user_option == "3":
            break
        
        else:
            print("Invalid input")
        
def teacher_session():
    
    while 1:
        print("")
        print("Teacher's Menu")
        print("")
        print("1. Mark student register")
        print("2. View register")
        print("3. Logout")
        
        user_option = input("Option : ")
        
        if user_option == "1":
            print("")
            print("Mark Student Register")
            command_handler.execute("SELECT username FROM users WHERE privilage = 'student'")
            records = command_handler.fetchall()
            date = input(str("DATE : DD/MM/YYYY : "))
            for record in records:
                record = str(record).replace(",","")
                record = str(record).replace("'","")
                record = str(record).replace("(","")
                record = str(record).replace(")","")
                #Present | Absent | Late
                status = input(str("Status for " + str(record) + " (P/A/L): "))
                query_vals = (str(record), date, status)
                command_handler.execute("INSERT INTO attendance (username, date, status) VALUES(%s, %s, %s)",query_vals)
                db.commit()
                print(record + " Marked as "+ status)

        elif user_option == "2":
            print("")
            print("---Attendance menu---")
            print("1. View all Student Register")
            print("2. View attendance register of a particular date")

            user_option = input("Option: ")

            if user_option == "1":
                command_handler.execute("SELECT * FROM attendance")
                records = command_handler.fetchall()
                if command_handler.rowcount < 1:
                    print("no students in class")
                else:
                    for record in records:
                        print(record)
                        print("")

            elif user_option == "2":
                date = input(str("DATE : DD/MM/YYYY : "))
                query_vals = (str(date),)
                command_handler.execute("SELECT * FROM attendance WHERE date = %s", query_vals) #!Not Working
                records = command_handler.fetchall()
                if command_handler.rowcount < 1:
                    print("no students in class")
                else:
                    for record in records:
                        print(record)

        elif user_option == "3":
            break
        else:
            print("Invalid Input")

def admin_session():
    while 1:
        print("")
        print("Admin Menu")
        print("1. Register new student")
        print("2. Register new teacher")
        print("3. Delete exsisting student")
        print("4. Delete exsisting teacher")
        print("5. Logout")

        user_option = input("option: ")
        if user_option == "1":
            print("")
            print("Register new student")
            username = input("Student name:")
            password = input("password: ")
            query_vals = (username, password)
            command_handler.execute("INSERT INTO users (username, password, privilage) VALUES (%s, %s, 'student')",query_vals)
            db.commit()
            print(username + " has been registered as a student.")
        
        elif user_option == "2":
            print("")
            print("Register new teacher")
            username = input("Teacher name:")
            password = input("password: ")
            query_vals = (username, password)
            command_handler.execute("INSERT INTO users (username, password, privilage) VALUES (%s, %s, 'teacher')",query_vals)
            db.commit()
            print(username + " has been registered as a teacher.")

        elif user_option == "3":
            print("")
            print("Delete exsisting student account")
            username = input("Student username: ")
            privilage = "student"
            #password = input("password: ")
            query_vals = (username, privilage)
            command_handler.execute("DELETE FROM users WHERE username = %s AND privilage = %s", query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("Student does not exsist")
            else:
                print(username + "'s account has been deleted.")

        elif user_option == "4":
            print("")
            print("Delete exsisting teacher account")
            username = input("Teacher username: ")
            privilage = "teacher"
            #password = input("password: ")
            query_vals = (username, privilage)
            command_handler.execute("DELETE FROM users WHERE username = %s AND privilage = %s", query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("Teacher does not exsist")
            else:
                print(username + "'s account has been deleted.")
            
        elif user_option == "5":
            break
        
        else:
            print("Invalid input.")


def auth_student():
    print("")
    print("Student's Login")
    print("")
    username = input(str("Username : "))
    password = input(str("Password : "))
    query_vals = (username, password, "student")
    command_handler.execute("SELECT username FROM users WHERE username = %s AND password = %s AND privilage = %s ",query_vals)
    if command_handler.rowcount <= 0:
        print("Login not recognised")
    else:
        print("Student sucessfully logged in.")
        student_session(username)



def auth_teacher():
    print("")
    print("Teacher's Login")
    print("")
    username = input("Username: ")
    password = input("Password: ")
    query_vals = (username, password)
    command_handler.execute("SELECT * FROM users WHERE username = %s AND password= %s AND privilage = 'teacher'",query_vals)
    if command_handler.rowcount <= 0:
        print("Login not recognised")
    else:
        print("Teacher sucessfully logged in.")
        teacher_session()

def auth_admin():
    print("")
    print("Admin Login")
    print("")
    username = input("Username: ")
    password = input("Password: ")
    if username == "admin":
        if password == "12345":
            admin_session()
        else:
            print("Incorrect Password!")
    else:
        print("Login details not recognised")

def main():
    while 1:
        print("Welcome to the college system")
        print("")
        print("1. Login as student")
        print("2. Login as teacher")
        print("3. Login as admin")
        print("4. Exit")

        user_option = input(str("Option : "))
        if user_option == "1":
            auth_student()
        elif user_option == "2":
            auth_teacher()
        elif user_option == "3":
            auth_admin()
        elif user_option == "4":
            break
        else:
            print("Invalid Input")



main()
