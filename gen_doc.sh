#!/usr/bin/env bash
mkdir -p docs
cd doc_sources
make html
cp -rf ./build/html/* ../docs/
cd -
git add -f docs/*
git commit -a -m 'auto build'
git push origin
open http://show.timger.info/Garen/index.html