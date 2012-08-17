import os
from setuptools import setup, find_packages

# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "ar_client",
    version = "0.0.1",
    author = "Chris Bun",
    author_email = "chrisbun@gmail.com",
    description = ("The control daemon for the Assembly Service"),
    url = "http://www.kbase.us/services/assembly",
    packages=find_packages(),
    install_requires=['pika>=0.9.5',
                      'pymongo>=2.2.1',
                      'requests>=0.13.6']
    include_package_data=True,
    long_description=read('README.md'),
    entry_points={'console_scripts':[
            'arast-server = lib.arastd',
            'arast-compute = lib.ar_computed']},
    package_data = {'':['*.conf']},
)