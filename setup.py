'''
Copyright (c) 2017, Jairus Martin.

Distributed under the terms of the MIT License.

The full license is in the file COPYING.txt, distributed with this software.

Created on Oct 24, 2017

@author: jrm
'''
from setuptools import setup, find_packages


setup(
    name="p4a-crystax",
    version="1.0",
    author="frmdstryr",
    author_email="frmdstryr@gmail.com",
    license='MIT',
    url='https://github.com/frmdstryr/p4a-crystax/',
    description="crystax python 2 and python 3 recipes for python-for-android",
    long_description=open("README.md").read(),
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'p4a_recipe': [
            'python2crystax = p4a_crystax.python2crystax.__init__:get_recipe',
            'python3crystax = p4a_crystax.python3crystax.__init__:get_recipe',
        ]
    }
)
