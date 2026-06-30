#!/bin/bash
while true; do
    clear
    printf '0    ft_alembic\n'
    printf '1    ft_distillation\n'
    printf '2    transmutation\n'
    printf '3    ft_kaboom\n'
    printf 'q    quit\n'
    read -p "choose action : " action
    clear
    if [ "$action" = "0" ]; then
        for i in 0 1 2 3 4 5; do
            python3 ft_alembic_$i.py
            printf '\n'
        done
    elif [ "$action" = "1" ]; then
        for i in 0 1; do
            python3 ft_distillation_$i.py
            printf '\n'
        done
    elif [ "$action" = "2" ]; then
        for i in 0 1 2; do
            python3 ft_transmutation_0.py
            printf '\n'
        done
    elif [ "$action" = "3" ]; then
        for i in 0 1; do
            python3 ft_kaboom_$i.py
            printf '\n'
        done
    elif [ "$action" = "q" ]; then
        exit
    else
        echo 'unknown command: $action'
    fi
    read -p "press Enter to pursue" dummy
done
