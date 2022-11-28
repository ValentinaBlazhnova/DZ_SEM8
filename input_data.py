from collections import defaultdict # Это подкласс класса словаря, который используется для возврата объекта, подобного словарю.

def teacher_add():
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    class_number = input('Введите класс: ')
    lesson =  input('Введите предмет: ') 
    grade = input('Введите оценку: ') 
    data_base = {}
    data_base = defaultdict(list)
    data_base[surname].append(name)
    data_base[surname].append(class_number)
    data_base[surname].append(lesson)
    data_base[surname].append(grade)
    return data_base

def student_add():
    surname = input('Введите фамилию: ')
    return surname

