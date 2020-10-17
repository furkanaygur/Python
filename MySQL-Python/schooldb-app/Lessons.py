class Lessons:
    def __init__(self, id,  name):
        self.id = id
        self.name = name

    @staticmethod
    def CreateLesson(obj):
        List = []
        if isinstance(obj, tuple):
            List.append(Lessons(obj[0], obj[1]))
        else:
            for i in obj:
                List.append(Lessons(i[0], i[1]))
        return List   