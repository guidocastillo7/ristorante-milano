#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r ./requirements.txt
python ristorante_milano/manage.py collectstatic --no-input
python ristorante_milano/manage.py migrate