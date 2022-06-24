#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names), encoding=kwargs.get("encoding", "utf8")
    ) as fh:
        return fh.read()


setup(
    name="logall",
    version="0.0.0",
    license="Apache-2.0",
    description="Unifies metric logging from different logging packages",
    long_description="{}\n{}".format(
        re.compile("^.. start-badges.*^.. end-badges", re.M | re.S).sub(
            "", read("README.rst")
        ),
        re.sub(":[a-z]+:`~?(.*?)`", r"``\1``", read("CHANGELOG.rst")),
    ),
    author="Farshid Varno",
    author_email="fr.varno@gmail.com",
    url="https://github.com/fvarno/logall",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        # uncomment if you test on these interpreters:
        "Topic :: Utilities",
    ],
    project_urls={
        "Documentation": "https://logall.readthedocs.io/",
        "Changelog": "https://logall.readthedocs.io/en/latest/changelog.html",
        "Issue Tracker": "https://github.com/fvarno/logall/issues",
    },
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
    python_requires=">=3.6",
    install_requires=[
        "torch",
        "tensorboard",
        "polyaxon",
        "mlflow",
        # eg: 'aspectlib==1.1.1', 'six>=1.7',
    ],
    extras_require={
        "test": [
            "pytest",
            "pytest-cov",
            "codecov",
        ]
    },
)
