#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

from lona_bootstrap_5 import VERSION_STRING

setup(
    include_package_data=True,
    name='lona-bootstrap-5',
    version=VERSION_STRING,
    author='Florian Scherf',
    url='https://github.com/lona-web-org/lona-bootstrap-5',
    author_email='f.scherf@pengutronix.de',
    license='MIT',
    packages=find_packages(),
    install_requires=[],
)
