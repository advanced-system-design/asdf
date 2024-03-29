from setuptools import setup, find_packages


setup(
    name = 'asdf',
    version = '0.1.0',
    author = 'Peleg Neufeld',
    description = 'An example package.',
    packages = find_packages(),
    install_requires = ['click', 'flask'],
    tests_require = ['pytest', 'pytest-cov'],
)
