class Student:
    name = ""
    sex = ""
    couse = "Python"

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex



    def doHomework(self):
        print("I'm doing homework!")

lwq = Student("Kaka","male")
lwq.doHomework()
print(lwq.name)
print(lwq.couse)
print(lwq.name)

lwq.