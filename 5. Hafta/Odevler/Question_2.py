class School():
    
    students = [] 
    teachers = {}

    def __init__(self, name, foundation_year, students, teachers):
        self.name = name
        self.foundation_year = foundation_year
        self.students = students
        self.teachers = teachers

    def add_new_student(self, student_name=None, student_class=None):
        if not student_name:
            student_name = input("Name of the student: ")
        if not student_class:
            student_class = input("Class of the student: ")
        
        new_student = [student_name, student_class]
        self.students.append(new_student)
    
    def add_new_teacher(self, teacher_name, branch):
        if not teacher_name:
            teacher_name = input("Name of the teacher: ")
        if not branch:
            branch = input("Major of the teacher: ")

        new_teacher = {
            "name": teacher_name,
            "branch": branch
        }

        self.teachers[teacher_name] = new_teacher
    
    def student_list(self):
        print("Student List:")
        for student in self.students:
            print(f"Name: {student[0]}, Class: {student[1]}")
    
    def teacher_list(self):
        print("Teacher List:")
        for teacher in self.teachers.values():
            print(f"Name: {teacher['name']}, Major: {teacher['branch']}")

    def __str__(self):
        return f"School Name: {self.name}, Founded: {self.foundation_year}"

school1 = School("Mehmet'in Yeri", 1988, School.students, School.teachers)

# school1.add_new_student(student_name="Ahmet", student_class="10A")
# school1.add_new_student(student_name="Mehmet", student_class="11B")
# school1.add_new_teacher(teacher_name="Ali", branch="Mathematics")
# school1.add_new_teacher(teacher_name="Veli", branch="Physics")

school1.add_new_student("Mahmut","11-A")
school1.add_new_teacher("Mukafat","Astrofizik")

print(school1)

school1.student_list()
school1.teacher_list()
