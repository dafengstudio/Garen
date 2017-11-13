#!/usr/bin/env bash
rm -rf build
rm -rf dist
rm -rf Garen.egg-info
python setup.py sdist
python setup.py install
twine upload dist/*
