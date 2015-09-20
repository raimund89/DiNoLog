# -*- coding: utf-8 -*-

"""
    DiNoLog - Distributed Node Logging System for Python
    Copyright (C) 2015  Raimond Frentrop

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""

from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()

setup(name='DiNoLog',
      version='0.0.1',
      description='Distributed Node Logging for Python',
      long_description=readme(),
      classifiers=[
            'Development Status :: 1 - Planning',
            'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
            'Framework :: Twisted'
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.2',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
      ],
      url='http://github.com/raimund89/DiNoLog',
      author='Raimond Frentrop',
      author_email='raimund89@gmail.com',
      license='GPLv2',
      packages=['DiNoLog'],
      install_requires=[
          'twisted',
      ],
      include_package_data=True,
      zip_safe=False)
