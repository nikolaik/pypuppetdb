import sys
import os
import codecs

from setuptools import setup
from setuptools.command.test import test as TestCommand

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


class Tox(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        errno = tox.cmdline(self.test_args)
        sys.exit(errno)

with codecs.open('README.rst', encoding='utf-8') as f:
    README = f.read()

with codecs.open('CHANGELOG.rst', encoding='utf-8') as f:
    CHANGELOG = f.read()

packages = [
    'pypuppetdb',
    'pypuppetdb.api',
    ]

setup(
    name='pypuppetdb',
    version='0.0.2',
    author='Daniele Sluijters',
    author_email='daniele.sluijters+pypi@gmail.com',
    packages=packages,
    url='https://github.com/nedap/pypuppetdb',
    license=open('LICENSE').read(),
    description='Library for working with the PuppetDB REST API.',
    long_description='\n'.join((README, CHANGELOG)),
    package_data={'': ['LICENSE', 'CHANGELOG.rst', ], },
    include_package_data=True,
    keywords='puppet puppetdb',
    tests_require=['tox'],
    cmdclass={'test': Tox},
    install_requires=[
        "requests >= 1.2.3",
        "pytz == 2013b",
        ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries'
        ],
    )
