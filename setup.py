#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

import versioneer
versioneer.VCS = 'git'
versioneer.versionfile_source = 'fx/_version.py'
versioneer.versionfile_build = 'fx/_version.py'
versioneer.tag_prefix = ''
versioneer.parentdir_prefix = 'fx-experiments-'


readme = open('README.rst').read()

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='fx-experiments',
    version=versioneer.get_version(),
    description='Experimental code using effects, and exploring API choices.',
    long_description=readme,
    author='Tom Prince',
    author_email='tom.prince@twistedmatrix.com',
    url='https://github.com/tomprince/fx-experiments',
    packages=[
        'fx', 'fx.tests',
    ],
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='effect',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='fx.tests',
    tests_require=test_requirements,
    cmdclass=versioneer.get_cmdclass(),
)
