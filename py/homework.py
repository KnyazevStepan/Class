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
        if not isinstance(lecturer, Lecturer):
            return 'Ошибка: Может оценивать только лекторов'
        if course not in self.courses_in_progress:
            return 'Ошибка: Студент не записан на этот курс'
        if course not in lecturer.courses_attached:
            return 'Ошибка: Лектор не закреплен за этим курсом'
        if not (1 <= grade <= 10):
            return 'Ошибка: Оценка должна быть от 1 до 10'
        
        if course in lecturer.grades:
            lecturer.grades[course].append(grade)
        else:
            lecturer.grades[course] = [grade]
        
        return None

    def __str__(self):
        avg_grade = self._calculate_average_grade()
        courses_in_progress = ', '.join(self.courses_in_progress) if self.courses_in_progress else 'Нет курсов'
        finished_courses = ', '.join(self.finished_courses) if self.finished_courses else 'Нет курсов'
        
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade:.1f}\n"
                f"Курсы в процессе изучения: {courses_in_progress}\n"
                f"Завершенные курсы: {finished_courses}")

    def _calculate_average_grade(self):
        """Вычисляет среднюю оценку за все домашние задания"""
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calculate_average_grade() < other._calculate_average_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calculate_average_grade() <= other._calculate_average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calculate_average_grade() == other._calculate_average_grade()

    def __ne__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calculate_average_grade() != other._calculate_average_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calculate_average_grade() > other._calculate_average_grade()

    def __ge__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calculate_average_grade() >= other._calculate_average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        avg_grade = self._calculate_average_grade()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_grade:.1f}")

    def _calculate_average_grade(self):
        """Вычисляет среднюю оценку за все лекции"""
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calculate_average_grade() < other._calculate_average_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calculate_average_grade() <= other._calculate_average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calculate_average_grade() == other._calculate_average_grade()

    def __ne__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calculate_average_grade() != other._calculate_average_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calculate_average_grade() > other._calculate_average_grade()

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calculate_average_grade() >= other._calculate_average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if not isinstance(student, Student):
            return 'Ошибка: Может оценивать только студентов'
        if course not in self.courses_attached:
            return 'Ошибка: Эксперт не закреплен за этим курсом'
        if course not in student.courses_in_progress:
            return 'Ошибка: Студент не изучает этот курс'
        if not (1 <= grade <= 10):
            return 'Ошибка: Оценка должна быть от 1 до 10'
        
        if course in student.grades:
            student.grades[course].append(grade)
        else:
            student.grades[course] = [grade]
        
        return None


# Функции для подсчета средних оценок
def calculate_average_hw_grade(students, course_name):
    """Подсчитывает среднюю оценку за домашние задания по всем студентам в рамках конкретного курса"""
    all_grades = []
    for student in students:
        if course_name in student.grades:
            all_grades.extend(student.grades[course_name])
    
    if not all_grades:
        return 0
    return sum(all_grades) / len(all_grades)


def calculate_average_lecture_grade(lecturers, course_name):
    """Подсчитывает среднюю оценку за лекции всех лекторов в рамках конкретного курса"""
    all_grades = []
    for lecturer in lecturers:
        if course_name in lecturer.grades:
            all_grades.extend(lecturer.grades[course_name])
    
    if not all_grades:
        return 0
    return sum(all_grades) / len(all_grades)


# Создаем экземпляры классов
print("=== СОЗДАНИЕ ЭКЗЕМПЛЯРОВ ===")

# 2 студента
student1 = Student('Ruoy', 'Eman', 'M')
student2 = Student('Анна', 'Смирнова', 'Ж')

# 2 лектора
lecturer1 = Lecturer('Иван', 'Иванов')
lecturer2 = Lecturer('Петр', 'Петров')

# 2 проверяющих
reviewer1 = Reviewer('Some', 'Buddy')
reviewer2 = Reviewer('Алексей', 'Экспертов')

# Настраиваем курсы
print("\n=== НАСТРОЙКА КУРСОВ ===")
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Введение в программирование']
student2.courses_in_progress += ['Python', 'Java', 'Git']

lecturer1.courses_attached += ['Python', 'Git']
lecturer2.courses_attached += ['Python', 'Java']

reviewer1.courses_attached += ['Python', 'Git']
reviewer2.courses_attached += ['Java', 'Git']

# Вызываем все методы
print("\n=== ВЫЗОВ МЕТОДОВ ===")

# Методы проверяющих
print("Оценки от проверяющих:")
print(reviewer1.rate_hw(student1, 'Python', 9))
print(reviewer1.rate_hw(student1, 'Python', 10))
print(reviewer1.rate_hw(student1, 'Git', 8))
print(reviewer2.rate_hw(student1, 'Git', 9))

print(reviewer1.rate_hw(student2, 'Python', 7))
print(reviewer1.rate_hw(student2, 'Python', 9))
print(reviewer2.rate_hw(student2, 'Java', 10))
print(reviewer2.rate_hw(student2, 'Git', 8))

# Методы студентов (оценка лекций)
print("\nОценки лекций от студентов:")
print(student1.rate_lecture(lecturer1, 'Python', 9))
print(student1.rate_lecture(lecturer1, 'Git', 10))
print(student2.rate_lecture(lecturer1, 'Python', 8))

print(student2.rate_lecture(lecturer2, 'Python', 9))
print(student2.rate_lecture(lecturer2, 'Java', 8))
print(student1.rate_lecture(lecturer2, 'Python', 7))  # Ошибка - лектор не закреплен за Git

# Метод add_courses
print("\nДобавление завершенных курсов:")
student1.add_courses('Основы алгоритмов')
student2.add_courses('Базы данных')

# Выводим информацию с помощью __str__
print("\n=== ИНФОРМАЦИЯ ОБ ОБЪЕКТАХ ===")
print("Проверяющие:")
print(reviewer1)
print()
print(reviewer2)
print("\nЛекторы:")
print(lecturer1)
print()
print(lecturer2)
print("\nСтуденты:")
print(student1)
print()
print(student2)

# Тестируем сравнение
print("\n=== СРАВНЕНИЕ ОБЪЕКТОВ ===")
print(f"lecturer1 > lecturer2: {lecturer1 > lecturer2}")
print(f"student1 < student2: {student1 < student2}")
print(f"lecturer1 == lecturer2: {lecturer1 == lecturer2}")
print(f"student1 >= student2: {student1 >= student2}")

# Используем функции для подсчета средних оценок
print("\n=== СРЕДНИЕ ОЦЕНКИ ПО КУРСАМ ===")
students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]

print(f"Средняя оценка за ДЗ по Python: {calculate_average_hw_grade(students_list, 'Python'):.2f}")
print(f"Средняя оценка за ДЗ по Git: {calculate_average_hw_grade(students_list, 'Git'):.2f}")
print(f"Средняя оценка за ДЗ по Java: {calculate_average_hw_grade(students_list, 'Java'):.2f}")

print(f"Средняя оценка за лекции по Python: {calculate_average_lecture_grade(lecturers_list, 'Python'):.2f}")
print(f"Средняя оценка за лекции по Git: {calculate_average_lecture_grade(lecturers_list, 'Git'):.2f}")
print(f"Средняя оценка за лекции по Java: {calculate_average_lecture_grade(lecturers_list, 'Java'):.2f}")

# Выводим детальную информацию об оценках
print("\n=== ДЕТАЛЬНАЯ ИНФОРМАЦИЯ ОБ ОЦЕНКАХ ===")
print("Оценки студентов:")
for student in students_list:
    print(f"{student.name} {student.surname}: {student.grades}")

print("\nОценки лекторов:")
for lecturer in lecturers_list:
    print(f"{lecturer.name} {lecturer.surname}: {lecturer.grades}")