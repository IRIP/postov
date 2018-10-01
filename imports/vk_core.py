import vk_api
import vk
from configs import passwords
# from configs import vk_settings
import time as t
import requests
import datetime

method = 'wall.get'
max_count = 2
values = {'owner_id': id}
key = 'items'
limit = None
stop_fn = None
negative_offset = False

class vk_parser:
    def __init__(self):
        """
            https://vk.com/dev/objects/post
            https://vk.com/dev/api_requests
        """
        login, password = passwords.login, passwords.password
        self.vk_session = vk_api.VkApi(login, password)

        try:
            self.vk_session.auth(token_only=True)
        except vk_api.AuthError as error_msg:
            print(error_msg)


    def get_info(self, id):
        """
            Получаем полную информацию из поста. Ссылки на фото, текст и т.п.
            одним пакетом.
        """

        tools = vk_api.VkTools(self.vk_session)
        wall = tools.get_all_iter(method, max_count, values, key, limit, stop_fn,
                                    negative_offset)
        return wall['items']


    def get_author_photo(self, photo_author):
        """
            Получаем фото автора поста/группы, загружаем, и складываем в папку
        """
        pass


    def get_title(self, title):
        """
            Генерируем заголовок из массива. Заголовок нужен для вывода списка
            записей по заголовку. Определить формирование заголовка...
        """
        pass


    def get_descriptions(self, excerpt):
        """
            Отрывок для descriptions (краткое описание).

        """
        pass


    def get_date_post(self, date_post):
        """
            Штамп даты и времени поста
        """
        pass


    def get_source_url(self, source_url):
        """
            Штамп урл.ссылки (источника)
        """
        pass


    def get_source_author(self, source_author):
        """
            Ссылка на группу/человека (без детализации до поста)
        """
        pass

    def get_photo(id):
        login = input('login: ')
        password = input('password: ')
        vkapi = vk.API(ap_id, login, password, access_token)
        album = vkapi.photos.getAlbums(owner_id=id, need_system=1)
        user_info = vkapi.users.get(user_ids=id)
        name = str(user_info[0]['first_name']) + ' ' + str(user_info[0]['last_name'])
        y, n = 0, 0
        while n <= 1000:
            photo = vkapi.photos.getAll(owner_id=id, count=200, offset=n)
            for i in photo['items']:
                for j in album['items']:
                    if j['id'] == i['album_id']:
                        if not os.path.exists(
                                "C:\\Users\\home\\Desktop\\vk_photo\\" + name + '\\' + str(
                                        j['title'])):
                            os.makedirs(
                                "C:\\Users\\home\\Desktop\\vk_photo\\" + name + '\\' + str(
                                    j['title']))
                        y += 1
                        print(y, [str(j['title'])], [str(i['id'])])
                        key = i.keys()
                        max_size = 0
                        for x in key:
                            if x.startswith('photo_') and (int(x[6:]) > max_size):
                                max_size = int(x[6:])
                        img = i['photo_' + str(max_size)]
                        date = datetime.datetime.fromtimestamp(i['date']).strftime(
                            '%Y.%m.%d-%H.%M')
                        h = httplib2.Http()
                        response, content = h.request(img)
                        foto = open(
                            'C:\\Users\\home\\Desktop\\vk_photo\\' + name + '\\' + str(
                                j['title']) + '\\' + str(
                                y) + ' ' + date + '.jpg', 'wb')
                        foto.write(content)
                        foto.close()
            n += 200

    if __name__ == '__main__':
        ids = input('id: ')
        get_photo(ids)


    def get_pictures(self, pictures):
        """
            Все фотографии поста (их нужно загрузить в папку upload/id_source/img
            проекта). то есть по [attachments] мне нужно получить значение
            [link][titel] [link][photo][photo_130] (любой размер)
            Получаем список альбомов (функция getAlbums возвращает словарь, с которым
                уже можно работать без сторонних модулей) и достаём из них id;
            Начинаем цикл по id альбомов;
            Получаем список всех фотографий (вот в таком виде);
            Начинаем цикл по фотографиям;
            Получаем ссылку на фото в максимальном доступном разрешении
                (если кто знает способ получить её проще, отпишите пожалуйста,
                в комменты);
            Скачиваем фото.
        """
        pass
        tools = vk_api.VkTools(self.vk_session)
        pic = tools.get_all('wall.get', {'owner_id': id})
        picture = []
        for i in range(1, 8):
            picture.append(info['attachments'][0]['photo']['src_small'])

        print(picture)

        # albums = [x['id'] for x in vkapi.photos.getAlbums(owner_id=yid)['items']]
        # # yid — идентификатор того, чьи альбомы скачиваем
        # for album in albums:
        #     photos = vkapi.photos.get(owner_id=yid, album_id=album)['items']
        #     for photo in photos:
        #         link = photo[sorted([x for x in photo.keys() if 'photo' in x],
        #                             key=lambda x: int(x.split('_')[1]))[-1]]
        #         urllib.request.urlretrieve(link, link.split('/')[-1])


    def get_music(self, music):
        """
            Все аудио поста (их нужно загрузить в папку upload/id_source/msc проекта)
            https://toster.ru/q/398540
        """
        pass


    def get_videos(self, videos):
        """
            Все видео поста (их нужно загрузить в папку upload/id_source/videos проекта)
        """
        pass
        r = api.wall.get(owner_id=id, count=7)[1:]
        for post in r:
            if 'video' in post['attachment']:
                access_key = post['attachment']['video']['access_key']
                owner = post['attachment']['video']['owner_id']
                vid = post['attachment']['video']['vid']

                template = 'https://vk.com/{}'
                print(template.format(api.video.get(
                    videos='{}_{}_{}'.format(owner, vid, access_key, extended=1))[1][
                                          'link']))
            else:
                print('No videos')


    def get_files(self, files):
        """
            Все файлы поста (их нужно загрузить в папку upload/id_source/files проекта)
        """
        pass

    # def get_members_list_id(owner_id):
    #     print('Начал работать в:', datetime.strftime(datetime.now(), "%H:%M:%S"))
    #
    # members_list = []  # изначально пустой список участников
    #
    # # первый запрос на 25000, чтобы получить первые 25000 и количество участников группы
    # r = requests.post(
    #     'https://api.vk.com/method/execute.Shmakov_getClub_members?group_id=' +
    #     str(owner_id) + '&offset=' + str(0) + '&count=' + str(
    #         25000) + '&access_token=' + token).json()['response']
    # members_count = r[0]  # количество участников
    #
    # print('Участников:', members_count)
    #
    # members_list.extend(r[1])  # вносим первые 25000 ID
    #
    # if members_count > 25000:
    #     print('Больше 25k участников. Запускаем цикл')
    #     for offset in range(25000, members_count, 25000):
    #         count = offset + 25000
    #
    #         r = requests.post(
    #             'https://api.vk.com/method/execute.Shmakov_getClub_members?group_id=' +
    #             str(owner_id) + '&offset=' + str(offset) + '&count=' + str(
    #                 count) + '&access_token=' + token).json()['response']
    #
    #         members_list.extend(r[1])  # вносим все последующие ID пачками по 25000 ID
    #
    #         # t.sleep(.35) #задержки между запросом --- ВАЖНО: если будут возникать проблемы - расскоментировать
    #     print('Цербер закончил сбор ID')
    # else:
    #     print('>25k участников. Закончили сбор ID')
    #
    # print(len(members_list))
    # write_txt(members_list, owner_id)  # записываем по 25000 ID
    # print('Данные успешно записаны')
    # print('Остановка:', datetime.strftime(datetime.now(), "%H:%M:%S"))
    #
    # get_ipython().magic('time get_members_list_id(12345)')