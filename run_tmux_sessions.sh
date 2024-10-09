#!/bin/bash

# Define the command and the configurations
command="python3 main.py"
configs=(
    "photo 1 1 0.03 10000 0 0"
    "flight 1 1 0.25 25000 0 0"
    "flight 1 1 0.25 50000 0 0"
    "flight 1 1 0.25 100000 0 0"
    "photo 1 1 0.01 25000 0 0"
    "photo 1 1 0.01 50000 0 0"
    "photo 1 1 0.01 100000 0 0"
)

# Loop through each configuration and run the command 5 times for each
session_number=1
for config in "${configs[@]}"; do
    for run in {1..10}; do
        session_name="session_${session_number}"
        full_command="$command $config; exec bash"
        tmux new-session -d -s $session_name "$full_command"
        echo "Started Tmux session $session_name with command: $full_command"
        ((session_number++))
    done
done
