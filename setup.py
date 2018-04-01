#!/usr/bin/env python
# -*- coding: utf-8 -*

import os

from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(
    name='persistent-celery-beat-scheduler',
    version='0.1.0',
    packages=find_packages('src', exclude=('tests',)),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    description=(
        'Celery Beat Scheduler that stores the scheduler data in Redis.'
    ),
    author='Richard O\'Dwyer',
    author_email='richard@richard.do',
    license='Apache 2',
    long_description='https://github.com/richardasaurus/persistent-celery-beat-scheduler',
    install_requires=install_requires,
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
