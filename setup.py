from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), 'r+') as f:
    long_description = f.read()

setup(
    
    name='brkout',

    version='0.6',

    description='A game combining the concept of prison escape and brick breaking', 

    long_description=long_description,

    url='https://github.com/thealphadollar/brkout',

    author='thealphadollar', 

    author_email='shivam.cs.iit.kgp@gmail.com',

    classifiers=[
        'Development Status :: 4 - Beta',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'
    ],

    keywords='game prison brkout brick_break',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    include_package_data=True,

    install_requires=['pygame'],

    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    entry_points={
        'console_scripts': [
            'brkout=game:main',
        ],
    },
)
