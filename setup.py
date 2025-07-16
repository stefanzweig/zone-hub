setup(
    name="zoneclient",
    version="0.1.0",
    description="A short description of your package",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Liu Haijiang",
    author_email="liuhaijiang@saicmotor.com",
    url="https://github.com/stefanzweig/dumb",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        "PyYAML==6.0.2",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.8",
)



#!/usr/bin/env python

from os.path import abspath, dirname, join
from setuptools import find_packages, setup

# Version number typically updated by running `invoke set-version <version>`.
# Run `invoke --help set-version` or see tasks.py for details.
VERSION = "0.1.0.dev1"
with open(join(dirname(abspath(__file__)), "README.md")) as f:
    LONG_DESCRIPTION = f.read()
    base_url = "http://10.133.122.70/liuhaijiang/zmclient/-/blob/main/"
    for text in ("INSTALL", "CONTRIBUTING"):
        search = f"`<{text}.rst>`__"
        replace = f"`{text}.rst <{base_url}/{text}.rst>`__"
        if search not in LONG_DESCRIPTION:
            raise RuntimeError(f"{search} not found from README.rst")
        LONG_DESCRIPTION = LONG_DESCRIPTION.replace(search, replace)
CLASSIFIERS = """
Development Status :: 5 - Production/Stable
License :: OSI Approved :: Apache Software License
Operating System :: OS Independent
Programming Language :: Python :: 3
Programming Language :: Python :: 3 :: Only
Programming Language :: Python :: 3.8
Programming Language :: Python :: 3.9
Programming Language :: Python :: 3.10
Programming Language :: Python :: 3.11
Programming Language :: Python :: 3.12
Programming Language :: Python :: 3.13
Programming Language :: Python :: 3.14
Framework :: Zone Framework
""".strip().splitlines()
DESCRIPTION = (
    "Zone framework for acceptance testing "
)
KEYWORDS = (
    "framework automation testautomation testing atdd bdd"
)
PACKAGE_DATA = [
    join("htmldata", directory, pattern)
    for directory in ("rebot", "libdoc", "testdoc", "lib", "common")
    for pattern in ("*.html", "*.css", "*.js")
] + ["api/py.typed", "logo.png"]


setup(
    name="robotframework",
    version=VERSION,
    author="Pekka Klärck",
    author_email="peke@eliga.fi",
    url="https://robotframework.org",
    project_urls={
        "Source": "https://github.com/robotframework/robotframework",
    },
    download_url="https://pypi.org/project/zoneclient",
    license="Apache License 2.0",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/x-rst",
    keywords=KEYWORDS,
    platforms="any",
    python_requires=">=3.8",
    classifiers=CLASSIFIERS,
    package_dir={"": "src"},
    package_data={"zoneclient": PACKAGE_DATA},
    packages=find_packages("src"),
    entry_points={
        "console_scripts": [
        ]
    },
)
