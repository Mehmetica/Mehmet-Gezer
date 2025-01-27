class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        
    def get_grade(self):
        return self.grade
    
class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students=[]

    def add_students(self,student):
        if len(self.students) < self.max_students: 
            self.students.append(student)
            print(f"{student.name} added! Success!")
            return True
        else:
            print(f"{student.name} can't be added! Failed!")
            return False
        
    def get_avarage(self):
        value=0
        for student in self.students:
            value+=student.get_grade()
        return value/len(self.students)
         

s1=Student("Tim",19,95)
s2=Student("Bill",19,75)
s3=Student("Karl",18,65)

course=Course("Science",2)
course.add_students(s1)
course.add_students(s2)
course.add_students(s3)

print(course.get_avarage())



         
       