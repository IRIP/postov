# для работы с MongoDB

import pymongo


class sqlite_base:
    def __init__(self, name_db):
        """
            Запись результата в базу данных
        """
        self.conn = pymongo.MongoClient(name_db)


    def save(self, data):
        """
            Запись строки в mongodb
        :param data:
        :return:
        """
        pass