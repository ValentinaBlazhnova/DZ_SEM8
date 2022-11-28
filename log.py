from input_data import teacher_add as student_data
from input_data import student_add as lastname

def loger(student_data):
    with open('dnevnik.txt', 'a', encoding = 'utf-8') as file:
        for key, val in student_data.items():
            file.write('{}:{}\n'.format(key,val))
    print('Данные ученика добавлены')

def view_student(lastname):
    with open('dnevnik.txt', 'r', encoding = 'utf-8') as file:
        data = student_data[lastname]
        for lastname in file:
            if lastname in data:
                print(student_data.values())
        