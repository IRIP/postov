import vk_api
from configs import passwords



class vk_parser:
    def __init__(self):
        login, password = passwords.login, passwords.password
        self.vk_session = vk_api.VkApi(login, password)

        try:
            self.vk_session.auth(token_only=True)
        except vk_api.AuthError as error_msg:
            print(error_msg)

    def get_info(self, id):
        """
        Получает полную информацию из поста. Ссылки на фото, текст и т.п.
        :param id:
        :return:
        """
        tools = vk_api.VkTools(self.vk_session)
        wall = tools.get_all('wall.get', 10, {'owner_id': id})
        return wall['items']

    def get_photo_author(self, photo_author):
        """
        Получает фото автора поста/группы
        :param photo_author:
        :return:
        """
        pass

    def get_title(self, title):
        """
        Генерируем заголовок из массива
        :param title:
        :return:
        """
        pass

    def get_excerpt(self, excerpt):
        """
        Отрывок для descriptions (краткое описание)
        :param excerpt:
        :return:
        """
        pass

    def get_date_post(self, date_post):
        """
        Штамп даты и времени поста
        :param date_post:
        :return:
        """
        pass

    def get_source_url(self, source_url):
        """
        Штамп урл.ссылки (источника)
        :param source_url:
        :return:
        """
        pass

    def get_source_author(self, source_author):
        """
        Ссылка на группу/человека (без детализации до поста)
        :param source_author:
        :return:
        """
        pass

    def get_pictures(self, pictures):
        """
        Все фотографии поста (их нужно загрузить в папку upload/id_source/img проекта)
        :param pictures:
        :return:
        """
        pass

    def get_music(self, music):
        """
        Все аудио поста (их нужно загрузить в папку upload/id_source/msc проекта)
        :param music:
        :return:
        """
        pass

    def get_videos(self, videos):
        """
        Все видео поста (их нужно загрузить в папку upload/id_source/videos проекта)
        :param videos:
        :return:
        """
        pass

    def get_files(self, files):
        """
        Все файлы поста (их нужно загрузить в папку upload/id_source/files проекта)
        :param files:
        :return:
        """
        pass
