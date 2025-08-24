#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
echo "✅ Environnement prêt ! Active avec 'source venv/bin/activate'"
