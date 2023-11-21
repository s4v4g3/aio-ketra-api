# coding: utf-8

"""
    Ketra Lighting API

    Control your Ketra lights  # noqa: E501

    The version of the OpenAPI document: 1.4.0
    Generated by: https://openapi-generator.tech
"""

import sys
from setuptools import setup, find_packages  # noqa: H301
import pathlib

if sys.version_info < (3, 6):
    raise RuntimeError("aioketraapi requires Python 3.6+")

HERE = pathlib.Path(__file__).parent

NAME = "aioketraapi"
VERSION = "0.1.12"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]
REQUIRES.append("aiohttp >= 3.0.0")


def read(f):
    return (HERE / f).read_text("utf-8").strip()


setup(
    name=NAME,
    version=VERSION,
    description="Ketra Lighting API",
    author="Joe Savage",
    author_email="joe@savage.zone",
    url="https://github.com/s4v4g3/aio-ketra-api.git",
    keywords=["OpenAPI", "OpenAPI-Generator", "Ketra Lighting API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    python_requires=">=3.6",
    include_package_data=True,
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
)
