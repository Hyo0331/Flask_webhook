db = {
    'user' : 'flask',
    'password' : '1111',
    'host' : 'localhost',
    'port' : '3306',
    'database' : 'board'
}


SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"
SQLALCHEMY_TRACK_MODIFICATIONS = False
