#!/bin/bash

# Demander le nom du dossier
read -p "Entrez le nom du dossier : " dossier

# Créer le dossier s'il n'existe pas
if [ ! -d "$dossier" ]; then
    mkdir "$dossier"
    echo "Dossier '$dossier' créé."
else
    echo "Le dossier '$dossier' existe déjà."
fi

# Demander le nombre de fichiers texte à créer
read -p "Combien de fichiers texte souhaitez-vous créer ? " nombre_fichiers

# Créer les fichiers texte dans le dossier
for ((i=1; i<=nombre_fichiers; i++)); do
    touch "$dossier/fichier$i.txt"
    echo "Fichier 'fichier$i.txt' créé dans '$dossier'."
done

# Lister tous les fichiers créés dans le dossier
echo "Liste des fichiers dans '$dossier' :"
ls -l "$dossier"
