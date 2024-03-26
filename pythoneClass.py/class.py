"""
class student skapar student så man kan fråga om dom
"""
class student:
    def __init__(self, f_name : str, l_name, age, gender):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.gender = gender 
    
    def __str__(self):
        return f"{self.f_name} {self.l_name}"

"""
gör samma som student fast för teatcher
"""
class teacher:
    def __init__(self, f_name, l_name, age, gender):
        self.f_name = f_name
        self.l_name = l_name 
        self.age = age 
        self.gender = gender 
    
    def __str__(self):
        return f"{self.f_name} {self.l_name}"

class Group:
    def __init__(self, subject, teacher : teacher, student : list):
        self.subject = subject
        self.teacher = teacher
        self.student = student

    """
    creating and adding a new student to the list
    """
    def add_student(self,new_student):
        self.student.append(new_student)
    
    def r_student(self, remove_student):
        self.remove_student = remove_student

"""
liknande till en lista fast med värden och all infomration inom dess class
"""
elis = student("Elis","Laxvik", "17", "Helicopter")
Elias = teacher("Elias", "Sjöling", "21", "Male")
school = Group("Programing", Elias, [elis])

school.add_student(student("michal", "gregory", "17", "airplane"))

for a in school.student:
    print(a)