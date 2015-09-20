# -*- coding: utf-8 -*-

from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()

setup(name='DiNoLog',
      version='0.1',
      description='Distributed Node Logging for Python',
      long_description=readme(),
      classifiers=[
            'Development Status :: 1 - Planning',
            'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
            'Framework :: Twisted'
            'Programming Language :: Python :: 3',
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
