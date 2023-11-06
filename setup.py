from setuptools import setup, find_packages
import os

version = '0.2.5'
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='flowlogger',
    version=version,
    url='https://github.com/oblivisheee/flowlogger',
    author='oblivisheee',
    author_email='author@gmail.com',
    description=f'This is a small library for logging while training ML. Current version is {version}, its a feature-poor pre-alpha.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),    
    install_requires=['GPUtil', 'psutil'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6', 
)