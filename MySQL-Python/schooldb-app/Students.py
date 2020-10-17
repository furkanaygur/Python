class Students:
    def __init__(self, id, StudentNumber, name, surname, birthdate, gender, classid):
        self.id = id
        self.StudentNumber = StudentNumber
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
        self.classid = classid

    @staticmethod
    def CreateStudent(obj):
        List = []
        
        if isinstance(obj, tuple):
            List.append(Students(obj[0], obj[1], obj[2], obj[3], obj[4], obj[5], obj[6]))
        else:
            for i in obj:
                List.append(Students(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
        return List    
        