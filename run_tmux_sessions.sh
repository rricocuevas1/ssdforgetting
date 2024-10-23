#!/bin/bash

# Define the command and the configurations
command="python3 main.py"
configs=(
    "photo 1 1 0.01 10000 0 0"
    "photo 1 1 0.02 10000 0 0"
    "photo 1 1 0.05 10000 0 0"
    "photo 1 1 0.1 10000 0 0"
)

# Log file to capture errors
logfile="tmux_error_log.txt"
tmux_log_dir="/tmp/tmux_logs"

# Create the directory for tmux logs if it doesn't exist
mkdir -p $tmux_log_dir

# Loop through each configuration and run the command 10 times for each
session_number=1
for config in "${configs[@]}"; do
    for run in {1..10}; do
        session_name="session_${session_number}"
        full_command="$command $config; exec bash"

        # Enable verbose logging for tmux sessions
        tmux -vv new-session -d -s $session_name "$full_command" 2>> $logfile
        
        # Check if tmux session creation failed
        if [ $? -ne 0 ]; then
            echo "Error starting session $session_name at $(date)" >> $logfile
        else
            echo "Started Tmux session $session_name with command: $full_command"
        fi

        # Move the tmux log to a specific location
        mv /tmp/tmux-server-*.log $tmux_log_dir/ 2> /dev/null
        
        # Increment session number
        ((session_number++))

        # Sleep to reduce parallel session creation overload
        sleep 1
    done
done

