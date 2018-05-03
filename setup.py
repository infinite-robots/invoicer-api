from setuptools import setup

setup(
    name     = 'invoicer-api',
    packages = ['invoicer'],
    include_package_data = True,
    install_requires = [
        'flask',
        'flask_sqlalchemy',
        'pymysql',
    ],
    
)
