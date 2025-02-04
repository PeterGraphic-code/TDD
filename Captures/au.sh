#!/bin/bash

while true; do
    read -p "Entrez un mot (tapez 'Au revoir!' pour quitter) : " mot
    if [ "$mot" = "Au revoir!" ]; then
        echo "Au revoir!"
        break
    else
        echo "Vous avez entré : $mot"
    fi
done
