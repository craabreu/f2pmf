#!/usr/bin/env bash

# exit when any command fails
set -e

flake8 f2pmf/
isort f2pmf/f2pmf.py
sphinx-build docs/ docs/_build
pytest -v --cov=f2pmf --doctest-modules f2pmf/
