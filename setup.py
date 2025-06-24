from setuptools import setup, find_packages

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
