import sys
from imports import vk_core
from bases.sqlite_core import sqlite_base
from configs import bases
import os

to_dos = 0
name_db = 'bases.name_db'


print('Привет! Давай поработаем!')
print('1. Импорт источников')
print('2. Экспорт источников')
print('3. Вывести список источников')


def exists(path):
    try:
        os.stat(path)
    except OSError:
        return False
    return True


while True:
    choise = input('\n Выбери цифру нужного варианта: ')

    if int(choise) <= 0:
        # нулевой случай
        print('Введено отрицательное число или == 0.')
        print('Работа программы прекращена')
        break

    elif int(choise) == 1:
        print('Выбран вариант № 1 \n')
        id = input('Введите id источника: \n')

        posts = []

        try:
            vk = vk_core.vk_parser()
            posts = vk.get_info(int(id))
        except:
            pass

        if not posts:
            print("Ошибка id-источника")
        else:
            print('Количество постов:', len(posts))
            save = input('Вы хотите сохранить введенные данные? Да(y)/Нет(n): \n')
            if save.lower() in ("да", "1", "y"):
                if not exists(name_db):
                    bd = input('Первый запуск программы. '
                               'Вы хотите создать базу данных? '
                               'Да(y)/Нет(n): \n')
                    if bd.lower() in ("да", "1", "y"):
                        to_dos = 1
                    else:
                        to_dos = 2
                else:
                    to_dos = 1
            elif save.lower() in ("нет", "0", "n"):
                to_dos = 2

            if to_dos == 1:
                bases = sqlite_base(name_db)
                data = [(
                        posts[i]['id'], posts[i]['source_id'], posts[i]['date'],
                        posts[i]['text']) for i in range(len(posts)
                        )]
                bases.save(data)
            elif to_dos == 2:
                print('Начинаем сначала!')

    elif int(choise) == 2:
        print('Выбран вариант № 2')
        continue

    elif int(choise) == 3:
        print('Выбран вариант № 3')
        print('Выводим список всех источников с назначением: ')
        continue

    else:
        print('Выбран неверный вариант! Повторите ввод или 0 для выхода')
        continue