from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='echr_od_loader',
    version='0.1.0',
    description='Python library to load and manipulate the European Court of Human Rights datasets',
    long_description=long_description,
    long_description_content_type='text/markdown',  # Optional (see note above)
    url='https://github.com/aquemy/ECHR-OD_loader',  # Optional
    author='Alexandre Quemy',
    author_email='aquemy@pl.ibm.com',  # Optional
    classifiers=[ 
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='classification justice prediction',
    install_requires=requirements,
    project_urls={ 
        'Bug Reports': 'https://github.com/aquemy/ECHR-OD_loader/issues',
        'Say Thanks!': 'https://saythanks.io/to/aquemy',
        'Source': 'https://github.com/aquemy/ECHR-OD_loader',
    },
)