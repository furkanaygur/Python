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
    
    def deleteStudent(self, id):
        sql = "Delete from students where ID = %s"
        value = (id,)
        self.cursor.execute(sql,value)
        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} Deleted")
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
    
    def getClasses(self):
        sql = "select * from classes"
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Classes.CreateClass(obj)
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


