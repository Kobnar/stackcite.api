import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.md')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'mongoengine',
    'marshmallow',
    'nose2',
    'cov-core'
]

setup(
    name='stackcite.api',
    version='0.0',
    description='A library of API resources for Stackcite services.',
    long_description=README + '\n\n' + CHANGES,
    author='Konrad R.K. Ludwig',
    author_email='konrad.rk.ludwig@gmail.com',
    url='http://www.konradrkludwig.com/',
    packages=['stackcite.api'],
    namespace_packages=['stackcite'],
    install_requires=requires
)
