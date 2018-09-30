import sys
from imports import vk_core
from bases.sqlite_core import sqlite_base
from configs import bases
import os
import json
import requests
import itertools
import operator
import pymongo

to_dos = 0
name_db = 'bases.name_db'


print('Привет! Давай поработаем!')
print('1. Импорт источников')
print('2. Экспорт источников')
print('3. Вывести список источников')
print('4. Запустить кросс-постинг.')


def exists(path):
    try:
        os.stat(path)
    except OSError:
        return False
    return True


while True:
    choise = input('\n Выбери цифру нужного варианта (0 - выход: ')

    if int(choise) <= 0:
        # нулевой случай
        print('Введено отрицательное число или == 0.')
        print('Работа программы прекращена')
        break

    elif int(choise) == 1:
        print('Выбран вариант № 1 \n')
        id = input('Введите id VK (впереди минус, если группа): \n')

        posts = []

        try:
            vk = vk_core.vk_parser()
            posts = vk.get_info(int(id))  # получаем список постов
            print(posts)
            by_name = operator.itemgetter('id')
            result = []
            for id, grp in itertools.groupby(sorted(posts, key=by_name), key=by_name):
                playing = set(itertools.chain.from_iterable(x['attachments'] for x
                              in grp))
            # Если порядок `игры` важен, используйте` collections.OrderedDict`
            # playing = collections.OrderedDict.fromkeys (
            # itertools.chain.from_iterable (x ['playing'] for x в grp))
                result.append({'id': id, 'attachments': list(playing)})
            print(result)

        except:
            print('none')

        if not posts:
            print("Ошибка id-источника (вначале минус, если группа!")
        else:
            print('Найдено постов:', len(posts))
            save = input('Вы хотите сохранить введенные данные? Да(y)/Нет(n): \n')

            if save.lower() in ("да", "1", "y"):
                # проверяем, если базы нет, предлагаем создать.
                if not exists(name_db):
                    bd = input('Первый запуск программы. '
                               'Вы хотите создать базу данных? '
                               'Да(y)/Нет(n): \n')
                    if bd.lower() in ("да", "1", "y"):
                        to_dos = 1
                    else:
                        to_dos = 2
                # если база создана, то переходим в to_dos
                else:
                    to_dos = 1

            elif save.lower() in ("нет", "0", "n"):
                to_dos = 2

            if to_dos == 1:
                bases = sqlite_base(name_db)
                data = [
                        (
                            posts[i]['id'],
                            posts[i]['date'],
                            posts[i]['text']) for i in range(len(posts)
                        )
                    ]
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

    elif int(choise) == 4:
        print('Выбран вариант № 4')
        print('Начинаем кросс-постинг...')
        continue

    else:
        print('Выбран неверный вариант! Повторите ввод или 0 для выхода')
        continue