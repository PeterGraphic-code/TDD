#!/bin/bash

until [ -f "$fichier" ]; do
    read -p "Entrez le chemin du fichier : " fichier
    if [ ! -f "$fichier" ]; then
        echo "Le fichier n'existe pas. Veuillez réessayer."
    fi
done

read -p "Entrez le mot à rechercher : " mot

if grep -q "$mot" "$fichier"; then
    echo "Le mot '$mot' a été trouvé dans le fichier."
else
    echo "Le mot '$mot' n'a pas été trouvé dans le fichier."
fi
