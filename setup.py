from setuptools import setup

setup(
    name='teamswebhook',
    version='0.2.3',    
    description='A Python package for sendind Adaptive Card to teams from Python code.',
    author='Anatolii Veselyi',
    author_email='anatolii.veselyi@icloud.com',
    packages=['teamswebhook'],
    install_requires=['requests']
)