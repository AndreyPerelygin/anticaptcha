from setuptools import setup, find_packages
import sys, os

version = '0.2'

setup(name='anticaptcha',
      version=version,
      description="0.2",
      long_description="""\
Python SDK for API 2.0 anti-captcha.com""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='anti-captcha.com SDK antigate',
      author='Andrey Perelygin',
      author_email='andrey@perelygin.me',
      url='perelygin.me',
      license='GNU GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
            "requests"
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
