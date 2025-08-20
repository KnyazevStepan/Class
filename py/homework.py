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


# Тестирование
print("=== ТЕСТИРОВАНИЕ ===")

# Создаем объекты
lecturer1 = Lecturer('Иван', 'Иванов')
lecturer2 = Lecturer('Петр', 'Петров')
reviewer = Reviewer('Some', 'Buddy')
student1 = Student('Ruoy', 'Eman', 'M')
student2 = Student('Анна', 'Смирнова', 'Ж')

# Настраиваем курсы
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Введение в программирование']
student2.courses_in_progress += ['Python', 'Java']

lecturer1.courses_attached += ['Python', 'Git']
lecturer2.courses_attached += ['Python', 'Java']
reviewer.courses_attached += ['Python', 'Git']

# Выставляем оценки
reviewer.rate_hw(student1, 'Python', 9)
reviewer.rate_hw(student1, 'Python', 10)
reviewer.rate_hw(student1, 'Git', 8)

reviewer.rate_hw(student2, 'Python', 7)
reviewer.rate_hw(student2, 'Python', 9)
reviewer.rate_hw(student2, 'Java', 10)

student1.rate_lecture(lecturer1, 'Python', 9)
student1.rate_lecture(lecturer1, 'Git', 10)
student2.rate_lecture(lecturer2, 'Python', 8)
student2.rate_lecture(lecturer2, 'Java', 9)

# Тестируем __str__
print("\n=== ИНФОРМАЦИЯ О ПРЕПОДАВАТЕЛЯХ ===")
print(reviewer)
print("\n" + "-" * 30)
print(lecturer1)
print("\n" + "-" * 30)
print(lecturer2)

print("\n=== ИНФОРМАЦИЯ О СТУДЕНТАХ ===")
print(student1)
print("\n" + "-" * 30)
print(student2)

# Тестируем сравнение
print("\n=== СРАВНЕНИЕ ===")
print(f"lecturer1 > lecturer2: {lecturer1 > lecturer2}")
print(f"lecturer1 < lecturer2: {lecturer1 < lecturer2}")
print(f"student1 == student2: {student1 == student2}")
print(f"student1 >= student2: {student1 >= student2}")