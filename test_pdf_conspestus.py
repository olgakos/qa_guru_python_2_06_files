# python test_pdf_conspestus.py
import os.path

# 01:12:57 - Работа с pdf.
# # 01:13:40 - Устанавливаем библиотеку PyPDF2
# # 01:17:40 - Берем текст страницы.


from PyPDF2 import PdfReader

# 1
# docs_pdf_path = os.path.abspath(__file__) + 'resources' + 'docs-pytest-org-en-latest.pdf'
pdf_reader = PdfReader('./resources/docs-pytest-org-en-latest.pdf')
number_of_pages = len(pdf_reader.pages)
print(number_of_pages)

#Ответ 412
# При опечатке и вимени файла%
# (venv) D:\PythonParty\qa_guru_python_2_06_files>python test_pdf_conspectus.py
# C:\Python39\python.exe: can't open file 'D:\PythonParty\qa_guru_python_2_06_files\test_pdf_conspectus.py': [Errno 2] No such file or directory


# 2 # 01:18:20 - Распечатываем текст.
pdf_reader = PdfReader('./resources/docs-pytest-org-en-latest.pdf')
number_of_pages = len(pdf_reader.pages)
assert number_of_pages == 412 # + проверка
page = pdf_reader.pages[0]
text = page.extract_text()
print(text)
assert 'Jul 11, 2022' in text # + проверка

# ОТВЕТ:
# (venv) D:\PythonParty\qa_guru_python_2_06_files>python test_pdf_conspestus.py
# 412
# pytest Documentation
# Release 0.1
# holger krekel, trainer and consultant, https://merlinux.eu/
# Jul 11, 2022


# 01:20:00 - О библиотеках.
# 01:21:20 - Вопрос: «Является ли произвольный файл pdf или не является?».