#!/bin/bash

# Define the command and the configurations
command="python3 main.py"
configs=(
    "flight 1 1 0.1 2000 0 0"
    "flight 1 1 0.25 2000 0 0"
    "flight 1 1 0.5 2000 0 0"
    "flight 1 1 0.75 2000 0 0"
    "flight 1 1 0.1 10000 0 0"
    "flight 1 1 0.1 50000 0 0"
    "flight 1 1 0.1 100000 0 0"
    "photo 1 0.1 0.001 2000 0 0"
    "photo 1 0.1 0.005 2000 0 0"
    "photo 1 0.1 0.01 2000 0 0"
    "photo 1 0.1 0.02 2000 0 0"
    "photo 1 0.1 0.005 10000 0 0"
    "photo 1 0.1 0.005 50000 0 0"
    "photo 1 0.1 0.005 100000 0 0"
    "wiki 1 1 0.01 2000 0 0"
    "wiki 1 1 0.1 2000 0 0"
    "wiki 1 1 0.25 2000 0 0"
    "wiki 1 1 0.5 2000 0 0"
    "flight 0.25 1 120 2000 0 1"
    "flight 0.5 1 120 2000 0 1"
    "flight 0.75 1 120 2000 0 1"
    "flight 1 1 120 2000 0 1"
    "photo 0.25 1 42 2000 0 1"
    "photo 0.5 1 42 2000 0 1"
    "photo 0.75 1 42 2000 0 1"
    "photo 1 1 42 2000 0 1"
    "wiki 0.25 1 1311 2000 0 1"
    "wiki 0.5 1 1311 2000 0 1"
    "wiki 0.75 1 1311 2000 0 1"
    "wiki 1 1 1311 2000 0 1"
    "flight 1 0.25 120 2000 0 1"
    "flight 1 0.5 120 2000 0 1"
    "flight 1 0.75 120 2000 0 1"
    "flight 1 1 120 2000 0 1"
    "photo 1 0.25 42 2000 0 1"
    "photo 1 0.5 42 2000 0 1"
    "photo 1 0.75 42 2000 0 1"
    "photo 1 1 42 2000 0 1"
    "wiki 1 0.25 1311 2000 0 1"
    "wiki 1 0.5 1311 2000 0 1"
    "wiki 1 0.75 1311 2000 0 1"
    "wiki 1 1 1311 2000 0 1"
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
