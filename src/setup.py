#!/usr/bin/python

from setuptools import setup, find_packages

setup(
    name   ='TagMyDatasetTools',
    version='0.1.0',
    author='Fernando Pujaico Rivera',
    author_email='fernando.pujaico.rivera@gmail.com',
    packages=['TagMyDatasetTools'],
    #scripts=['bin/script1','bin/script2'],
    url='https://github.com/trucomanx/TagMyDatasetTools',
    license='GPLv3',
    description='functions to process datasets',
    #long_description=open('README.txt').read(),
    install_requires=[
       "numpy", #"Django >= 1.1.1",
       "pandas" #
    ],
)

#! python setup.py sdist bdist_wheel
# Upload to PyPi
# or 
#! pip3 install dist/TagMyDatasetTools-0.1.tar.gz 
