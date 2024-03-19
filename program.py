import psycopg2
from psycopg2 import sql

#connect this code to the database
conn = psycopg2.connect(database = "students",
                        user = "postgres",
                        host = "localhost",
                        password = "Bacadababa03",
                        port = "5432")

#function to get all students
#print all students in the database
def get_students():
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()

#function to add a student to the database by asking required information to the user
def add_student():
    cur = conn.cursor()
    first_name = input("Enter student first name: ")
    last_name = input("Enter student last name: ")
    email = input("Enter student email: ")
    enrolment_date = input("Enter student enrolment date: ")
    cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, enrolment_date))
    conn.commit()

#function to update student email by asking the user to enter the new email and the student id
def update_student_email():
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    new_email = input("Enter new email: ")
    id = input("Enter student id: ")
    cur.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, id))
    conn.commit()

#function to delete a student by asking the user to enter the student id
def delete_student():
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    id = input("Enter student id: ")
    cur.execute("DELETE FROM students WHERE student_id = %s", (id,))
    conn.commit()

#main function to ask the user to select an option
def main():
    while True:
        question = input("Select one of the options: \n 1) Get all students \n 2) add students \n 3) update student email \n 4) delete student \n 5) exit \n")
        if question == "1":
            get_students()
        elif question == "2":
            add_student()
        elif question == "3":
            update_student_email()
        elif question == "4":
            delete_student()
        elif question == "5":
            exit()
        else:
            print("Invalid input")

main()