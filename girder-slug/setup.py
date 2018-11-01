#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    'girder>=3.0.0a1'
]

setup(
    author="Roni Choudhury",
    author_email='roni.choudhury@kitware.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    description='A Girder plugin to enable slugs for Collections, Folders, and Items',
    install_requires=requirements,
    license='Apache Software License 2.0',
    long_description=readme,
    include_package_data=True,
    keywords='girder-plugin, girder_slug',
    name='girder_slug',
    packages=find_packages(exclude=['test', 'test.*']),
    url='https://github.com/arclamp/girder-slug',
    version='0.1.0',
    zip_safe=False,
    entry_points={
        'girder.plugin': [
            'girder_slug = girder_slug:GirderPlugin'
        ]
    }
)
