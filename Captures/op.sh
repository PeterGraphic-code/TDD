#!/bin/bash

etudiants=()

while true; do
    read -p "Entrez le nom de l'étudiant (ou 'fin' pour terminer) : " nom
    if [ "$nom" = "fin" ]; then
        break
    fi
    read -p "Entrez l'âge de l'étudiant : " age
    read -p "Entrez la classe de l'étudiant : " classe

    etudiant="$nom, $age ans, classe $classe"
    etudiants+=("$etudiant")
done

echo "Liste des étudiants :"
for etudiant in "${etudiants[@]}"; do
    echo "$etudiant"
done
