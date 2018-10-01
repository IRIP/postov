import sqlite3


class sqlite_base:
    def __init__(self, name_db):
        """
            Запись результата в базу данных
        """
        # Connection объект олицетворяет базу данных
        self.conn = sqlite3.connect(name_db)

        # Создание таблицы
        self.c = self.conn.cursor()

        # Вставка ряда данных
        self.c.execute(
                '''
                CREATE TABLE IF NOT EXISTS source( 
                        post_id,
                        id integer, 
                        date date,
                        text integer,
                        lat int ,
                        lng int,
                        place_id integer ,                        
                        post_source integer,
                        profiles integer,
                    CONSTRAINT name_unique UNIQUE (post_id))
                '''
            )
        self.c.execute(
                '''
                CREATE TABLE IF NOT EXISTS attachments( 
                        vkdata_id,
                        id int,
                        type integer,
                        dict integer
                    CONSTRAINT name_unique UNIQUE (id))
                '''
            )


    def save(self, source, attachments):
        self.c.executemany("INSERT OR IGNORE INTO source(id) VALUES (?,?,?)", source)
        self.c.executemany("INSERT OR IGNORE INTO attachments(id) VALUES (?,?,?)",
                           attachments)

        # Сохранение (commit) изменений
        self.conn.commit()

        # Закрытие курсора, в случае если он больше не нужен
        self.conn.close()