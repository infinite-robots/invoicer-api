from setuptools import setup

setup(
    name     = 'invoicer-api',
    version  = '0',
    packages = ['invoicer'],
    include_package_data = True,
    install_requires = [
        'mysqlclient',
        'flask',
        'flask_sqlalchemy',
        'Flask-Migrate'
    ],
)
