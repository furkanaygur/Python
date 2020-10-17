class Classes:
    def __init__(self, id,  name, teacherid):
        self.id = id
        self.name = name
        self.teacherid = teacherid

        
    @staticmethod
    def CreateClass(obj):
        List = []
        if isinstance(obj, tuple):
            List.append(Classes(obj[0], obj[1], obj[2]))
        else:
            for i in obj:
                List.append(Classes(i[0], i[1], i[2]))
        return List   