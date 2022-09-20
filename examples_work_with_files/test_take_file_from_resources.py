import os

def test_take_file_from_resources():
    #('./resources/sampleFile.jpeg'))
    #D:\PythonParty\qa_guru_python_2_06_files\resources\sampleFile.jpeg
    #print(os.path.to_resources('sampleFile.jpeg')) #нет

    picture_size = os.path.to_resources.getsize('sampleFile.jpeg')
    print(picture_size)


# ...реализацию хелпера который точно строит абсолютный путь на основе пути относительного папки resources
# browser.element('[id="uploadPicture"]').send_keys(path.to_resource('photo.jpg'))
# и не важно где этот код будет вызван, в каком бы файле с тестом он ни был
# всегда нужный файл лежащий внутри resoureses/ будет найден