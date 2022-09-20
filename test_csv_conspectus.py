# python test_csv_conspectus.py
import csv

# t 00.55
# csv =  таблицы разделены запятыми
# пример лежит в Ресурсах - SampleCSVFile_11kb.csv

# №1
# здесь: .reader - это один ИЗ доступных стандартных методов...
# здесь: i тк это "многострочный файл" ?
# with open('resources/SampleCSVFile_11kb.csv') as csvfile:
#     csvfile = csv.reader(csvfile)
#     for i in csvfile:
#         print(i)
# #   РЕЗУЛЬТАТ: выведет в терминал весь большой текст


# №2
# with open('resources/SampleCSVFile_11kb.csv') as csvfile:
#     csvfile = csv.reader(csvfile)
#     for row in csvfile:
#         print(row)
# #   РЕЗУЛЬТАТ: выведет в терминал весь большой текст "по строкам" (?)"


# №3
# with open('resources/SampleCSVFile_11kb.csv') as csvfile:
#     csvfile = csv.reader(csvfile)
#     row_count = sum(1 for row in csvfile)
#     print(row_count)
#
# # ОТВЕТ: (venv) D:\PythonParty\qa_guru_python_2_06_files>python test_csv_conspectus.py
# # 100

# # №4
# # 01:03:58 - Как обратиться к csv по строке. (?, потом)
# with open('resources/SampleCSVFile_11kb.csv') as csvfile:
#     table = csv.reader(csvfile)
#     for row in table:
#         print(row[0])
# # ОТВЕТ:


# №5
# 01:08:41 - Меняем csv на table.
# Находим строку по ее индексу

with open('resources/SampleCSVFile_11kb.csv') as csvfile:
    table = csv.reader(csvfile)
    # row_count = sum(1 for row in table)
    for line_no, line in enumerate(table, 1):
        if line_no == 2:
            print(line[1])

#Ответ:
# (venv) D:\PythonParty\qa_guru_python_2_06_files>python test_csv_conspectus.py
# 1.7 Cubic Foot Compact "Cube" Office Refrigerators
#
# Верно, т.к. в теле файла было:
# 1,"Eldon Base for stackable storage shelf, platinum",Muhammed MacIntyre,3,-213.25,38.94,35,Nunavut,Storage & Organization,0.8
# 2,"1.7 Cubic Foot Compact ""Cube"" Office Refrigerators",Barry French,293,457.81,208.16,68.02,Nunavut,Appliances,0.58
# 3,"Cardinal Slant-D� Ring Binder, Heavy Gauge Vinyl",Barry French,293,46.71,8.69,2.99,Nunavut,Binders and Binder Accessories,0.39


# 01:10:40 - Что нужно для того, чтобы распечатать что-то в строке.
