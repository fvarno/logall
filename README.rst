========
Overview
========

.. start-badges

.. image:: https://readthedocs.org/projects/logall/badge/?style=flat
    :target: https://logall.readthedocs.io/
    :alt: Documentation Status

.. image:: https://github.com/fvarno/logall/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/fvarno/logall/actions

.. image:: https://codecov.io/gh/fvarno/logall/branch/main/graphs/badge.svg?branch=main
    :alt: Coverage Status
    :target: https://codecov.io/github/fvarno/logall

.. image:: https://img.shields.io/pypi/v/logall.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/logall

.. image:: https://img.shields.io/pypi/wheel/logall.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/logall

.. image:: https://img.shields.io/pypi/pyversions/logall.svg
    :alt: Supported versions
    :target: https://pypi.org/project/logall

.. image:: https://img.shields.io/pypi/implementation/logall.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/logall

.. image:: https://img.shields.io/github/commits-since/fvarno/logall/v0.0.3.svg
    :alt: Commits since latest release
    :target: https://github.com/fvarno/logall/compare/v0.0.3...main



.. end-badges

Unifies metric logging from different logging packages

* Free software: Apache Software License 2.0

Installation
============

::

    pip install logall

You can also install the in-development version with::

    pip install https://github.com/fvarno/logall/archive/main.zip


Documentation
=============


https://logall.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
