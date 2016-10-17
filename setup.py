import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-boolean-switch',
    version='0.2.8.5',
    packages=['boolean_switch'],
    include_package_data=True,
    description='Django app to switch boolean fields from list view',
    long_description=README,
    url='https://github.com/makeev/django-boolean-switch',
    author='Mikhail Makeev',
    author_email='mihail.makeev@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
