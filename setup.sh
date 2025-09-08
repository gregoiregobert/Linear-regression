#!/bin/bash

# Crée l'environnement virtuel
python3 -m venv venv

# Active l'environnement
source venv/bin/activate

# Met à jour pip
pip install --upgrade pip

# Installe les dépendances
pip install -r requirements.txt

echo "✅ Environment setup complete!"
