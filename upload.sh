#!/usr/bin/env bash
rm -vrf build
rm -vrf dist
rm -vrf Garen.egg-info
python setup.py sdist
twine upload dist/*