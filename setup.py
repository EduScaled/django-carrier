import os
from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django_carrier_client',
    version='0.2',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='A simple Django client for Carrier',
    url='https://github.com/EduScaled/django-carrier-client',
    author='Nick Lubyanov',
    author_email='lubyanov@gmail.com',
)