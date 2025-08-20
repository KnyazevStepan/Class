class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)
    
    def rate_lecture(self, lecturer, course, grade):
        # Проверяем, что lecturer является экземпляром класса Lecturer
        if not isinstance(lecturer, Lecturer):
            return 'Ошибка: Может оценивать только лекторов'
        
        # Проверяем, что студент записан на этот курс
        if course not in self.courses_in_progress:
            return 'Ошибка: Студент не записан на этот курс'
        
        # Проверяем, что лектор закреплен за этим курсом
        if course not in lecturer.courses_attached:
            return 'Ошибка: Лектор не закреплен за этим курсом'
        
        # Проверяем, что оценка в допустимом диапазоне (1-10)
        if not (1 <= grade <= 10):
            return 'Ошибка: Оценка должна быть от 1 до 10'
        
        # Добавляем оценку лектору
        if course in lecturer.grades:
            lecturer.grades[course].append(grade)
        else:
            lecturer.grades[course] = [grade]
        
        return None  # Успешное выполнение

               
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    """Класс для лекторов, наследуется от Mentor"""
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}  # Словарь для хранения оценок за лекции


class Reviewer(Mentor):
    """Класс для экспертов, проверяющих домашние задания, наследуется от Mentor"""
    
    def rate_hw(self, student, course, grade):
        # Проверяем, что student является экземпляром класса Student
        if not isinstance(student, Student):
            return 'Ошибка: Может оценивать только студентов'
        
        # Проверяем, что эксперт закреплен за этим курсом
        if course not in self.courses_attached:
            return 'Ошибка: Эксперт не закреплен за этим курсом'
        
        # Проверяем, что студент изучает этот курс
        if course not in student.courses_in_progress:
            return 'Ошибка: Студент не изучает этот курс'
        
        # Проверяем, что оценка в допустимом диапазоне (1-10)
        if not (1 <= grade <= 10):
            return 'Ошибка: Оценка должна быть от 1 до 10'
        
        # Добавляем оценку студенту
        if course in student.grades:
            student.grades[course].append(grade)
        else:
            student.grades[course] = [grade]
        
        return None  # Успешное выполнение


# Тестирование
lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')

student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

print(student.rate_lecture(lecturer, 'Python', 7))   # None - успешно
print(student.rate_lecture(lecturer, 'Java', 8))     # Ошибка: Лектор не закреплен за этим курсом
print(student.rate_lecture(lecturer, 'C++', 8))      # Ошибка: Студент не записан на этот курс
print(student.rate_lecture(reviewer, 'Python', 6))   # Ошибка: Может оценивать только лекторов

print(lecturer.grades)  # {'Python': [7]}