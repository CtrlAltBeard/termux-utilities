#!/bin/bash

# Log cleanup script for Termux
# Deletes logs older than X days

DAYS=7  # Change this to however many days you want

# Array of log directories
LOG_DIRS=(
    "$HOME/.config/logs"
    "$HOME/logs"
    "$HOME/var/log"
)
    # Add more directories as needed

# Loop through each directory and delete old logs
for dir in "${LOG_DIRS[@]}"; do
    if [ -d "$dir" ]; then
        echo "Cleaning logs in: $dir"
        find "$dir" -type f -name "*.log" -mtime +$DAYS -delete
        echo "Done: $dir"
    fi
done

echo "Log cleanup complete!"
