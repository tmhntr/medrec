#!/usr/bin/env python
from setuptools import setup, find_packages
import pkg_resources
import os
import sys


if os.environ.get('CONVERT_README'):
    import pypandoc

    long_description = pypandoc.convert('README.md', 'rst')
else:
    long_description = ''

version = sys.version_info[:2]

VERSION = '0.1.1'

install_requires = ['customtkinter']
extras_require = {}

setup(name='medrecs',
      version=VERSION,
      description="A simple medical records app",
      long_description=long_description,
      author='Timothy Hunter',
      author_email='thunte27@uwo.ca',
      url='https://github.com/tmhntr/medical_records_app',
      license='MIT',
      packages=find_packages(exclude=['tests', 'tests.*']),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      extras_require=extras_require,
      entry_points={'console_scripts': [
          'main = medrecs.app:main']})