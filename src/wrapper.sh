#!/bin/bash
if [[ -x "$(command -v python3)" ]]
then
    pyv="$(python3 -V 2>&1)"
    if [[ $pyv == "Python 3"* ]]
    then
        python3 main.py $1
        exit 0
    else
        echo 'Error:
        Wrong version of Python. Please update to Python 3 or later.' >&2
        exit 1
    fi
else
    echo 'Error: 
    This program runs on Python, but it looks like Python is not installed.
    To install Python, check out https://installpython3.com/' >&2
    exit 1
fi