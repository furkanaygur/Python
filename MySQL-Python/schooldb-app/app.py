from datetime import datetime
from DbManager import DbManager
from datetime import datetime
from Students import Students

class App:
    def __init__(self):
        self.db = DbManager()
    
    def initApp(self):
        while True:
            print(" Menu ".center(50,'*'))
            print("1- List Students\n2- Add Student\n3- Update Student\n4- Delete Student\n5- Exit\n")
            choice = input("Your Choice: ")
            if choice == '1':
                self.displayStudents()
            elif choice == '2':
                self.addStudent()
            elif choice == '3':
                self.updateStudent()
            elif choice == '4':
                self.deleteStudent()
            elif choice == '5':
                self.db.closeConnection()
                break
            else:
                print("Only 1-2-3-4-5")
    
    def displayClasses(self):
        for i in self.db.getClasses():
            print(f"{i.id}- {i.name}")


    def displayStudents(self):
        self.displayClasses()

        classid = int(input('*** Enter Class ID: '))
        students = self.db.getStudentByClassId(classid)
        print(" Student List ".center(25,'*'))
        for i in students:
            print(f"{i.id}- {i.name} {i.surname}")


    def addStudent(self):
        self.displayClasses()
        classid = int(input('*** Enter Class ID: '))
        number = input("Studen Number: ")
        name = input("Name: ")
        surname = input("Surname: ")
        birthdate =  input("Birthdate (YYYY,MM,DD): ")
        gender = input("Gender (M,F): ")
        student = Students(None, number, name, surname, birthdate, gender, classid)
        self.db.addStudent(student)


    def updateStudent(self):
        self.displayStudents()
        studentid = int(input("Student ID: "))

        student = self.db.getStudentById(studentid)
        print(student[0].name, student[0].surname)

        student[0].name = input('Name: ') or student[0].name
        student[0].surname = input('Surname: ') or student[0].surname
        student[0].birthdate = input('Birthdate (YYYY,MM,DD): ') or student[0].birthdate 
        student[0].gender = input('Gender: ') or student[0].gender
        student[0].classid = input('Class ID: ') or student[0].classid

        self.db.updateStudent(student[0])


    def deleteStudent(self):
        self.displayStudents()
        studentid = int(input("Student ID: "))
        self.db.deleteStudent(studentid)


# ********************** Main *********************

app = App()
app.initApp()