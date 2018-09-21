import sqlite3


class sqlite_base:
    def __init__(self, name_db):
        self.conn = sqlite3.connect(name_db)
        self.c = self.conn.cursor()
        try:
            self.c.execute(
                '''CREATE TABLE vkdata ( id integer, data integer, txt text)''')
        except:
            print("Не удалось создать таблицу")

    def save(self, data):
        self.c.executemany("INSERT INTO vkdata VALUES (?,?,?)", data)
        self.conn.commit()
        self.conn.close()