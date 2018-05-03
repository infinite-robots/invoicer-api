import os

config = {
    'SECRET' : os.urandom(24).encode('hex'),
    'DBURI'  : 'mysql+pymysql://root@localhost/invoicer',
}
