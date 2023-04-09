from setuptools import setup, find_packages

setup(
    name='bloxlib',
    version='1.0.0',
    description='A module for interacting with Roblox instances',
    author='ElCapor',
    author_email='EpicSpellBreaker@protonmail.ch',
    packages=find_packages(),
    install_requires=["pymem"],
)