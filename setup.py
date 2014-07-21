import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

CONTROLLER = True
COMPUTE_NODE = True

requires = ['flask', 'gunicorn', 'requests', 'mako',
            'nose', 'coverage', 'watchdog']
scripts = []

setup(name='meow-meow',
      version='0.1',
      description='meow',
      long_description='meow meow~',
      classifiers=["Programming Language :: Python :: 3.4"],
      author='Teerasak Kroputaponchai',
      author_email='tkroputa@gmail.com',
      # scripts = scripts,
      # license = 'xxx License',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      )
