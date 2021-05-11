#!/bin/bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install poetry
poetry install
rm coefficients.json
echo '{"b0": 0, "b1": 0}' > coefficients.json