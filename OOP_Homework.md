class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lection(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def av_rating(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating
        
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.av_rating()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Ошибка")
            return
        return self.av_rating() < other.av_rating()

    def av_rating_for_course(self, course):
        sum_rating = 0
        len_rating = 0
        for lesson in self.grades.keys():
            if lesson == course:
                sum_rating += sum(self.grades[course])
                len_rating += len(self.grades[course])
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating    

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def av_rating(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.av_rating()}"
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Ошибка")
            return
        return self.av_rating() < other.av_rating()

    def av_rating_for_course(self, course):
        sum_rating = 0
        len_rating = 0
        for lesson in self.grades.keys():
            if lesson == course:
                sum_rating += sum(self.grades[course])
                len_rating += len(self.grades[course])
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating       

class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res

[Студенты]: #
student_1 = Student('Sean', 'Paul', 'Male')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ["ООП"]

student_2 = Student('Jessica', 'Alba', 'Female')
student_2.courses_in_progress += ['Python']
student_2.finished_courses += ["ООП"]

[Лекторы]: #
lecturer_1 = Lecturer('Khal', 'Drogo')
lecturer_1.courses_attached += ['Python']
 
lecturer_2 = Lecturer('Sansa', 'Stark')
lecturer_2.courses_attached += ['Python']

[Проверяющие]: #
reviewer_1 = Reviewer('Leonardo', 'Dicaprio')
reviewer_1.courses_attached += ['Python']
 
reviewer_2 = Reviewer('Mark', 'Wahlberg')
reviewer_2.courses_attached += ['Python']

[Оценки студентам]: #
reviewer_1.rate_hw(student_1, 'Python', 1)
reviewer_1.rate_hw(student_1, 'Python', 4)
reviewer_1.rate_hw(student_1, 'Python', 9)

reviewer_2.rate_hw(student_2, 'Python', 6)
reviewer_2.rate_hw(student_2, 'Python', 3)
reviewer_2.rate_hw(student_2, 'Python', 10)

[Оценки лекторам]: #
student_1.rate_lection(lecturer_1, 'Python', 7)
student_1.rate_lection(lecturer_1, 'Python', 2)
student_1.rate_lection(lecturer_1, 'Python', 1)

student_2.rate_lection(lecturer_2, 'Python', 10)
student_2.rate_lection(lecturer_2, 'Python', 10)
student_2.rate_lection(lecturer_2, 'Python', 10)

student_list = [student_1, student_2]
lecturer_list = [lecturer_1, lecturer_2]
reviewer_list = [reviewer_1, reviewer_2]

def average_rating_for_course(course, student_list):
    sum_rating = 0
    quantity_rating = 0
    for stud in student_list:
        for course in stud.grades:
            stud_sum_rating = stud.av_rating_for_course(course)
            sum_rating += stud_sum_rating
            quantity_rating += 1
    average_rating = round(sum_rating / quantity_rating, 2)
    return average_rating


print(average_rating_for_course('Python', student_list))
print(average_rating_for_course('Python', lecturer_list))
print(student_1)
print(student_2)
print(lecturer_1)
print(lecturer_2)