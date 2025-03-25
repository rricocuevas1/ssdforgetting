#!/bin/bash

command="python3 main.py"
configs=(
    "S_1M_10M 1 1 0.1 10000 0 1"
    "S_10M_10M 1 1 0.1 10000 0 1"
    "S_100M_100K 1 1 0.1 10000 0 1"
    "S_100M_1M 1 1 0.1 10000 0 1"
    "S_100M_10M 1 1 0.1 10000 0 1"
)


wait_for_sessions() {
    echo "Waiting for all tmux sessions for the current config to complete..."
    while [ $(tmux list-sessions 2>/dev/null | grep "session_" | wc -l) -gt 0 ]; do
        sleep 10
    done
    echo "All sessions for the current config completed."
}

session_number=1
runs_per_config=5

for config in "${configs[@]}"; do
    for run in $(seq 1 $runs_per_config); do
        session_name="session_${session_number}"
        full_command="$command $config"
        tmux new-session -d -s "$session_name" "$full_command"
        echo "Started Tmux session $session_name with command: $full_command"
        ((session_number++))
        sleep 1
    done
    wait_for_sessions
done

echo "All configurations processed."