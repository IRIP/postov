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
                CREATE TABLE IF NOT EXISTS vkdata( 
                        id integer, 
                        owner_id integer,
                        from_id integer,
                        created_by integer, 
                        date integer, 
                        text string, 
                        reply_owner_id integer, 
                        reply_post_id integer,
                        friends_only integer,
                        post_type string, 
                        signer_id integer,
                    CONSTRAINT name_unique UNIQUE (id))
                '''
            )
        #
        # except:
        #     print("Не удалось создать таблицу")

    def save(self, data):
        self.c.executemany("INSERT OR IGNORE INTO vkdata(id) VALUES (?,?,?)", data)
        # Сохранение (commit) изменений
        self.conn.commit()
        # Закрытие курсора, в случае если он больше не нужен
        self.conn.close()