#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r ./requirements.txt
python manage.py ristorante_milano/collectstatic --no-input
python manage.py ristorante_milano/migrate