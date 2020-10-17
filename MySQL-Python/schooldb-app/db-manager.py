import mysql.connector
from datetime import datetime
from connection import connection
from Students import Students
from Teachers import Teachers
# from Lessons import Lessons
# from Classes import Classes


# ************************ Class ******************************

class DbManager:
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def getStudentById(self, id):
        sql = "select * from students where ID = %s"
        value = (id,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchone()
            return Students.CreateStudent(obj)
        except mysql.connector.Error as err:
            print("Error", err)  


    def getStudentByClassId(self, id):
        sql = "select * from students where Classid = %s"
        value = (id,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchall()
            return Students.CreateStudent(obj)
        except mysql.connector.Error as err:
            print("Error", err)  


    def addStudent(self, Students: Students ):
        sql = "INSERT INTO students(StudentNumber, Name, SurName, Birthdate, Gender, Classid) VALUES (%s, %s, %s, %s, %s, %s)"
        value = (Students.StudentNumber, Students.name, Students.surname, Students.birthdate, Students.gender, Students.classid)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount } Added")
        except mysql.connector.Error as err:
            print("Error",err)

    def updateStudent(self, Students: Students):
        sql = "update students set StudentNumber = %s, Name = %s, SurName= %s, Birthdate = %s, Gender= %s, Classid= %s where ID = %s"
        values = (Students.StudentNumber, Students.name, Students.surname, Students.birthdate, Students.gender, Students.classid, Students.id)
        self.cursor.execute(sql, values)

        try:
            self.connection.commit()
            print(f" { self.cursor.rowcount } updated")
        except mysql.connector.Error as err:
            print("Error",err)


    def getTeacherById(self, id):
        sql = "select * from teachers where ID = %s"
        value = (id,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchone()
            return Teachers.CreateTeacher(obj)
        except mysql.connector.Error as err:
            print("Error", err) 

    def addTeacher(self, Teachers: Teachers ):
        sql = "INSERT INTO teachers(Branch, Name, SurName, Birthdate, Gender) VALUES (%s, %s, %s, %s, %s)"
        value = (Teachers.branch, Teachers.name, Teachers.surname, Teachers.birthdate, Teachers.gender)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount } Added")
        except mysql.connector.Error as err:
            print("Error",err)

    def updateTeacher(self, Teachers: Teachers):
        sql = "update teachers set Branch = %s, Name = %s, SurName= %s, Birthdate = %s, Gender= %s where ID = %s"
        values = (Teachers.branch, Teachers.name, Teachers.surname, Teachers.birthdate, Teachers.gender, Teachers.id)
        self.cursor.execute(sql, values)

        try:
            self.connection.commit()
            print(f" { self.cursor.rowcount } updated")
        except mysql.connector.Error as err:
            print("Error",err)
    
    def closeConnection(self):
        self.connection.close()
        print("Database Closed")



# **************************** Main ****************************

db = DbManager()

# get student by id
# student = db.getStudentById(40)
# print(student.name, student.surname)
# db.closeConnection()

# get teacher by id
# teacher = db.getTeacherById(2)
# print(teacher[0].name)


# get student by class id
# student = db.getStudentByClassId(1)
# print(student[0].name)
# print(student[1].name)
# db.closeConnection()

# Add student
# std = Students(None, 207, "Furkan", "Aygur", datetime(1998,2,8), "M", 1)
# db.addStudent(std)
# db.closeConnection()

# Add teacher
# teacher = Teachers(None,"physics", "Furkan", "Aygur", datetime(1990,8,2),"M")
# db.addTeacher(teacher)
# db.closeConnection()

# Update student
# student = db.getStudentById(50)
# student[0].name = "Furkan"
# student[0].surname = "AYGUR"
# db.updateStudent(student[0])
# db.closeConnection()

# Update teacher
teacher = db.getTeacherById(4)
teacher[0].name = "FURKAN"
db.updateTeacher(teacher[0])
db.closeConnection()