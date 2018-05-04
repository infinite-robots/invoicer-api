from setuptools import setup

setup(
    name     = 'invoicer-api',
    version  = '0',
    packages = ['invoicer'],
    include_package_data = True,
    install_requires = [
        'flask',
        'flask_sqlalchemy',
        'pymysql',
    ],
    scripts = [
        'bin/invoicer-createdb.py'
    ]
)
