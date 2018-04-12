from setuptools import setup

setup(
    name='Flask-Gitkit',
    version='1.1',
    description='Google Identity Toolkit integration for Flask',
    py_modules=['flask_gitkit'],
    install_requires=[
        'Flask>=0.11',
        'identity-toolkit-python-client>=0.1',
    ])
