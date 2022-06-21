#!/usr/bin/env python
"""Setup environment for sea."""

from setuptools import setup, find_packages

exec(open("sea/__version__.py").read())
readme = open("README.md").read()

setup(
    name="sea",
    version="0.1.0",
    description="A Python Package",
    long_description=readme,
    author="sea",
    author_email="joyce.xinyue.wang@gmail.com",
    url="https://github.com/JoyceXinyueWang/sea",
    packages=find_packages(),
    package_dir={"sea": "sea"},
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "sea = sea.scripts.cli:cli",
            ]
        },
    install_requires=[
        "numpy==1.22.0",
        "scipy==0.19.1",
        "click==6.7",
        "pandas==0.22.0",
        "aboleth==0.7.0",
        "sklearn==0.0",
        "jupyter==1.0.0",
        "matplotlib==2.2.0",
        # "mypy==0.521",
        # "mypy_extensions==0.3.0",
        # "modron==0.1.0",
        # "dretch==0.1.0",
        # "glabrezu==0.3.0",
        ],
    # dependency_links=[
    #     "git+ssh://git@github.com/determinant-io/dretch.git@refactor#egg=dretch-0.1.0",
    #     "git+ssh://git@github.com/determinant-io/modron.git@develop#egg=modron-0.1.0",
    #     "git+ssh://git@github.com/determinant-io/glabrezu.git@develop#egg=glabrezu-0.3.0",
    # ],
    extras_require={
        "dev": [
            "pytest>=3.1.3",
            "pytest-flake8>=0.8.1",
            "pytest-mock>=1.6.2",
            "pytest-cov>=2.5.1",
            "pytest-regtest>=0.15.1",
            "flake8-docstrings>=1.1.0",
            "flake8-quotes>=0.11.0",
            "flake8-comprehensions>=1.4.1"
            ]
        },
    license="All Rights Reserved",
    zip_safe=False,
    keywords="sea",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Operating System :: POSIX",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.4",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    )
