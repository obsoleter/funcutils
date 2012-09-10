# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('readme.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='funcutils',
    version='0.0.1',
    description='Simple helper functions',
    long_description=readme,
    author='Jeremy Axmacher',
    author_email='jeremy@obsoleter.com',
    url='https://github.com/obsoleter/funcutils',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
