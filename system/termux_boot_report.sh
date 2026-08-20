#!/bin/bash
LOG_FILE="$HOME/termux_boot_report.log"
{
    echo "===== Termux Boot Report - $(date) ====="
    echo -e "\n=== Disk Usage ==="
    df -h
    echo -e "\n=== Running Processes ==="
    ps aux | head -n 10
    echo -e "\n=== Network Status ==="
    ifconfig | grep "inet "
} >> "$LOG_FILE"
