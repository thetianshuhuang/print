
from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='printtools',
    version='1.2',
    packages=['print'],
    license='MIT',
    install_requires='pyfiglet',
    author='Tianshu Huang',
    author_email='thetianshuhuang@gmail.com',
    description=(
        'Collection of print utilities making heavy use of ANSI '
        'escape sequences with PyFiglet integration'),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/thetianshuhuang/print',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)
