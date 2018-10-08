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
    choise = input('\n >>> (0-выход): ')

    if int(choise) <= 0:
        # нулевой случай
        print('Ошибка ввода.')
        print('Работа программы прекращена')
        break

    elif int(choise) == 1:
        print('Выбран вариант № 1 \n')
        id = input('Введите id VK (впереди минус, если группа): \n')

        try:
            vk = vk_core.vk_parser()
            count = vk.get_posts_count(int(id))  # получаем кол-во постов
            print('Всего найдено:', count)

        except:
            print('Пустой запрос')

        # if not posts:
        #     print("Ошибка id-источника (вначале минус, если группа!")
        else:
            save = input('Сохранить данные? Да(y)/Нет(n): ')

            if save.lower() in ("да", "1", "y"):
                # проверяем, если базы нет, предлагаем создать.
                if not exists(name_db):
                    bd = input('Первый запуск программы. '
                               'Вы хотите создать базу данных? '
                               'Да(y)/Нет(n): ')
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
                post_list = vk.get_info(id)  # получили list с id всех записей
                # print(post_list)           # проверили работоспособность



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