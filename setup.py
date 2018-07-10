# -*- coding: utf-8 -*-

from setuptools import setup
from pip.req import parse_requirements
install_reqs = parse_requirements('./requirements.txt', session=False)
reqs = [str(ir.req) for ir in install_reqs]


with open('README.md') as f:
  readme = f.read()

with open('LICENSE') as f:
  license = f.read()

setup(
    name='dashtat',
    version='0.1.0',
    description='Dashboard Statistics',
    long_description=readme,
    author='Andy Rea',
    author_email='email@andrewrea.co.uk',
    url='https://github.com/reaandrew/dashtat',
    license=license,
    packages=['dashtat'],
    install_requires=reqs,
    include_package_data=True
)
