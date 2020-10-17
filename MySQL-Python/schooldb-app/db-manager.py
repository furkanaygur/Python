import mysql.connector
from datetime import datetime
from connection import connection
from Students import Students
from Teachers import Teachers
from Lessons import Lessons
from Classes import Classes


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
        value = (Teachers.branch, Teachers.name, Teachers.surname, Teachers.birthdate, Teachers.gender, Teachers.id)
        self.cursor.execute(sql, value)

        try:
            self.connection.commit()
            print(f" { self.cursor.rowcount } updated")
        except mysql.connector.Error as err:
            print("Error",err)
    
    
    def getClassById(self, id):
        sql = "select * from classes where ID = %s"
        value = (id,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchone()
            return Classes.CreateClass(obj)
        except mysql.connector.Error as err:
            print("Error", err) 

    def addClass(self, Classes : Classes):
        sql = "INSERT INTO classes(Name, Teacherid) VALUES (%s, %s)"
        value = (Classes.name, Classes.teacherid)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount } Added")
        except mysql.connector.Error as err:
            print("Error",err)      

    def updateClass(self, Classes: Classes):
        sql = "update classes set Name = %s, Teacherid = %s where ID = %s"
        value = (Classes.name, Classes.teacherid, Classes.id)
        self.cursor.execute(sql, value)

        try:
            self.connection.commit()
            print(f" { self.cursor.rowcount } updated")
        except mysql.connector.Error as err:
            print("Error",err)

    def getLessonById(self, id):
        sql = "select * from lessons where ID = %s"
        value = (id,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchone()
            return Lessons.CreateLesson(obj)
        except mysql.connector.Error as err:
            print("Error", err) 


    def addLesson(self, Lessons : Lessons):
        sql = "INSERT INTO lessons(Name) VALUES (%s)"
        value = (Lessons.name,)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount } Added")
        except mysql.connector.Error as err:
            print("Error",err)  

    def updateLesson(self, Lessons: Lessons):
        sql = "update lessons set Name = %s where ID = %s"
        value = (Lessons.name,  Lessons.id)
        self.cursor.execute(sql, value)

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

# # Get student by id
# student = db.getStudentById(40)
# print(student.name, student.surname)
# db.closeConnection()

# # Get teacher by id
# teacher = db.getTeacherById(2)
# print(teacher[0].name)


# # Get student by class id
# student = db.getStudentByClassId(1)
# print(student[0].name)
# print(student[1].name)
# db.closeConnection()

# # Add student
# std = Students(None, 207, "Furkan", "Aygur", datetime(1998,2,8), "M", 1)
# db.addStudent(std)
# db.closeConnection()

# # Add teacher
# teacher = Teachers(None,"physics", "Furkan", "Aygur", datetime(1990,8,2),"M")
# db.addTeacher(teacher)
# db.closeConnection()

# # Add class
# Class = Classes(None,"9/A",4)
# db.addClass(Class)
# db.closeConnection()

# # Add lesson
# lesson = Lessons(None,"physics")
# db.addLesson(lesson)
# db.closeConnection()

# # Update student
# student = db.getStudentById(50)
# student[0].name = "Furkan"
# student[0].surname = "AYGUR"
# db.updateStudent(student[0])
# db.closeConnection()

# # Update teacher
# teacher = db.getTeacherById(4)
# teacher[0].name = "FURKAN"
# db.updateTeacher(teacher[0])
# db.closeConnection()

# # Update Class
# Class = db.getClassById(4)
# Class[0].teacherid = 1
# db.updateClass(Class[0])
# db.closeConnection()

# # Update Lesson
# lesson = db.getLessonById(4)
# lesson[0].name = "Physics"
# db.updateLesson(lesson[0])
# db.closeConnection()