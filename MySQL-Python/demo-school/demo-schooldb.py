import mysql.connector
from datetime import datetime
from schooldb_connection import connection 

# ******************* Class *************************

class Student:
    connection = connection
    cursor = connection.cursor()

    def __init__(self):
        print("deneme")

    def display(self):
        sql = "select * from students"
        Student.cursor.execute(sql)

        try:
            result = Student.cursor.fetchall()
            for i in result:
                print(f"ID: {i[0]} \t Student Number: {i[1]} \t Name Surname: {i[2]} {i[3]} \t Gender: {i[4]}")
        except mysql.connector.Error as err:
            print("Error", err)

    def saveStudent(self, studentNumber, name, surName, birthdate, gender):
        sql = "INSERT INTO students(StudentNumber, Name, SurName, Birthdate, Gender) VALUES (%s, %s, %s, %s, %s)"
        value = (studentNumber, name, surName, birthdate, gender)
        Student.cursor.execute(sql,value)

        try:
            Student.connection.commit()
            print(f"{Student.cursor.rowcount } Added")
        except mysql.connector.Error as err:
            print("Error",err)


    # @staticmethod
    # def saveStudents(students_list):
    #     sql = "INSERT INTO students(StudentNumber, Name, SurName, Birthdate, Gender) VALUES (%s, %s, %s, %s, %s)"
    #     values = students_list
    #     Student.cursor.executemany(sql,values)

    #     try:
    #         Student.connection.commit()
    #         print(f"{Student.cursor.rowcount } Added")
    #     except mysql.connector.Error as err:
    #         print("Error",err)

    @staticmethod
    def updateStudent(studentNumber):
        name = input("Name: ")
        surName = input("SurName: ")
        birthdate = input("Birtdate (YYYY,MM,DD): ")
        gender = input("Gender (M/F) : ")

        sql = "update students set Name = %s, SurName= %s, Birthdate = %s, Gender= %s where StudentNumber = %s"
        values = (name, surName, birthdate, gender, studentNumber)
        Student.cursor.execute(sql, values)

        try:
            Student.connection.commit()
            print(f" { Student.cursor.rowcount } updated")
        except mysql.connector.Error as err:
            print("Error",err)
    

    @staticmethod
    def deleteStudent(id):
        sql = "delete from students where ID = %s"
        value = (id,)
        Student.cursor.execute(sql, value)

        try:
            Student.connection.commit()
            print(f" { Student.cursor.rowcount } deleted")
        except mysql.connector.Error as err:
            print("Error",err)
    
    def closeDB(self):
        Student.connection.close()

# ******************* Main *************************


# furkan = Student("111","Furkan", "Aygur", datetime(1998,8,2), "M")
# furkan.saveStudent()

# students_list = [
#     ("201","Furkan", "Aygur", datetime(1998,8,2), "M"),
#     ("202","Enes", "Aygur", datetime(1996,6,8), "M"),
#     ("203","Burak", "Aygur", datetime(1994,10,25), "M"),
#     ("204","Talha", "Aydin", datetime(1998,2,18), "M")
# ]

# Student.saveStudents(students_list)


student = Student()
while True :
    print(" MENU ".center(50,'*'))
    choice = input("1- Show Students \n2- Insert Student \n3- Update Student \n4- Delete Student \n5- Exit \nYour Choice: ")
    if choice == '5':
        student.closeDB()
        break
    elif choice == '1':
        student.display()
    elif choice == '2':
        StudentNubmer = float(input("Studen Number: "))
        name = input("Name: ")
        surName = input("SurName: ")
        birthdate = input("Birtdate (YYYY,MM,DD): ")
        gender = input("Gender (M/F) : ")
        student.saveStudent(StudentNubmer, name, surName, birthdate, gender)
 
    elif choice == '3':
        StudentNubmer = input("Student Number: ")
        student.updateStudent(StudentNubmer)

    elif choice == '4':
        id = input("ID: ")
        student.deleteStudent(id)

    else:
        print(" Only (1, 2, 3, 4, 5) ".center(50,'!'))