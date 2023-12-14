from urllib.parse import quote_plus
from os.path import dirname , abspath, join

BASEDIR = abspath(dirname(dirname(__file__)))

class DB:
    def sqlite_uri(self):
        db_path = join(BASEDIR, 'db', 'data.sqlite')
        return f'sqlite:///{db_path}'


    def postgres_uri(self):
        dialect = 'postgresql'
        host = 'postgresql'
        db = 'db_name'
        user = 'db_user'
        port = '5432'
        password = ''
        db_uri = f'{dialect}://{user}:{quote_plus(password)@{host}:{port}/{db}}'
        return db_uri()

    def mysql_uri(self):
        dialect = 'mysql+pymysql'
        host = 'localhost'
        db = 'db_name'
        user = 'root'
        port = '3306'
        password = ''
        db_uri = f'{dialect}://{user}:{quote_plus(password)@{host}:{port}/{db}}'
        return db_uri()