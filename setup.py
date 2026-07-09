#used to configure and set the distribution of the project 
from setuptools import setup, find_packages

setup(
    name="src",
    version="0.0.1",
    author="Shivansh",
    author_email="Shivanshkale17@gmail.com",
    packages=find_packages()
)

"""
setuptools → A library used to package, install, and distribute Python projects.
             

setup() → Defines your project's information(metadata and packaging configuration) and tells Python how to package it.

find_packages() → Automatically finds all Python packages in your project, so you don't have to list them manually.
                 # Automatically finds all Python packages (folders with __init__.py)
"""