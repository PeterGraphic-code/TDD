
#!/bin/bash

while true; do
    echo "--- Menu ---"
    echo "1. Option 1"
    echo "2. Option 2"
    echo "3. Quitter"
    read -p "Choisissez une option (1-3): " choix

    case $choix in
        1) echo "Vous avez choisi l'option 1." ;;
        2) echo "Vous avez choisi l'option 2." ;;
        3) echo "Au revoir!"; break ;;
        *) echo "Option invalide. Veuillez réessayer." ;;
    esac
done
