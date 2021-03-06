from __future__ import unicode_literals

import re

from setuptools import find_packages, setup


def get_version(filename):
    content = open(filename).read()
    metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", content))
    return metadata['version']

setup(
    name='Mopidy-GMusic',
    version=get_version('mopidy_gmusic/__init__.py'),
    url='http://github.com/hechtus/mopidy-gmusic/',
    license='Apache License, Version 2.0',
    author='Ronald Hecht',
    author_email='ronald.hecht@gmx.de',
    description='Google Play Music extension for Mopidy',
    long_description=open('README.rst').read(),
    packages=find_packages(exclude=['tests', 'tests.*']),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'setuptools',
        'Mopidy >= 1.0',
        'Pykka >= 1.1',
        'gmusicapi == 5.1.0-dev',
        'pycrypto >= 2.6.1',
    ],
    dependency_links=[
        ("http://github.com/simon-weber/Unofficial-Google-Music-API/"
         "tarball/develop#egg=gmusicapi-5.1.0-dev")
    ],
    test_suite='nose.collector',
    tests_require=[
        'nose',
        'mock >= 1.0',
    ],
    entry_points={
        'mopidy.ext': [
            'gmusic = mopidy_gmusic:GMusicExtension',
        ],
    },
    classifiers=[
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Multimedia :: Sound/Audio :: Players',
    ],
)
