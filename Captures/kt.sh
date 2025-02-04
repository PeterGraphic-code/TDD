#!/bin/bash

read -p "Entrez la première valeur : " a
read -p "Entrez la deuxième valeur : " b

echo "Opérations disponibles :"
echo "1. Addition"
echo "2. Soustraction"
echo "3. Multiplication"
echo "4. Division"

read -p "Choisissez une opération (1-4): " choix

case $choix in
    1) echo "Résultat de l'addition : $(($a + $b))" ;;
    2) echo "Résultat de la soustraction : $(($a - $b))" ;;
    3) echo "Résultat de la multiplication : $(($a * $b))" ;;
    4) if [ $b -ne 0 ]; then
           echo "Résultat de la division : $(echo "scale=2; $a / $b" | bc)"
       else
           echo "Erreur : Division par zéro."
       fi ;;
    *) echo "Opération invalide." ;;
esac
