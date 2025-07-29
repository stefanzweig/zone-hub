#!/usr/bin/env python
from os.path import abspath, dirname, join
from setuptools import find_packages, setup

VERSION = "0.1.0.dev2"
with open(
    join(dirname(abspath(__file__)), "README.rst"), encoding="utf-8"
) as f:
    LONG_DESCRIPTION = f.read()

CLASSIFIERS = """
Development Status :: 5 - Production/Stable
License :: OSI Approved :: Apache Software License
Operating System :: OS Independent
Programming Language :: Python :: 3
Programming Language :: Python :: 3 :: Only
Programming Language :: Python :: 3.8
Programming Language :: Python :: 3.9
Programming Language :: Python :: 3.10
""".strip().splitlines()
DESCRIPTION = "Zone framework for acceptance testing "
KEYWORDS = "framework automation-test automation-testing atdd bdd"


setup(
    name="zone-hub",
    version=VERSION,
    author="Stefan Zweig",
    author_email="stefan.zweig@gmail.com",
    url="http://10.133.122.70/liuhaijiang/zmclient",
    project_urls={
        "Source": "http://10.133.122.70/liuhaijiang/zmclient",
    },
    download_url="https://pypi.org/project/zone-hub",
    license="Apache License 2.0",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/x-rst",
    keywords=KEYWORDS,
    platforms="any",
    python_requires=">=3.8",
    classifiers=CLASSIFIERS,
    package_dir={"": "src"},
    package_data={"zone": ["etc/zonemaster_config.yaml"]},
    packages=find_packages("src"),
    entry_points={"console_scripts": []},
    extras_require={
        "dev": [
            "pytest",
            "black",
            "furo",
            "sphinx-autobuild",
            "codespell",
            "sphinx-copybutton",
            "beanbag-docutils>=2.0",
            "pygments-csv-lexer",
        ],
        "docs": [
            "furo",
            "sphinx-autobuild",
            "codespell",
            "sphinx-copybutton",
            "beanbag-docutils>=2.0",
            "pygments-csv-lexer",
        ],
    },
    install_requires=["thrift", "PyYAML==6.0.2"],
)
