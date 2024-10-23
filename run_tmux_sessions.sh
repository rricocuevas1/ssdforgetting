#!/bin/bash

# Define the command and the configurations
command="python3 main.py"
configs=(
    "photo 1 1 0.01 10000 0 0"
    "photo 1 1 0.02 10000 0 0"
    "photo 1 1 0.05 10000 0 0"
    "photo 1 1 0.1 10000 0 0"
    "photo 1 1 0.25 10000 0 0"
    "photo 1 1 0.5 10000 0 0"
)

# Loop through each configuration and run the command 5 times for each
session_number=1
for config in "${configs[@]}"; do
    for run in {1..10}; do
        session_name="session_${session_number}"
        full_command="$command $config; bash"
        tmux new-session -d -s $session_name "$full_command"
        echo "Started Tmux session $session_name with command: $full_command"
        ((session_number++))
    done
done
