#!/usr/bin/env python

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setup(name='reedmuller',
      version='1.1.2',
      description='Reed-Muller encoding and decoding',
      author='Sebastian Raaphorst',
      author_email='srcoding@gmail.com',
      url='https://github.com/sraaphorst/reedmuller',
      packages=['reedmuller'],
      long_description=long_description,
      long_description_content_type="text/markdown",
      classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Mathematics',
        ],
      keywords='mathematics combinatorics codes reedmuller',
      license='Apache 2.0'
      )
