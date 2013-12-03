#from distutils.core import setup
from setuptools import setup

setup(name='shadowdice',
    version='1.0a1',
    description="Tools for Shadowrun 5e.",
    url="https://github.com/dclements/shadowdice",
    classifiers=[
      'Programming Language :: Python :: 3'
    ],
    license='MIT',
    packages=['shadowdice'],
    include_package_data=True,
    test_suite = 'shadowdice.tests')
