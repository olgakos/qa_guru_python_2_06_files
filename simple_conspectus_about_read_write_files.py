import os

def test_simple1():
    2 > 1

def test_simple2():
    2 != 4

# ---- ТЕМА: размер файла. путь к файлу. -------

#библиотека os // import os
#путь к файлу
#распечатать ответ simple_conspectus_about_read_write_files.py::test_file_size0 PASSED [100%]4096
def test_file_size0():
    picture_size = os.path.getsize('./resources/sampleFile.jpeg')
    print(picture_size)

#test_take_file_from_resources.py
#библиотека os // import os
#путь к файлу
#проверка размера файла  [100%]4096
#узнать АБЛОЛЮТНЫЙ путь к файлу: [100%]D:\PythonParty\qa_guru_python_2_06_files\resources\sampleFile.jpeg
#Абсолютный путь нужен когда надо передать путь к файлу в какой-то метод
def test_file_size():
    picture_size = os.path.getsize('./resources/sampleFile.jpeg')
    assert picture_size == 4096
    #assert picture_size == 4097 #упадет
    print(os.path.abspath('./resources/sampleFile.jpeg')) #узнАем абсолютный путь к файлу

# запуск: python simple_conspectus_about_read_write_files.py
#команда напечатать путь к директории. Полезно для дебага. Или чтобы найти пусть к проекту или к Питону. Далее примеры
os.path.dirname(os.path.abspath('./resources/sampleFile.jpeg'))

#ЗДЕСЬ: join "для склеивания пути в разных ОС
#"а) узнай имя(current_dir) папки откуда был запущен скрипт (__file__), б) приклей к ней имя(current_dir=ресурсы) в) принт"
# отклик в Терминал:
# (venv) D:\PythonParty\qa_guru_python_2_06_files>python simple_conspectus_about_read_write_files.py
# D:\PythonParty\qa_guru_python_2_06_files\resources //(1)
# D:\PythonParty\qa_guru_python_2_06_files\resources\tmp //(2)

current_dir = os.path.dirname(os.path.abspath(__file__))
resources = os.path.join(current_dir, 'resources')
print(resources) #узнали путь до сюда (1)
resources_tmp = os.path.join(current_dir, 'resources', 'tmp')
print(resources_tmp) #узнали путь до сюда(2)

# --------ТЕМА: 24:20 - Рассматриваем чтение записи файла. -----------
# После выполнения этого фрагмента кода будет СОЗДАН в этой же папке новый текстовой файл, имеющий внутри текст
# разбор:
# путь к тому что надо создать/открыть + имя файла + ключ на запись?(w) + текст который хотим вписать
# f здесь - это объект в который пишем
# w здесь - это команда на запись
# после выполнения этой команды рядом (ожидание около 5 сек!) появится НОВЫЙ файл с текстом
with open('example.txt', 'w') as f:
    f.write('Hello world\nRow2\nIt\'s row3')

with open('example_created_file.txt', 'w') as f:
    f.write('My\ncreated\nfile2')

# логика: писать что-то можно только в ОТКРЫТЫЙ файл:
# Закрывать файл вручную - антипаттерн, нужно стараться использовать контекстный менеджер
# здесь: f это (объект)переменная .write это уже метод записи
f = open('example2.txt', 'w')
f.write('Hello22345')
f.close()
# f.write('Пробую записать что-то в уже ЗАХЛОПНУТЫЙ файл, д.б. ошибка')
# пример сообщения об ошибке ошибке:
# simple_conspectus_about_read_write_files.py:None (simple_conspectus_about_read_write_files.py)
# simple_conspectus_about_read_write_files.py:66: in <module>
#     f.write('Пробую записать что-то в уже ЗАХЛОПНУТЫЙ файл, д.б. ошибка')
# E   ValueError: I/O operation on closed file.


# r здесь - это команда на чтение
# открой СУЩЕСТВУЮЩИЙ  файл Х('example.txt') прочитай и напечатай в консоли
# (запуск: python test_csv_conspectus.py / python simple_conspectus_about_read_write_files.py)
with open('example.txt', 'r') as f:
    file = f.read()
    print(file)
    assert file == 'Hello world\nRow2\nIt\'s row3' #Полное соответствие
    assert 'It' in file #Полное соответствие (стокового значения)


# ----t2_6 00.38
#"Построчно зачитай существующий файл с существующим текстом" (?)
def test_rows():
    with open('example2.txt', 'r') as file:
        for i in file:

            assert i == 'Hello22345'
            print(i)


# ----t2_6 00.41
# ТЕМА: Вопрос: «Как дописывать файл?».
# Команда "а" допишет еще кусочек текст в начало файла example3x.txt
# будет дописывать при каждом запуске!
with open('example3_a.txt', 'a') as file:
    file.write('Hello\n')


# -----46:56 - Вопрос: «Чем отличается x?».
# не очень понятно. "Х пытается создать НОВЫЙ файл, но видит в директории уже существующий одноименный.
# Мол, нельза дубликат, надо давать новое имя. НЕЛЬЗЯ дополнить текстовой файл через Х
# NB! закомент. "через Х", потому что этот код не позволит записывать ВТОРИЧНО и будет давать ошибку
# with open('example4_x.txt', 'x') as file:
#     file.write('Hello\n')


# -----ТЕМА: 50:41 - Дополняем через "а".
# NB! закомент. "через Х", потому что этот код не позволит записывать ВТОРИЧНО и будет давать ошибку
# with open('example5_x.txt', 'x') as file:
#     file.write('Hello\n')

#Через "а" будет осуществляться бесконечная дозапись текта в указагнный файл
with open('example5_x.txt', 'a') as file:
    file.write('NewHello')