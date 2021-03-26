# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in doctype_with_chart/__init__.py
from doctype_with_chart import __version__ as version

setup(
	name='doctype_with_chart',
	version=version,
	description='-',
	author='ALYF GmbH',
	author_email='hallo@alyf.de',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
