#!/usr/bin/env bash
set -e

# create venv
python3 -m venv .venv

# activate
source .venv/bin/activate

# make sure tooling is fresh
python -m pip install --upgrade pip setuptools wheel

# install your project + deps
pip install -e .
