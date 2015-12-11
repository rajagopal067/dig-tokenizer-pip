from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='digTokenizer',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='4.0',
    include_package_data=True,
    description='Tokenizer Utility',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/usc-isi-i2/dig-tokenizer',

    # Author details
    author='Dipsy Kapoor',
    author_email='dig-isi@isi.edu',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ],

    # What does your project relate to?
    keywords='dig lsh clustering tokenizer isi',
    package_data={
    'digTokenizer': ['spark-submit.sh','*.zip'],
    },
    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    #scripts = ['spark-submit.sh']

    entry_points ={
        'console_scripts': [
            'digTokenizer = digTokenizer.helper:main'
        ]
    },

)