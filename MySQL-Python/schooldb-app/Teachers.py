class Teachers:
    def __init__(self, id, branch, name, surname, birthdate, gender):
        self.id = id
        self.branch = branch
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
    
    @staticmethod
    def CreateTeacher(obj):
        List = []
        if isinstance(obj, tuple):
            List.append(Teachers(obj[0], obj[1], obj[2], obj[3], obj[4], obj[5]))
        else:
            for i in obj:
                List.append(Teachers(i[0], i[1], i[2], i[3], i[4], i[5]))
        return List   