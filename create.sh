#! /bin/sh

echo Creating from template for day $1

sed -e "s/__DAY__/$1/g" template.py > puzzles/day$1.py
