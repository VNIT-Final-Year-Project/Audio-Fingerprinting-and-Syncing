from setuptools import setup
import os

with open('requirements.txt') as f:
      required = f.read().splitlines()

setup(name="Audio",
      version="0.1",
      packages=['Audio'],
      install_requires=required)