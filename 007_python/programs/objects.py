class Person:
    def __init__(self,first_name='default',age=0,):
        self.first_name=first_name
        self.age=age
        self.skills=[]
    def print(self):
        return f'fname= {self.first_name}, age={self.age}, skills={self.skills}'
    def add_skills(self,skill):
        self.skills.append(skill)


p=Person("asna",22)

p.add_skills("python")
print(p.print())


class Student(Person):
    def __init__(self, first_name='default', age=0,studid=0):
        super().__init__(first_name, age)
        self.studentId=studid
    def print(self):
        return f'{super().print()} studentid={self.studentId}'

s1=Student(20,"ashwin",101)
s1.add_skills("java")
print(s1.print())

