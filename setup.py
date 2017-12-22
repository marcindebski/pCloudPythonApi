# -*- coding: utf-8 -*-
from setuptools import setup
from setuptools import find_packages


with open('README.md') as f:
    README = f.read()

with open('LICENSE') as f:
    LICENSE = f.read()

setup(
    name='pCloud API',
    version='0.1',
    description='API that provides access to the data in pCloud infrastructure',
    long_description=README,
    author='Marcin Debski',
    author_email='debski.marcin.r@gmail.com',
    url='https://github.com/marcindebski/pCloudPythonApi',
    license=LICENSE,
    packages=find_packages(exclude=('tests'))
)
