#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
===============================
HtmlTestRunner
===============================


.. image:: https://img.shields.io/pypi/v/gfanki.svg
        :target: https://pypi.python.org/pypi/gfanki
.. image:: https://img.shields.io/travis/st-walker/gfanki.svg
        :target: https://travis-ci.org/st-walker/gfanki

Create custom German Frequency List Anki Decks from open sources


Links:
---------
* `Github <https://github.com/st-walker/gfanki>`_
"""

from setuptools import setup, find_packages

requirements = ['Click>=6.0', ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Stuart Walker",
    author_email='stuart.derek.walker@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Create custom German Frequency List Anki Decks from open sources",
    entry_points={
        'console_scripts': [
            'gfanki=gfanki.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=__doc__,
    include_package_data=True,
    keywords='gfanki',
    name='gfanki',
    packages=find_packages(include=['gfanki']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/st-walker/gfanki',
    version='0.1.0',
    zip_safe=False,
)
