#!/bin/sh
[ -f ./install.sh ] && (echo Install ...; sh ./install.sh)

[ -L ./tests/dd1 ] && (echo Unit tests ...; python3 -B -m unittest discover -s tests)
