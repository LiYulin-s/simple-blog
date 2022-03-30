import sqlite3
import enum

class fileType(enum.Enum):
        ERROR = 0
        IMAGE = 1
        AUDIO = 2
        OTHER = 3

class targetFile():
    __name:str
    __data:bytearray
    __type:fileType
    def __init__(self,name:str,data:bytearray,type:fileType):
        self.__name = name
        self.__type = type
        self.__data = data


class datamgr():
    __cursor:sqlite3.Cursor
    __database:sqlite3.Connection
    sql_get_file:str = "SELECT * FROM file WHERE name = ?"
    def __init__(self):
        self.__database = sqlite3.connect("simple-blog.db",check_same_thread=False)
        self.__cursor = self.__database.cursor()
    def getFile(self,fileName:str) ->targetFile:
        self.__cursor.execute(sql_get_file,[fileName])
