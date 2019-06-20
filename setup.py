from setuptools import setup, find_packages
from codecs import open
import os
import re

with open("README.rst", "r") as f:
    long_description = f.read()

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()


def get_version():
    here = os.path.abspath(os.path.dirname(__file__))
    version_file = os.path.join(here, 'dictconfig', '__version__.py')

    with open(version_file, "r") as vf:
        lines = vf.read()
        version = re.search(r"^_*version_* = ['\"]([^'\"]*)['\"]", vf, re.M).group(1)
        return version


dictconfig_version = get_version()

setup(
    name='dictconfig',
    version=dictconfig_version,
    author='Adam Batten',
    author_email='adamjbatten@gmail.com',
    url='https://github.com/abatten/dictconfig',
    download_url="https://pypi.org/project/dictconfig",
    project_urls={
        'Source Code': "https://github.com/abatten/dictconfig"
        },
    description='A wrapper around configparser to help create dictionaries from parameter files',
    long_description=long_description,
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Operating System :: Unix",
        ],
    package_dir={"dictconfig": "dictconfig"},
    packages=find_packages(),
    include_package_data=True,
    keywords=("configparser parameters dictionaries"),
)
