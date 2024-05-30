import os
import subprocess

# 1. перейдите в каталог PZ11. Выведите список всех файлов в этом каталоге.
# Имена вложенных подкаталогов выводить не нужно.

os.chdir(r'/home/student/Документы/Kim Yana is-22/PZ_11')
files = [f for f in os.listdir() if os.path.isfile(f)]
print("Список файлов в каталоге PZ_11:")
for file in files:
    print(file)


# 2. перейти в корень проекта, создать папку с именем test. В ней создать еще одну папку
# test1. В папку test переместить два файла из ПЗ6, а в папку test1 - один файл из ПЗ7.
# Файл из ПЗ7 переименовать в test.txt. Вывести в консоль информацию о размере
# файлов в папке test.

# os.chdir(r'/home/student/Документы/Kim Yana is-22')
# os.makedirs('test/test1')
# os.replace(r'PZ_6/PZ_6_1.py', 'test/PZ_6_1.py')
# os.replace(r'PZ_6/PZ_6_2.py', 'test/PZ_6_2.py')
# os.replace(r'PZ_7/PZ_7_1.py', 'test/test1/test.txt')
#
# total_size = sum(os.path.getsize(os.path.join('test', f)) for f in os.listdir('test'))
# print(f"Размер файлов в папке test: {total_size} байт")

# 3. перейти в папку с PZ11, найти там файл с самым коротким именем, имя вывести в
# консоль. Использовать функцию basename () (os.path.basename()).

os.chdir(r'/home/student/Документы/Kim Yana is-22/PZ_11')
files = os.listdir()

shortest_filename = None

for file in files:
    if shortest_filename is None or len(file) < len(shortest_filename):
        shortest_filename = file

print('Самое короткое имя имеет файл:', os.path.basename(shortest_filename))


# 4. перейти в любую папку, где есть отчет в формате .pdf и «запустите» файл в
# привязанной к нему программе. Использовать функцию os.startfile().

pdf_file = r'/home/student/Документы/Kim Yana is-22/PZ_13/PZ_13.pdf'
subprocess.call(['xdg-open', pdf_file])


# 5. удалить файл test.txt.

file = r'/home/student/Документы/Kim Yana is-22/test/test1/test.txt'

if os.path.exists(file):
    try:
        os.remove(file)
        print("Файл успешно удален")
    except OSError as e:
        print(f"Ошибка при удалении файла: {e}")
else:
    print("Ошибка: файл не найден")
