# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='drugbox',
    version='0.1.0',
    description='Parsers for several drug info databases',
    long_description=readme,
    author='Emre Guney',
    author_email='emreguney@gmail.com',
    url='https://github.com/emreg00/drugbox',
    license=license,
    packages=find_packages(exclude=('test', 'doc'))
)

