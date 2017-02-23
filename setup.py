from setuptools import setup

setup(
    name='Flask-Gitkit',
    version='1.0',
    description='Google Identity Toolkit integration for Flask',
    packages=['flask_gitkit'],
    install_requires=[
        'Flask>=0.11',
        'identity-toolkit-python-client>=0.1',
    ])
