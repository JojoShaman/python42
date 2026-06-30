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
        python3 ft_alembic_0.py
        read -p "" next
        printf '\n'
        python3 ft_alembic_1.py
        read -p "" next
        printf '\n'
        python3 ft_alembic_2.py
        read -p "" next
        printf '\n'
        python3 ft_alembic_3.py
        read -p "" next
        printf '\n'
        python3 ft_alembic_4.py
        read -p "" next
        printf '\n'
        python3 ft_alembic_5.py
        printf '\n'
    elif [ "$action" = "1" ]; then
        python3 ft_distillation_0.py
        read -p "" next
        printf '\n'
        python3 ft_distillation_1.py
        printf '\n'
    elif [ "$action" = "2" ]; then
        python3 ft_transmutation_0.py
        read -p "" next
        printf '\n'
        python3 ft_transmutation_1.py
        read -p "" next
        printf '\n'
        python3 ft_transmutation_2.py
        printf '\n'
    elif [ "$action" = "3" ]; then
        python3 ft_kaboom_0.py
        read -p "" next
        printf '\n'
        python3 ft_kaboom_1.py
        printf '\n'
    elif [ "$action" = "q" ]; then
        exit
    else
        echo 'unknown command: $action'
    fi
    read -p "press Enter to pursue" dummy
done
