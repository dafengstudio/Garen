#!/usr/bin/env bash
mkdir -p docs
cd doc_sources
make html
cp -vrf ./build/html/* ../docs/
cd -
git add -f docs/*
git commit -a -m 'auto build'
git push origin