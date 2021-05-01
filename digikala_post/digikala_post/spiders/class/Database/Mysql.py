import mysql.connector as connector
from colorama import Fore


class Mysql:
    def __init__(self, host, user, password, name):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__name = name
        try:
            self.__connection = connector.connect(
                host=self.__host, user=self.__user, passwd=self.__password, database=self.__name)
        except connector.Error as e:
            print(Fore.RED + f"Database cannot connect\n{e.msg}" + Fore.WHITE)
        self.__cursor = self.__connection.cursor()

    def query(self, query):
        try:
            self.__cursor.execute(query)
            return True
        except connector.Error as e:
            print(
                Fore.RED + f"Query dosen't execute successfully:\n{e.msg}" + Fore.WHITE)
            return False

    def commit(self):
        self.__connection.commit()
