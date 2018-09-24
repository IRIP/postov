import vk_api
from configs import passwords
import time as t



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
            Получаем полную информацию из поста. Ссылки на фото, текст и т.п.
            одним пакетом.
        """
        tools = vk_api.VkTools(self.vk_session)
        wall = tools.get_all('wall.get', 10, {'owner_id': id})
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


    def get_pictures(self, pictures):
        """
            Все фотографии поста (их нужно загрузить в папку upload/id_source/img проекта)
        """
        pass


    def get_music(self, music):
        """
            Все аудио поста (их нужно загрузить в папку upload/id_source/msc проекта)
        """
        pass


    def get_videos(self, videos):
        """
            Все видео поста (их нужно загрузить в папку upload/id_source/videos проекта)
        """
        pass


    def get_files(self, files):
        """
            Все файлы поста (их нужно загрузить в папку upload/id_source/files проекта)
        """
        pass
