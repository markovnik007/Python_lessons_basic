__author__ = 'Вторушин Марк Викторович'
# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

import os
import shutil

def new_dir(name):
    dir = os.path.join(name)
    try:
        os.makedirs(dir)
        print('Создана папка ' + name)
    except FileExistsError:
        print('Директория с таким именем уже существует')

def dir_del(rdir):
    choice = input('{} {} {}'.format('Удалить? ', rdir, '? Y/N'))

    if choice == 'y' or choice == 'Y':
            os.removedirs(rdir)
            print('Вы успешно удалили ' + rdir)
    else:
        print('Операция отменена')

def cd(dir):
    choice = input('{} {} {}'.format("Сменить директорию?", dir, "? Y/n"))

    if choice == "y" or choice == "Y":
        os.chdir(dir)
        print("Вы перешли в папку:", dir)
    else:
        print("Ну и ладно... не очень и хотелось")

def remove_duplicates(dirname):
    file_list = os.listdir(dirname)
    double_count = 0
    for f in file_list:
        fullname = os.path.join(dirname, f)
        if fullname.endswith('.bak'):
            os.remove(fullname)
            if not os.path.exists(fullname):
                double_count += 1
                print("Файл", fullname, "был успешно удален")
    return double_count

def duble_files(dirname):
    print("Создание бэкапов в текущей директории")
    file_list = os.listdir(dirname)
    i = 0
    while i < len(file_list):
        duplicate_file(file_list[i])
        i += 1

def duplicate_file(filename):
    if os.path.isfile(filename):
        newfile = filename + ".bak"
        shutil.copy(filename, newfile)
        print(newfile)
        if os.path.exists(newfile):
            print("Файл", newfile, "был успешно создан")
            return True
        else:
            print("Возникли проблемы копирования")
            return False

def del_file(filename):
    choice = input('{} {} {}'.format('Удалить? ', filename, '? Y/N'))
    if os.path.isfile(filename):
        if choice == 'y' or choice == 'Y':
            os.remove(filename)
            print('Вы успешно удалили ' + filename)
        else:
            print('Операция отменена')

print("Привет программист)")
answer = ""
while answer != "q":
    answer = input("Поработаем? (Y/N/q)")
    if answer == "Y" or answer == "y":
        print("1) Покажу все файлы в директории")
        print("2) Создам директории dir_1 - dir_9")
        print("3) Удалю директории в данной папке")
        print("4) Продублирую файлы в текущей директории")
        print("5) Удалю дубликаты файлов")
        print("6) Продублирую указанный файл")
        print("7) Удалю указаный файл")
        print("8) Сменить рабочую директорию")
        print("9) Покажу текущую рабочую директорию")
        choice = int(input("Что будем делать?"))

        if choice == 1:
            print(os.listdir())
        elif choice == 2:
            if __name__ == "__main__":
                for count in range(1, 10):
                    new_dir('{}_{}'.format('dir', count))
        elif choice == 3:
            if __name__ == "__main__":
                for count in range(1, 10):
                    dir_del('{}_{}'.format('dir', count))
        elif choice == 4:
            duble_files(".")
        elif choice == 5:
            print("Удаление дубликатов в директории")
            dirname = input("Укажите имя директории:")
            count = remove_duplicates(dirname)
            print("Удалено файлов: ", count)
        elif choice == 6:
            print("Дублирование указанного файла")
            filename = input("Укажите имя файла:")
            duplicate_file(filename)
        elif choice == 7:
            print("Удаление указанного файла")
            filename = input("Укажите имя файла: ")
            del_file(filename)
        elif choice == 8:
            print("Текущая рабочая директория:", os.getcwd())
            dir = input("Куда желаете перейти?")
            cd(dir)
        elif choice == 9:
            print("Текущая рабочая директория:", os.getcwd())
        else:
            pass
    else:
        pass
    if answer == "N" or answer == "n" or answer == "q":
        print("Давай досвидания!")
        break
    else:
        pass

