#!/usr/bin/python3
# ! -*- coding: utf-8 -*-

from apscheduler.schedulers.blocking import BlockingScheduler
from bs4 import BeautifulSoup
import urllib.request
from os import system
import json
import ssl
import codecs

# url сайта
url_avito = 'https://www.avito.ru/evpatoriya/vakansii'

# run script by timer
sched = BlockingScheduler()

def html_to_soup(link):
    """
        Читаем html и отправляем в bs4.
        item item_table clearfix js-catalog-item-enum js-item-trackable item-highlight
    """
    try:
        # make ssl certificate (for launch on windows)
        gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)

        with urllib.request.urlopen(link, context=gcontext) as response:
            # write html code to variable
            html = response.read()

        return BeautifulSoup(html, 'html.parser')

    except Exception as err:
        print('Error in html_to_soup')
        print(err.args)


def data_write_to_json(file, data_to_write):
    """
        пишем в json
    :param file:
    :param data_to_write:
    :return:
    """
    try:
        with codecs.open(file, 'w+', 'utf-8') as f:
            json.dump(data_to_write, f, indent=4, sort_keys=True, ensure_ascii=False)
        return True

    except IOError:
        # Error while write
        print("Ошибка: файл не существует. Write_to_json.")
        return False


def data_read_from_json(file):
    """
        Чтение файла json
    :param file:
    :return:
    """
    try:
        with codecs.open(file, 'r', encoding='utf-8', errors='ignore') as f:
            return json.load(f)

    except IOError:
        # Error
        print("Файл не существует. data_read_from_json")
        return False


def scan_by_timer():
    """
        Сканируем по времени
    :return:
    """
    promo_soup = html_to_soup(url_avito)

    try:
        promo = promo_soup.select(".item")
    except:
        print("Error in read .item by soup!")

    promo_array = []

    data_in_file = data_read_from_json('avito_data.json')

    # promo in all promo
    if promo:
        for item in promo:
            # id
            promo_id = item['id']

            # Название remove \n
            promo_title = item.select('.description-title-link js-item-link')[0].get_text().strip()

            # price with remove \n
            promo_price = item.select('.option price')[
                0].get_text().strip()

            # if promo have image -> image promo, select src and remove '//' in url
            if item.select_one('.img-link js-item-link '):
                promo_image = item.select_one('.photo-count-show')['src'][2:]
            else:
                promo_image = 'https://avatars2.githubusercontent.com/u/1342004?v=4&s=200'

            # make promo array
            item_array = {
                'id': promo_id if promo_id else 'id_error',
                'text': promo_title if promo_title else 'text_error',
                'price': promo_price if promo_price else 'price_error',
                'image': promo_image if promo_image else 'image_error'
            }

            # add promo array to list promo
            promo_array.append(item_array)

    # check read file
    # Dont write to file dublicate!!!
    if data_in_file != False and promo_array:

        for item_file in data_in_file:
            # for in array. Check all el. in array with el. in file.
            for item_arr in promo_array:
                index_arr = 0
                if int(item_file['id'][1:]) == int(item_arr['id'][1:]):
                    promo_array.pop(index_arr)

                index_arr += 1

    if data_write_to_json('data.json', promo_array) == True:
        print('Data was written!')
    else:
        print('Error while data write!')


# add task to timer
sched.add_job(scan_by_timer, 'interval', minutes=1)

# start timer
sched.start()