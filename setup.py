try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst') as f:
    README = f.read()

VERSION = '0.1.0'

setup(
    name = 'propublica-nonprofit',
    version = VERSION,
    description = 'A Python client for the ProPublica NonProfit Explorer API.',
    long_description = README,
    url = 'https://github.com/robrem/propublica-nonprofit',
    author = 'Rob Remington',
    author_email = 'rob@rob.codes',
    license = 'MIT',
    py_modules = ['nonprofit'],
    install_requires = ['httplib2'],
    platforms = ['any'],
    classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    test_suite='test',
)