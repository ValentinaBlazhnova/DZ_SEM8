from input_data import teacher_add, student_add
from log import loger, view_student

def menu():
    print('Введите "0", если Вы учитель ')
    print('Введите "1", если Вы ученик')
    flag = int(input())
    if flag == 0:
        add_stud = teacher_add()
        loger(add_stud)
    elif flag == 1:
        student = student_add()
        view_student(student)
    else:
        print("Введено неверное значение, введите 0 или 1")
