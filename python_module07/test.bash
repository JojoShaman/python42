#!/bin/bash

while true; do
    clear
    printf '0    battle.py\n'
    printf '1    capacitor.py\n'
    printf '2    tournament.py\n'
    printf 'q    quit\n\n'
    read -p "choose action : " action
    clear
    if [ "$action" = "0" ]; then
        python3 battle.py
    elif [ "$action" = "1" ]; then
        python3 capacitor.py
    elif [ "$action" = "2" ]; then
        python3 tournament.py
    elif [ "$action" = "q" ]; then
        exit
    else
        echo "Unkown command $action"
    fi
    printf '\n'
    read -p "press Enter to pursue" dummy
done