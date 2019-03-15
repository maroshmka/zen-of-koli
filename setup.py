
from setuptools import setup, find_packages

setup(
    name='zen-of-koli',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Ultimite guide to life, python and all.',
    long_description=open('README.txt').read(),
    url='https://github.com/maroshmka/zen-of-koli',
    author='Mario Hunka',
    author_email='hunka.mario@gmail.com'
)