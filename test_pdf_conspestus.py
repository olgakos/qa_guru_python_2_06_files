# python test_pdf_conspectus.py

import os.path
from PyPDF2 import PdfReader

# docs_pdf_path = os.path.abspath(__file__) + 'resources' + 'docs-pytest-org-en-latest.pdf'
pdf_reader = PdfReader('./resources/docs-pytest-org-en-latest.pdf')
number_of_pages = len(pdf_reader.pages)

assert number_of_pages == 412
page = pdf_reader.pages[0]
text = page.extract_text()
print(text)
assert 'Jul 11, 2022' in text

# 01:12:57 - Работа с pdf.
# 01:13:40 - Устанавливаем библиотеку PyPDF2
# 01:17:40 - Берем текст страницы.
# 01:18:20 - Распечатываем текст.
# 01:20:00 - О библиотеках.
# 01:21:20 - Вопрос: «Является ли произвольный файл pdf или не является?».