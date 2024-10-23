#!/bin/bash

# Define the command and the configurations
command="python3 main.py"
configs=(
    "photo 1 1 0.01 10000 0 0"
    "photo 1 1 0.02 10000 0 0"
    "photo 1 1 0.05 10000 0 0"
    "photo 1 1 0.1 10000 0 0"
)

# Log file for capturing errors
logfile="tmux_error_log.txt"

# Loop through each configuration and run the command 10 times for each
session_number=1
for config in "${configs[@]}"; do
    for run in {1..10}; do
        session_name="session_${session_number}"
        
        # Redirect stdout and stderr to a log file specific to the session
        full_command="$command $config > /tmp/session_${session_number}_output.log 2>&1; exec bash"

        # Start tmux session and log any errors
        tmux new-session -d -s $session_name "$full_command" 2>> $logfile
        
        # Check if tmux session creation failed
        if [ $? -ne 0 ]; then
            echo "Error starting session $session_name at $(date)" >> $logfile
        else
            echo "Started Tmux session $session_name with command: $full_command"
        fi

        ((session_number++))

        # Sleep to reduce parallel session creation overload
        sleep 1
    done
done


