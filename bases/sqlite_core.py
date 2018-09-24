import sqlite3


class sqlite_base:
    def __init__(self, name_db):
        self.conn = sqlite3.connect(name_db)
        self.c = self.conn.cursor()
        try:
            self.c.execute(
                '''
                CREATE TABLE vkdata( 
                    id integer,  # id источника
                    author_photo,  # аватар автора поста
                    title,  # заголовок (генерируется)
                    descriptions,  # описание (генерируется)
                    date_post,  # дата написания поста
                    source_url,  # ссылка на пост на источнике
                    source_author,  # ссылка на автора поста
                    data integer,  # весь текст целиком
                    pictures,   # фото (ссылки (прямые на файлы))
                    music,   # аудио
                    hash_tags,  # теги 
                    quests,  # опрос
                    videos,  # ссылки на видео
                    links,  # прикрепленные в текст ссылки 
                    files,  # прикрепленные файлы
                    txt text  # чистый текст поста (со сссылками внутри и т.п.))
                '''
            )

        except:
            print("Не удалось создать таблицу")

    def save(self, data):
        self.c.executemany("INSERT INTO vkdata VALUES (?,?,?)", data)
        self.conn.commit()
        self.conn.close()