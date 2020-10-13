import mysql.connector
from datetime import datetime
from schooldb_connection import connection 

# ******************* Class *************************

class Student:
    connection = connection
    cursor = connection.cursor()

    def __init__(self, studentNumber, name, surName, birthdate, gender ):
        self.studentNumber = studentNumber
        self.name = name
        self.surName = surName
        self.birthdate = birthdate
        self.gender = gender
    
    def saveStudent(self):
        sql = "INSERT INTO students(StudentNumber, Name, SurName, Birthdate, Gender) VALUES (%s, %s, %s, %s, %s)"
        value = (self.studentNumber, self.name, self.surName, self.birthdate, self.gender)
        Student.cursor.execute(sql,value)

        try:
            Student.connection.commit()
            print(f"{Student.cursor.rowcount } Added")
        except mysql.connector.Error as err:
            print("Error",err)
        finally:
            Student.connection.close()


    @staticmethod
    def saveStudents(students_list):
        sql = "INSERT INTO students(StudentNumber, Name, SurName, Birthdate, Gender) VALUES (%s, %s, %s, %s, %s)"
        values = students_list
        Student.cursor.executemany(sql,values)

        try:
            Student.connection.commit()
            print(f"{Student.cursor.rowcount } Added")
        except mysql.connector.Error as err:
            print("Error",err)
        finally:
            Student.connection.close()

# ******************* Main *************************

# furkan = Student("111","Furkan", "Aygur", datetime(1998,8,2), "E")
# furkan.saveStudent()

students_list = [
    ("201","Furkan", "Aygur", datetime(1998,8,2), "E"),
    ("202","Enes", "Aygur", datetime(1996,6,8), "E"),
    ("203","Burak", "Aygur", datetime(1994,10,25), "E"),
    ("204","Talha", "Aydin", datetime(1998,2,18), "E")
]

Student.saveStudents(students_list)
 