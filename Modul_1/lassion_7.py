# Дополнительное практическое задание по модулю: "Базовые структуры данных."
# Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности
# Предисловие:
# Сложность подобных задач заключается в:
# Отсутствии чёткого алгоритма решения. Его вы должны придумать сами на основе полученных ранее знаний (синтаксиса и инструментов).
# Объединении большинства тем изученного модуля.
# Предполагаемом большом объёме решения.
# Задание "Средний балл":
# Вам необходимо решить задачу из реальной жизни: "школьные учителя устали подсчитывать вручную средний балл каждого ученика, поэтому вам предстоит автоматизировать этот процесс":
# На вход даны следующие данные:
# Список: grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# Множество: students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
# Например: 'Aaron' - [5, 3, 3, 5, 4]
# Множество students содержит неупорядоченную последовательность имён всех учеников в классе.
# Напишите программу, которая составляет словарь, используя grades и students, где ключом будет имя ученика, а значением - его средний балл.
# Вывод в консоль:
# {'Aaron': 4.0, 'Bilbo': 2.25, 'Johhny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8}
# Примечания:
# Самостоятельно составлять (вручную) словарь не нужно (только изначально пустой).
# Для решения задачи нужно вспомнить функции sum, len и др. (подумать самому).
# Помните, что множество не является упорядоченной последовательностью. (нужен перевод в другой тип).


################ Решение ################
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students_avarege = {}

one_grades = grades[0]
one_gredes_ = list(one_grades[:5])
one_grades_avarege = sum(one_grades) / len(one_grades)

two_gredes = grades[1]
two_gredes_ = list(two_gredes[:5])
two_gredes_avarege = sum(two_gredes) / len(two_gredes)

three_gredes = grades[2]
three_gredes_ = list(three_gredes[:5])
three_gredes_avarege = sum(three_gredes) / len(three_gredes)

four_gredes = grades[3]
four_gredes_ = list(four_gredes[:5])
four_gredes_avarage = sum(four_gredes) / len(four_gredes)

fife_gredes = grades[4]
fife_gredes_ = list(fife_gredes[:5])
fife_gredes_avarage = sum(fife_gredes) / len(fife_gredes)

##################################
sort_student = sorted(students)

one_student = sort_student[0]
two_student = sort_student[1]
three_student = sort_student[2]
four_student = sort_student[3]
fife_student = sort_student[4]

students_avarege = {one_student:one_grades_avarege, two_student:two_gredes_avarege, three_student:three_gredes_avarege,
four_student:four_gredes_avarage, fife_student:fife_gredes_avarage}

print(students_avarege)