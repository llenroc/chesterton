import os
import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass into pytest")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = '-n auto'

    def run_tests(self):
        import shlex
        import pytest
        errno = pytest.main(shlex.split(self.pytest_args))
        sys.exit(errno)


version_contents = {}
with open("robotic_bow/version.py", "r", encoding='utf-8') as f:
    exec(f.read(), version_contents)


with open("README.md", "r") as f:
    long_description = f.read()


deps = [
    'fast_arrow',
    'tornado'
#    'click',
#    'pathlib2',
#    'requests',
#    'pandas>=0.23.2',
#    'numpy',
#    'yarl'
]


test_deps = [
    'pipenv',
    'pytest',
    'pytest-cov',
    'detox',
    'flake8',
    'vcrpy']


setup(name='robotic_bow',
    version=version_contents['VERSION'],
    description='Order execution agent for fast_arrow on Robinhood',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Weston Platter',
    author_email='westonplatter@gmail.com',
    url='https://github.com/westonplatter/robotic_bow/',
    license='MIT License',
    python_requires=">=3.5",
    packages=['robotic_bow'],
    # package_data={'fast_arrow': ['ssl_certs/certs.pem']},
    install_requires=deps,
    tests_require=test_deps,
    cmdclass={'test': PyTest},
    project_urls={
        'Issue Tracker': 'https://github.com/westonplatter/robootic_bow/issues',
        'Source Code': 'https://github.com/westonplatter/robotic_bow',
    }
)
