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
                        vkdata_id,
                        id integer, 
                        from_id integer,
                        owner_id integer,
                        date integer, 
                        marked_as_ads integer,
                        post_type string, 
                        created_by integer, 
                        text string,
                         
                        reply_owner_id integer, 
                        reply_post_id integer,
                        friends_only integer,
                        signer_id integer,
                    CONSTRAINT name_unique UNIQUE (id))
                '''
            )
        self.c.execute(
                '''
                CREATE TABLE IF NOT EXISTS vkdatattachments( 
                        vkdata_id,
                        type integer, 
                        from_id integer,
                        owner_id integer,
                        date integer, 
                        marked_as_ads integer,
                        post_type string, 
                        created_by integer, 
                        text string, 
                        reply_owner_id integer, 
                        reply_post_id integer,
                        friends_only integer,
                        signer_id integer,
                    CONSTRAINT name_unique UNIQUE (id))
                '''
            )
        self.c.execute(
                '''
                CREATE TABLE IF NOT EXISTS vkdataAttachmenType( 
                        vkdata_id,
                        id, 
                                               
 
                    CONSTRAINT name_unique UNIQUE (id))
                '''
            )

    def save(self, data):
        self.c.executemany("INSERT OR IGNORE INTO vkdata(id) VALUES (?,?,?)", data)

        # Сохранение (commit) изменений
        self.conn.commit()

        # Закрытие курсора, в случае если он больше не нужен
        self.conn.close()