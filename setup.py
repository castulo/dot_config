"""Project setup script"""

import re
import ast
from setuptools import setup

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('dot_config/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name='dot_config',
    version=version,
    description='Config parser with dot notation',
    long_description=open('README.md'),
    author='Castulo Martinez',
    author_email='castulojavier@hotmail.com',
    url='https://github.com/castulo',
    download_url='',
    packages=['dot_config'],
    install_requires=[],
    extras_require={
        'dev': [
            'pylint',
            'mock',
            'coverage',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
)
