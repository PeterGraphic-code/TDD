#!/bin/bash

read -p "Entrez un nombre : " nombre
read -p "Choisissez 'multiplication' ou 'division' : " operation

if [ "$operation" = "multiplication" ]; then
    for i in {1..10}; do
        echo "$nombre x $i = $(($nombre * $i))"
    done
elif [ "$operation" = "division" ]; then
    for i in {1..10}; do
        if [ $i -ne 0 ]; then
            echo "$nombre / $i = $(echo "scale=2; $nombre / $i" | bc)"
        fi
    done
else
    echo "Opération non reconnue."
fi
